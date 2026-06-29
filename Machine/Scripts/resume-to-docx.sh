#!/usr/bin/env bash
#
# resume-to-docx.sh — Convert a Markdown resume to a styled .docx.
#
# Styling is inherited from Machine/Templates/resume-reference.docx, so you
# style that ONE file in Word once and every resume matches it forever.
#
# Usage:
#   Machine/Scripts/resume-to-docx.sh <input.md> [output.docx]
#
# If output is omitted, writes alongside the input with a .docx extension.
# The internal "## Tailoring notes" section (and any trailing rule) is stripped
# so it never ships to an employer.
#
# Requires: pandoc  (brew install pandoc)

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REF="$VAULT_ROOT/Machine/Templates/resume-reference.docx"

IN="${1:?Usage: resume-to-docx.sh <input.md> [output.docx]}"
OUT="${2:-${IN%.md}.docx}"

command -v pandoc >/dev/null 2>&1 || { echo "ERROR: pandoc not found. Run: brew install pandoc" >&2; exit 1; }
[ -f "$IN" ]  || { echo "ERROR: input not found: $IN" >&2; exit 1; }
[ -f "$REF" ] || { echo "ERROR: reference template not found: $REF" >&2; exit 1; }

TMP="$(mktemp -t resume).md"
trap 'rm -f "$TMP"' EXIT

# Drop the internal "## Tailoring notes" section and trim any trailing blank/--- lines.
awk '
  /^## Tailoring notes/ { exit }
  { c++; line[c]=$0 }
  END {
    while (c>0 && (line[c] ~ /^[[:space:]]*$/ || line[c] ~ /^---[[:space:]]*$/)) c--
    for (i=1; i<=c; i++) print line[i]
  }
' "$IN" > "$TMP"

pandoc "$TMP" --reference-doc "$REF" -o "$OUT"
echo "Wrote $OUT"
