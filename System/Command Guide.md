---
type: guide
status: active
tags: [commands, workflow]
---

# Command Guide

Included commands in this edition:

- `/start`
- `/interview`
- `/today`
- `/new`
- `/closeday`
- `/meeting-notes`
- `/job-apply`
- `/content`

## Core model
- `/start` explains the system and points you to the best next move.
- `/interview` personalizes the vault and rewrites the compiled prompts used by `/today` and `/closeday`.
- `/today` reads the compiled today prompt plus live vault state.
- `/closeday` reads the compiled closeday prompt plus today's note.
- `/new` routes inputs into the right notes.
- `/job-apply` researches a job (company, hiring manager, role), recommends apply / don't apply, and drafts a tailored resume (recruiter-audited to >= 80/100) and optional cover letter. Runs standalone when you pass a job URL or pasted description; with no argument it drives the Job Search Tracker board (Research cards get researched and moved to Pending; cards you move to Apply get a resume generated and move to Done).
- `/content` drafts on-voice content for LinkedIn, the company blog, or a monthly webinar, all in `VOICE.md`. Runs standalone when you pass an idea (e.g. `/content blog: why AI slop is real`); with no argument it drives the content board at `00 Human/90 Content/Pipeline.md` (Ideas cards tagged `#linkedin`/`#blog`/`#webinar` get drafted and moved to Drafting; you own Drafting -> Review -> Scheduled -> Published). Reads `Machine/Personalization/content-prompt.md`, which `/interview` compiles from `00 Human/70 Context/content-preferences.md`.
