#!/usr/bin/env python3
"""Sync GitHub repos into their vault project notes (progress digest + docs mirror).

Config-driven: add an entry to PROJECTS to onboard a new repo-backed project to
the same operating model. For each project (pull-only, repo -> vault):
  1. Progress digest: append new commits / merged PRs / open issues to the
     project note's ## Log. Idempotent: items already present in the note
     (by short SHA or #num) are skipped, so re-runs never double-log.
  2. Docs mirror: copy key root docs + all docs/**.md into a read-only,
     gitignored `repo-docs/` folder next to the note.

Graceful: any gh/network failure for a project prints a [skip] line and moves
on; one bad repo never blocks the others. Mirrors the gcalcli pattern in /today.

Usage:
  python3 sync-repos.py                 # dry-run (report only)
  python3 sync-repos.py --apply         # write digests + refresh mirrors
  python3 sync-repos.py --only cate     # limit to repos matching a substring
"""
import base64
import json
import shutil
import subprocess
import sys
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
STATE = Path(__file__).resolve().parent / ".repo-sync-state.json"

# Each project maps one repo to one vault note. The docs mirror lives at
# <note parent>/repo-docs/.
PROJECTS = [
    {"repo": "cate-hq/platform",
     "note": "00 Human/30 Projects/Ridgewells/Ridgewells.md"},
    {"repo": "Dual-Logic/platform",
     "note": "00 Human/30 Projects/Dual Logic Platform/Dual Logic Platform.md"},
]

ROOT_DOCS = ["README.md", "STRATEGY.md", "CONCEPTS.md", "AGENTS.md"]
FALLBACK_DAYS = 14  # lookback when no prior state exists for a repo


class GhError(Exception):
    pass


def gh(args, parse=True):
    """Run a gh command; return parsed JSON (or raw text). Raise on failure."""
    try:
        out = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        raise GhError("gh CLI not installed")
    except subprocess.TimeoutExpired:
        raise GhError("gh timed out")
    if out.returncode != 0:
        raise GhError(out.stderr.strip() or f"gh exited {out.returncode}")
    return json.loads(out.stdout) if parse else out.stdout


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except json.JSONDecodeError:
            pass
    return {}


def since_iso(state, repo):
    if state.get(repo, {}).get("last_run"):
        return state[repo]["last_run"]
    return (datetime.now(timezone.utc) - timedelta(days=FALLBACK_DAYS)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def fetch_progress(repo, since):
    commits = gh(["api", f"repos/{repo}/commits?since={since}&per_page=100"])
    commits = [
        {"sha": c["sha"][:7], "msg": c["commit"]["message"].splitlines()[0].strip()}
        for c in commits
    ]
    prs = gh(["pr", "list", "--repo", repo, "--state", "merged",
              "--limit", "50", "--json", "number,title,mergedAt"])
    prs = [p for p in prs if p.get("mergedAt", "") >= since]
    issues = gh(["issue", "list", "--repo", repo, "--state", "open",
                 "--limit", "50", "--json", "number,title"])
    return commits, prs, issues


def already_logged(note_text):
    shas = set(re.findall(r"\b[0-9a-f]{7}\b", note_text))
    nums = set(re.findall(r"#(\d+)", note_text))
    return shas, nums


def build_digest_block(repo, commits, prs, issues, now):
    lines = [f"### {now:%Y-%m-%d} (repo sync {now:%H:%M})"]
    if commits:
        shown = "; ".join(f"`{c['sha']}` {c['msg']}" for c in commits[:15])
        extra = f" (+{len(commits) - 15} more)" if len(commits) > 15 else ""
        lines.append(f"- Commits ({len(commits)}): {shown}{extra}")
    if prs:
        shown = "; ".join(f"#{p['number']} {p['title']}" for p in prs[:10])
        lines.append(f"- Merged PRs ({len(prs)}): {shown}")
    if issues:
        shown = "; ".join(f"#{i['number']} {i['title']}" for i in issues[:10])
        lines.append(f"- Open issues ({len(issues)}): {shown}")
    lines.append(f"- Docs mirrored to `repo-docs/` from {repo}.")
    return "\n".join(lines)


def list_doc_paths(repo):
    tree = gh(["api", f"repos/{repo}/git/trees/HEAD?recursive=1"])["tree"]
    paths = [t["path"] for t in tree if t["type"] == "blob"]
    docs = [p for p in paths if p in ROOT_DOCS]
    docs += [p for p in paths if p.startswith("docs/") and p.endswith(".md")]
    return sorted(set(docs))


def fetch_file(repo, path):
    blob = gh(["api", f"repos/{repo}/contents/{path}"])
    return base64.b64decode(blob["content"]).decode("utf-8", "replace")


def refresh_mirror(mirror, repo, paths, now):
    if mirror.exists():
        shutil.rmtree(mirror)
    mirror.mkdir(parents=True)
    (mirror / "_GENERATED.md").write_text(
        "---\ntags: [generated]\n---\n\n"
        f"# repo-docs (generated mirror)\n\n"
        f"> Read-only mirror of `{repo}` docs. Do NOT edit here; changes belong "
        f"in the repo. Regenerated by `Machine/Scripts/sync-repos.py`.\n"
        f"> Last synced: {now:%Y-%m-%d %H:%M}.\n",
        encoding="utf-8",
    )
    for path in paths:
        dest = mirror / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(fetch_file(repo, path), encoding="utf-8")


def sync_one(project, apply, state, now):
    repo = project["repo"]
    note = VAULT / project["note"]
    mirror = note.parent / "repo-docs"
    try:
        commits, prs, issues = fetch_progress(repo, since_iso(state, repo))
        doc_paths = list_doc_paths(repo)
    except GhError as e:
        print(f"[skip] {repo}: {e}")
        return

    note_text = note.read_text(encoding="utf-8")
    seen_shas, seen_nums = already_logged(note_text)
    new_commits = [c for c in commits if c["sha"] not in seen_shas]
    new_prs = [p for p in prs if str(p["number"]) not in seen_nums]
    have_progress = bool(new_commits or new_prs)

    print(f"{repo}: {len(new_commits)} new commits, {len(new_prs)} new merged PRs, "
          f"{len(issues)} open issues, {len(doc_paths)} docs to mirror.")

    if not apply:
        if have_progress:
            print("  --- digest preview ---")
            print("  " + build_digest_block(repo, new_commits, new_prs, issues, now)
                  .replace("\n", "\n  "))
        return

    refresh_mirror(mirror, repo, doc_paths, now)
    if have_progress:
        block = build_digest_block(repo, new_commits, new_prs, issues, now)
        note.write_text(note_text.rstrip() + "\n" + block + "\n", encoding="utf-8")

    state[repo] = {
        "last_run": now.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }


def main():
    apply = "--apply" in sys.argv
    only = None
    if "--only" in sys.argv:
        i = sys.argv.index("--only")
        if i + 1 < len(sys.argv):
            only = sys.argv[i + 1]

    now = datetime.now().astimezone()
    state = load_state()
    projects = [p for p in PROJECTS if not only or only in p["repo"]]
    print(f"{'APPLY' if apply else 'DRY-RUN'}: {len(projects)} project(s)")
    for project in projects:
        sync_one(project, apply, state, now)
    if apply:
        STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
