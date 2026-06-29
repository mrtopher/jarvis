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

## Core model
- `/start` explains the system and points you to the best next move.
- `/interview` personalizes the vault and rewrites the compiled prompts used by `/today` and `/closeday`.
- `/today` reads the compiled today prompt plus live vault state.
- `/closeday` reads the compiled closeday prompt plus today's note.
- `/new` routes inputs into the right notes.
- `/job-apply` researches a job (company, hiring manager, role), recommends apply / don't apply, and drafts a tailored resume (recruiter-audited to >= 80/100) and optional cover letter. Runs standalone when you pass a job URL or pasted description; with no argument it drives the Job Search Tracker board (Research cards get researched and moved to Pending; cards you move to Apply get a resume generated and move to Done).
