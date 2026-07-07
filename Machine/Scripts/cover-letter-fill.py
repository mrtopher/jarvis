#!/usr/bin/env python3
"""cover-letter-fill.py — Render a styled .docx cover letter from a YAML content
file and a docxtpl (Jinja) template.

The template (Machine/Templates/cover-letter-reference.docx) reuses the resume's
header banner (name + contact line) and owns all layout. This script only pours
in the letter content, so every cover letter comes out identically formatted.

YAML schema:
    date:        "July 6, 2026"
    salutation:  "Dear Dan,"
    paragraphs:                 # one entry per body paragraph
      - "First paragraph..."
      - "Second paragraph..."
    closing:     "Sincerely,"
    signer:      "Chris Monnat"

Usage:
    Machine/Scripts/cover-letter-fill.py <content.yaml> [output.docx] [--template path]

If output is omitted, writes alongside the YAML with a .docx extension.

Requires: docxtpl, pyyaml  (pip3 install --user docxtpl pyyaml)
"""
import argparse
import os
import sys

from docxtpl import DocxTemplate
import yaml

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_TEMPLATE = os.path.join(VAULT_ROOT, "Machine", "Templates", "cover-letter-reference.docx")


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
