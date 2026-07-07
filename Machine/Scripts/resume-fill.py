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

    doc = DocxTemplate(args.template)
    doc.render(context, autoescape=True)
    doc.save(output)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
