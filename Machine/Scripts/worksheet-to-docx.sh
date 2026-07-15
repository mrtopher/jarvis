#!/usr/bin/env bash
#
# worksheet-to-docx.sh — Convert a Markdown or HTML worksheet to a branded .docx.
#
# Styling (fonts, heading colors, and any header/footer logo you add) is
# inherited from Machine/Templates/power-automate-reference.docx, so you style
# that ONE file once and every worksheet matches it forever. Open the .docx in
# Google Docs and File > Save as Google Docs to get a native, editable Doc.
#
# Usage:
#   Machine/Scripts/worksheet-to-docx.sh <input.md|input.html> [output.docx]
#
# If output is omitted, writes alongside the input with a .docx extension.
#
# Requires: pandoc  (brew install pandoc)

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REF="$VAULT_ROOT/Machine/Templates/power-automate-reference.docx"

IN="${1:?Usage: worksheet-to-docx.sh <input.md|input.html> [output.docx]}"
OUT="${2:-${IN%.*}.docx}"

command -v pandoc >/dev/null 2>&1 || { echo "ERROR: pandoc not found. Run: brew install pandoc" >&2; exit 1; }
[ -f "$IN" ]  || { echo "ERROR: input not found: $IN" >&2; exit 1; }
[ -f "$REF" ] || { echo "ERROR: reference template not found: $REF" >&2; exit 1; }

pandoc "$IN" --reference-doc "$REF" -o "$OUT"
echo "Wrote $OUT"
