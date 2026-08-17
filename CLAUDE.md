# CLAUDE.md

This repository is an **Obsidian vault operating system** packaged for community use.

## What this vault is
- `00 Human/` = user-owned notes and source-of-truth information
- `Machine/` = workflows, templates, personalization files, scripts, and outputs
- `System/` = onboarding and operating docs

## This package
- This is the **starter edition**.
- It is sanitized for distribution.
- `emai-command-center` is intentionally excluded.
- Commands are written to work from the vault root using relative paths.

## Included commands
- `/start`
- `/interview`
- `/today`
- `/new`
- `/closeday`
- `/meeting-notes`
- `/job-apply`
- `/content`
- `/research`

## Personalization model
`/interview` updates these files:
- `00 Human/70 Context/business-profile.md`
- `00 Human/70 Context/audience-profile.md`
- `00 Human/70 Context/writing-style.md`
- `Machine/Personalization/operator-profile.md`
- `Machine/Personalization/today-prompt.md`
- `Machine/Personalization/closeday-prompt.md`
- `Machine/Personalization/meeting-notes-prompt.md`
- `Machine/Personalization/content-prompt.md`

`/today` should read `Machine/Personalization/today-prompt.md` rather than loading multiple preference notes.
`/closeday` should read `Machine/Personalization/closeday-prompt.md` rather than loading multiple preference notes.
`/content` should read `Machine/Personalization/content-prompt.md` (plus `VOICE.md`) rather than loading multiple preference notes.

## Content channels
`/content` supports LinkedIn, blog, webinar, and Substack. Drafts save to `00 Human/90 Content/<Channel>/YYYY-MM-DD - <slug>.md`.

## Note conventions
- Person notes: flat files in `00 Human/50 People/<Name>.md` (no subfolders).
- Company notes: `00 Human/40 Resources/Companies/<Name>.md` (`type: company`).
- Concept/topic notes: `00 Human/40 Resources/Concepts/<Name>.md` (`type: concept`).
- Always create notes from the matching template in `00 Human/80 Templates/`.
- Quote wikilinks in YAML frontmatter: `company: "[[Acme]]"` (an unquoted `[[...]]` breaks YAML).

## Working rules
1. Respect the Human/Machine boundary.
2. Use templates when creating new notes.
3. Log activity into the daily note when a workflow calls for it.
4. Keep file paths vault-relative.
5. Prefer updating compiled personalization files in `Machine/Personalization/` through `/interview` instead of making `/today` or `/closeday` read many separate preference files every run.
6. All AI-generated prose in this vault (any workflow or ad-hoc request: posts, resumes, cover letters, messages, briefs, notes) must follow `VOICE.md`. Read `VOICE.md` before generating written output, then run the output through the `humanizer` skill to remove signs of AI writing before saving or returning it.
7. Optional GPTHuman pass (public /content pieces and resumes/cover letters only, not research briefs): as an early mechanical pass you may run prose through the GPTHuman API via `Machine/Scripts/humanize-text.py` (needs `GPTHUMAN_API_KEY` in env or the gitignored `Machine/Scripts/.secrets`; skip gracefully if missing). GPTHuman is a black-box detection-bypass rewriter, NOT the voice authority: the `VOICE.md` + `humanizer` pass in rule #6 always runs AFTER it and wins any conflict (fix any em dashes / generic phrasing / drift it introduces). For resumes/cover letters, only run the narrative prose (summary, cover-letter paragraphs) through it, never bullets or metric-bearing lines.
8. Daily planning uses a single "Today's Commitment" (one thing to finish today). Do not use "frog" or "ONE Thing" framing anywhere.
