---
type: resource
status: active
tags: [job-search, resume]
---

# Resumes

Drop your current and most recent resumes here (markdown, PDF, or DOCX).

The `/job-apply` workflow reads this folder when you choose to apply to a job. It uses the **most recent** resume as the base for tailoring and pulls supporting detail from older ones.

Name files so the latest is obvious, e.g. `2026-06 Resume.md`.

## Tailored resume → .docx (style once)
When you apply, `/job-apply` writes the tailored content as a YAML data file into the company folder and then pours it into a house template to produce a formatted `.docx`:

`Machine/Scripts/resume-fill.py <content.yaml> [output.docx] [--template path]`

Two templates ship with the vault; the script fills them via Jinja tags (`{{ ... }}`, `{% for %}`), so every resume comes out identically formatted and you never restyle individual resumes again:

- **`Machine/Templates/resume-ats.docx`** — the **default**. A simple, single-column, ATS-friendly layout with a keyword-rich categorized Skills line. Uses `skill_groups[]`.
- **`Machine/Templates/resume-reference.docx`** — the styled version: tables, the shaded achievements box, and the three-column competency grid. Uses `competencies[]`. Opt in with `--template "Machine/Templates/resume-reference.docx"`.

Shared tag schema (both templates read from the same YAML): `target_title`, `summary`, `achievements[]` (`label`, `text`), and `experience[]` (`company`, `location`, `dates`, `role`, `summary`, `bullets[]`). Template-specific: the styled one also uses `target_subtitle` and `competencies[]` (sliced across 3 columns: `[:5]`, `[5:10]`, `[10:]`); the ATS one uses `skill_groups[]` (`label`, `entries` — note the key is `entries`, not `items`). Education is hardcoded in both templates.

Requires `docxtpl` and `pyyaml` (`pip3 install --user docxtpl pyyaml`, one-time).
