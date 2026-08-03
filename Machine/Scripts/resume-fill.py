#!/usr/bin/env python3
"""
resume-fill.py — Render a styled .docx resume from a YAML content file and a
docxtpl (Jinja) template.

The template owns ALL layout and styling — tables, fonts, margins, and (for the
styled template) the shaded achievements box and competency grid. This script
only pours in tailored content, so the format is identical every time.

Two templates ship with the vault:
  - resume-ats.docx        the default: a simple, single-column, ATS-friendly
                           layout with a keyword-rich categorized Skills line
                           (uses skill_groups[]).
  - resume-reference.docx  the styled version with shaded boxes and a
                           competency grid (uses competencies[]). Opt in with
                           --template Machine/Templates/resume-reference.docx.

Usage:
    Machine/Scripts/resume-fill.py <content.yaml> [output.docx] [--template path]

If output is omitted, writes alongside the YAML with a .docx extension.

Requires: docxtpl, pyyaml  (pip3 install --user docxtpl pyyaml)
"""
import argparse
import os
import sys

from docxtpl import DocxTemplate
import yaml

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_TEMPLATE = os.path.join(VAULT_ROOT, "Machine", "Templates", "resume-ats.docx")

# Length budgets. The summary paragraph and the Skills section are the two blocks
# that consistently overflow, so they are guarded here at build time. Tune these
# in one place if the layout changes.
SUMMARY_MAX_WORDS = 75          # aim ~60; a 3-4 sentence intro, not a paragraph
SKILL_GROUPS_MAX = 5            # ATS Skills line categories (skill_groups[])
SKILL_ENTRIES_MAX_CHARS = 80    # per-category keyword string, so it never wraps long


def check_lengths(context):
    """Return a list of length warnings for the blocks that tend to overflow."""
    warnings = []

    summary = (context.get("summary") or "").strip()
    words = len(summary.split())
    if words > SUMMARY_MAX_WORDS:
        warnings.append(
            f"summary is {words} words (max {SUMMARY_MAX_WORDS}); "
            f"cut to a 3-4 sentence intro of ~60 words."
        )

    groups = context.get("skill_groups") or []
    if len(groups) > SKILL_GROUPS_MAX:
        warnings.append(
            f"skill_groups has {len(groups)} categories (max {SKILL_GROUPS_MAX}); "
            f"merge or drop the weakest so the Skills section stays short."
        )
    for g in groups:
        label = (g.get("label") or "?").strip()
        entries = (g.get("entries") or "").strip()
        if len(entries) > SKILL_ENTRIES_MAX_CHARS:
            warnings.append(
                f"skill_groups '{label}' entries line is {len(entries)} chars "
                f"(max {SKILL_ENTRIES_MAX_CHARS}); cut the weakest keywords."
            )

    return warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("output", nargs="?")
    ap.add_argument("--template", default=DEFAULT_TEMPLATE)
    args = ap.parse_args()

    output = args.output or os.path.splitext(args.content)[0] + ".docx"

    for path, label in [(args.content, "content"), (args.template, "template")]:
        if not os.path.isfile(path):
            sys.exit(f"ERROR: {label} not found: {path}")

    with open(args.content, encoding="utf-8") as fh:
        context = yaml.safe_load(fh)

    warnings = check_lengths(context)

    doc = DocxTemplate(args.template)
    doc.render(context, autoescape=True)
    doc.save(output)
    print(f"Wrote {output}")

    for w in warnings:
        print(f"LENGTH WARNING: {w}", file=sys.stderr)
    if warnings:
        print(
            f"LENGTH WARNING: {len(warnings)} block(s) over budget in {args.content}. "
            f"Trim the YAML and re-run.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
