#!/usr/bin/env python3
"""One-off import: transform CRM person notes into vault Person template (flat files)."""
import re
import sys
from pathlib import Path

SRC = Path.home() / "Documents/jarvis/crm/people"
DST = Path(__file__).resolve().parents[2] / "00 Human/50 People"

FIELD_RE = re.compile(r"^-\s*(Title|Company|Type|Email|Phone|Location)\s*:\s*(.*)$", re.I)


def yq(value: str) -> str:
    """Quote a YAML scalar safely."""
    if not value:
        return ""
    return '"' + value.replace('"', '\\"') + '"'


def parse(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    name = path.stem
    fields = {}
    note_lines = []
    for ln in lines:
        stripped = ln.strip()
        if stripped.startswith("# ") and not name_set(fields):
            name = stripped[2:].strip()
            fields["_name_found"] = True
            continue
        m = FIELD_RE.match(stripped)
        if m:
            fields[m.group(1).lower()] = m.group(2).strip()
            continue
        if stripped in ("***", "---") or stripped.startswith("***"):
            continue
        note_lines.append(ln)
    # trim leading/trailing blank note lines
    while note_lines and not note_lines[0].strip():
        note_lines.pop(0)
    while note_lines and not note_lines[-1].strip():
        note_lines.pop()
    return name, fields, note_lines


def name_set(fields):
    return fields.get("_name_found", False)


def clean_email(raw: str) -> str:
    return raw.strip().strip("<>").replace("mailto:", "").strip()


def build(name, fields, note_lines):
    title = fields.get("title", "")
    company = fields.get("company", "")
    location = fields.get("location", "")
    email = clean_email(fields.get("email", ""))
    phone = fields.get("phone", "").strip()

    fm = ["---", "type: person", f"name: {yq(name)}"]
    if title:
        fm.append(f"title: {yq(title)}")
    if company:
        fm.append(f"company: {yq(company)}")
    if location:
        fm.append(f"location: {yq(location)}")
    fm.append("relationship:")
    fm.append("tags: [person]")
    fm.append("---")

    # Overview line
    if title and company:
        ov = f"{title} at {company}"
    elif title:
        ov = title
    elif company:
        ov = f"At {company}"
    else:
        ov = "Imported contact."
    if location:
        ov = f"{ov} — {location}."
    elif not ov.endswith("."):
        ov = f"{ov}."

    body = [
        "",
        f"# {name}",
        "",
        "## Overview",
        f"> {ov}",
        "",
        "## Contact",
        f"- **Email:** {email}",
        f"- **Phone:** {phone}",
        "- **LinkedIn:**",
        "",
        "## Projects",
        "-",
        "",
        "## Notes",
    ]
    if note_lines:
        body.extend(note_lines)
    body.extend([
        "",
        "## Log",
        "### 2026-06-29",
        "- Imported from CRM.",
        "",
    ])
    return "\n".join(fm + body)


def main():
    apply = "--apply" in sys.argv
    created, skipped = [], []
    for src in sorted(SRC.glob("*.md")):
        name, fields, notes = parse(src)
        out = DST / f"{src.stem}.md"
        if out.exists():
            skipped.append(name)
            continue
        content = build(name, fields, notes)
        created.append(name)
        if apply:
            out.write_text(content, encoding="utf-8")
    mode = "WROTE" if apply else "DRY-RUN would create"
    print(f"{mode}: {len(created)} | skipped (exists): {len(skipped)}")
    if skipped:
        print("Skipped:", ", ".join(skipped))
    if not apply and created:
        print("\nSample output (first person):")
        s = sorted(SRC.glob("*.md"))[0]
        n, f, nt = parse(s)
        print(build(n, f, nt))


if __name__ == "__main__":
    main()
