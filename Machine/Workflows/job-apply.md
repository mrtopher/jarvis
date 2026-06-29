---
type: workflow
status: active
trigger: /job-apply
last_verified: "2026-06-29"
review_loop: "resume audit must reach >= 80/100 (max 5 passes)"
tags: [workflow, job-search, research, application]
---

# Workflow - /job-apply

Turn a job posting (URL or pasted description) into company + hiring-manager + role research, give a clear apply / don't-apply recommendation, and - if the user chooses to apply - craft a tailored resume, critique it with a recruiter audit until it scores >= 80/100, write an optional cover letter, and finish with an AI-smell and voice pass. The full job description is archived up front so it survives a dead URL, and everything written follows `VOICE.md`.

## Step 1 - Read context
Read these so the research and recommendation reflect the user's actual situation, goals, and voice:
- `Machine/Personalization/operator-profile.md` (current role, 30-day goals, target areas)
- `00 Human/70 Context/business-profile.md` (background, strengths)
- `VOICE.md` (vault root) — **the authoritative voice for everything written in this workflow** (resume wording, cover letter, summaries). Treat its rules as hard constraints (e.g. no em dashes, ever; don't start sentences with "and"; short, punchy sentences). If `VOICE.md` is missing, fall back to `00 Human/70 Context/writing-style.md`.
- `00 Human/30 Projects/Job Search/Job Search.md` (active pipeline and goal)

## Step 2 - Get the job input
The input is in `$ARGUMENTS`.
- If it is a URL, use WebFetch to retrieve the posting and extract the full description. Keep the complete raw text and the source URL - they get archived in Step 4.
- If it is pasted text, use it directly and keep the full text for archiving.
- If nothing usable was provided, ask the user to paste the job description or a link, then stop until they do.

## Step 3 - Identify the role and company
From the posting, extract: company name, role title, location / remote policy, seniority, compensation (if listed), and the key requirements and responsibilities. Determine the canonical company name to use for the folder.

## Step 4 - Create the company folder and archive the full JD
Create `00 Human/30 Projects/Job Search/[Company Name]/`. All research and application files for this job live here.

Immediately archive the full, unedited job description so it survives if the URL later dies or changes. Save the complete raw text from Step 2 as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Job Description.md`
At the top of that file, record the source URL and the fetch date, then paste the full posting verbatim (do not summarize - the Role Summary in Step 7 is the summary; this file is the archival copy).

## Step 5 - Research the company
Use WebSearch / WebFetch. Investigate: what they do, size, stage / funding, products, business model, tech stack, recent news, culture and values, Glassdoor / employee reputation, and any green flags or red flags. Create the file from `Machine/Templates/Job Company Research.md` and save as:
`00 Human/30 Projects/Job Search/[Company Name]/Company Research.md`

## Step 6 - Research the hiring manager
Identify the most likely hiring manager, team lead, or recruiter from the posting, the company site, and LinkedIn. Capture: name, title, background, what they likely care about, mutual connections or shared interests, and concrete talking points. If the person cannot be confirmed, say so explicitly and list best guesses plus how to find the right contact. Create the file from `Machine/Templates/Job Hiring Manager Research.md` and save as:
`00 Human/30 Projects/Job Search/[Company Name]/Hiring Manager Research.md`

## Step 7 - Summarize the role and recommend
Map the role's requirements against the user's experience and 30-day goals. Give a clear, honest **APPLY** or **DON'T APPLY** recommendation with reasoning (fit, compensation signals, growth, alignment to the goal of a signed offer by 2026-07-29). Create the file from `Machine/Templates/Job Role Summary.md` and save as:
`00 Human/30 Projects/Job Search/[Company Name]/Role Summary.md`

## Step 8 - Present and ask
Show the user the recommendation and the headline reasons. Then ask directly: **"Do you want to apply to this role?"** Wait for their answer.

## Step 9 - If applying, craft the resume
Only run this step if the user chooses to apply.
- Read the user's resumes from `00 Human/30 Projects/Job Search/Resumes/`. Use the most recent file (by date in the name or frontmatter) as the base, and pull supporting detail from older ones.
- If that folder has no resume, ask the user to add their current and most recent resume there, then stop until they do.
- Tailor the content to this role: reorder and reword to lead with the most relevant experience, mirror the posting's language, and quantify impact.
- Write every line in the user's voice per `VOICE.md` - obey its hard rules (no em dashes, ever; don't start sentences with "and"; short, punchy sentences; avoid the phrases it bans).
- Write the tailored content as a YAML data file matching the template schema (`target_title`, `target_subtitle`, `summary`, `achievements[]` with `label`/`text`, `competencies[]`, `experience[]` with `company`/`location`/`dates`/`role`/`summary`/`bullets[]`). Save as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Resume.yaml`
- Generate the styled `.docx` by pouring that YAML into the house template (`Machine/Templates/resume-reference.docx`), which owns all layout and styling:
`Machine/Scripts/resume-fill.py "00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Resume.yaml" "00 Human/30 Projects/Job Search/[Company Name]/chris-monnat-resume([company-slug]).docx"`
- If `docxtpl`/`pyyaml` are missing, tell the user to run `pip3 install --user docxtpl pyyaml` once, then re-run.

## Step 10 - Critically review the resume and iterate until it scores >= 80/100
Only run this step if a resume was created in Step 9. Adopt the recruiter persona below and audit the **current** resume against the target JD. The audit produces a 0-100 impact-visibility score (Phase 2).

Run this as a loop:
1. Run the full audit (prompt below) on the latest resume version.
2. Read out the Phase 2 score.
3. **If the score is >= 80/100**, stop looping — the resume passes.
4. **If the score is < 80/100**, improve the resume and re-audit:
   - Apply the Phase 3 surgical rewrites (X-Y-Z formula) to the weakest bullets in the YAML.
   - Fold in the Phase 4 missing ATS keywords where they are truthful for the candidate.
   - Address the Phase 2 gaps by surfacing real, relevant experience the candidate already has (never fabricate).
   - Regenerate the `.docx` with `Machine/Scripts/resume-fill.py` (same command as Step 9).
   - Go back to sub-step 1.
5. **Safety cap:** run at most 5 passes. If the score is still < 80 after 5 passes, stop, keep the highest-scoring version, and tell the user the score plus the specific gaps that are blocking 80 (usually a genuine experience gap that can't be honestly written around).

Save the final audit from `Machine/Templates/Job Resume Review.md` as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Resume Review.md`
Record every pass and its score in the audit's iteration log, and set the `score`, `passed`, and `passes` frontmatter fields.

Use this exact audit rubric each pass:

> **SYSTEM ROLE:** You are an elite Tech Recruiter and Hiring Manager with 15 years of experience at Tier-1 firms. You specialize in the "6-Second Scan" - the initial audit that determines if a candidate moves to the "Yes" pile or the "No" pile.
>
> **INPUT DATA:** 1. [RESUME]: the tailored resume just created. 2. [TARGET JD]: the job description from Step 2/3.
>
> **MISSION:** Conduct a brutal, high-fidelity audit of the [RESUME] against the [TARGET JD]. Do not be polite. Be effective.
>
> **PHASE 1 - THE RECRUITER'S SCAN (6 SECONDS):** Tell me exactly where my eyes "stumble" or lose interest. Identify the "Weakest Signal" - the one bullet point or section that makes me doubt the candidate's seniority or fit. Flag any "AI Smell" - generic buzzwords that add zero value.
>
> **PHASE 2 - THE GAP ANALYSIS:** What are the 3 critical skills/outcomes in the [TARGET JD] that are totally missing or underrepresented in the [RESUME]? Then, on a scale of 1-100, how "visible" is the candidate's impact for this specific role? (This number is the loop's score.)
>
> **PHASE 3 - THE SURGICAL REWRITE:** Select the 3 weakest bullet points and rewrite them using the X-Y-Z Formula ("Accomplished [X] as measured by [Y], by doing [Z]"). STYLING: maintain a human, professional, confident tone. Avoid flowery language like "passionate visionary" or "leverages synergy."
>
> **PHASE 4 - KEYWORD OPTIMIZATION:** List the top 5 keywords the ATS will look for in this JD that are currently missing from the resume.
>
> **PHASE 5 - FINAL VERDICT:** Give a one-sentence "Pitch" for this candidate that I can tell the VP of Engineering.

## Step 11 - Optional cover letter
Ask whether the user wants a cover letter. If yes, write it in their voice per `VOICE.md` (obey its hard rules - no em dashes, ever; no sentences starting with "and"; short, punchy sentences), addressed to the hiring manager from Step 6 when known, connecting their experience to the role and company. Save from `Machine/Templates/Job Cover Letter.md` as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Cover Letter.md`

## Step 12 - Final AI-smell and voice pass (remediate in place)
Run this last, after the resume and (if created) the cover letter exist, so it polishes everything that will actually be sent. Re-read `VOICE.md` first.

Critically review the resume (`[Company Name] - Resume.yaml`) and the cover letter (if present) for:
- **VOICE.md violations** - especially the hard rules (no em dashes, ever; no sentence starting with "and"; banned phrases). The em-dash check is non-negotiable: replace every `—` and `–` with a period, comma, or rephrase.
- **AI smell** - generic buzzwords and filler that add no evidence ("passionate visionary," "leverages synergy," "cutting-edge," "spearheaded," "results-driven," "seamlessly," "robust," "dynamic"), hollow intensifiers, and tells like uniform bullet length, repeated sentence openers, and tidy rule-of-three lists.
- **Robotic cadence** - vary sentence and bullet length so it reads like a person, matching the rhythm `VOICE.md` describes.

Remediate every issue directly in the source files (the YAML and the cover letter markdown). If the YAML changed, regenerate the `.docx` with `Machine/Scripts/resume-fill.py` (same command as Step 9). Then append a short "Final polish" note to `[Company Name] - Resume Review.md` listing what was changed (e.g. "removed 14 em dashes, cut 'leverages synergy,' varied bullet length"). Do not re-score - this pass is about human authenticity, not the recruiter rubric.

## Step 13 - Update the Job Search project
In `00 Human/30 Projects/Job Search/Job Search.md`:
- Add the company under `## Pipeline` (move it to `Applied:` if the user applied, otherwise note it as researched).
- Add a dated entry to the `## Log` noting the company, the recommendation, whether materials were drafted, and the final resume review score.

## Step 14 - Log it
Append a timestamped entry to today's daily note Activity Log summarizing: company researched, recommendation, which application files were created, and the final resume review score.

## Step 15 - Report back
Tell the user what was created (with vault-relative paths), the recommendation, the final resume review score, and the suggested next step.

## Error Handling
| Failure Point | Recovery |
|--------------|----------|
| URL won't fetch | Ask the user to paste the description text (still archive it in Step 4) |
| Company / hiring manager not findable | State the gap explicitly; provide best guesses and how to verify |
| No resume on file | Ask the user to add resumes to `00 Human/30 Projects/Job Search/Resumes/` |
| `VOICE.md` missing | Fall back to `00 Human/70 Context/writing-style.md` and tell the user to create `VOICE.md` |

## Related
- Project - [[Job Search]]
- Command - `/job-apply`
