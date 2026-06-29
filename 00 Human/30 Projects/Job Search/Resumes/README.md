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
When you apply, `/job-apply` writes the tailored content as a YAML data file into the company folder and then pours it into the house template to produce a styled `.docx`:

`Machine/Scripts/resume-fill.py <content.yaml> [output.docx]`

All layout AND styling — tables, the shaded achievements box, the competency grid, fonts, headings, spacing — lives in one file: **`Machine/Templates/resume-reference.docx`**. The script only fills in content via Jinja tags (`{{ ... }}`, `{% for %}`), so every resume comes out identically formatted. You never restyle individual resumes again.

The template's tag schema: `target_title`, `target_subtitle`, `summary`, `achievements[]` (`label`, `text`), `competencies[]` (sliced across 3 columns: `[:5]`, `[5:10]`, `[10:]`), and `experience[]` (`company`, `location`, `dates`, `role`, `summary`, `bullets[]`). Education and Toolkit are currently hardcoded in the template.

Requires `docxtpl` and `pyyaml` (`pip3 install --user docxtpl pyyaml`, one-time).
