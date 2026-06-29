---
type: workflow
status: active
trigger: /job-apply
last_verified: "2026-06-29"
review_loop: "resume audit must reach >= 80/100 (max 5 passes)"
modes: "standalone (job passed as argument) | tracker (no argument, drives the Kanban board)"
tags: [workflow, job-search, research, application]
---

# Workflow - /job-apply

Turn a job posting into company + hiring-manager + role research, give a clear apply / don't-apply recommendation, and - when chosen - craft a tailored resume, critique it with a recruiter audit until it scores >= 80/100, write an optional cover letter, and finish with an AI-smell and voice pass. The full job description is archived up front so it survives a dead URL, and everything written follows `VOICE.md`.

This workflow runs in one of two modes. **Decide the mode first** (Step 0), then run the matching flow. Both flows reuse the shared phases (Context, Research, Apply) defined below.

## Step 0 - Pick the mode
Look at `$ARGUMENTS`:
- **It contains a job URL or pasted job description -> Standalone mode.** Run the **Standalone flow** on that single job. Ignore the tracker.
- **It is empty -> Tracker mode.** Run the **Tracker flow**, which drives `00 Human/30 Projects/Job Search/Tracker.md`.

---

## Shared phase: Context
Read these so the research, recommendation, and writing reflect the user's actual situation, goals, and voice:
- `Machine/Personalization/operator-profile.md` (current role, 30-day goals, target areas)
- `00 Human/70 Context/business-profile.md` (background, strengths)
- `VOICE.md` (vault root) - **the authoritative voice for everything written in this workflow**. Treat its rules as hard constraints (no em dashes, ever; don't start sentences with "and"; short, punchy sentences). If missing, fall back to `00 Human/70 Context/writing-style.md`.
- `00 Human/30 Projects/Job Search/Job Search.md` (active pipeline and goal)

## Shared phase: Research (the research half)
Given a job (a URL or pasted description):
1. **Get the job text.** If it is a URL, use WebFetch to retrieve the posting and extract the full description; keep the complete raw text and the source URL. If it is pasted text, use it directly. If nothing usable is available, say so and stop for this job.
2. **Identify the role and company.** Extract company name, role title, location / remote policy, seniority, compensation (if listed), and the key requirements and responsibilities. Determine the canonical company name for the folder.
3. **Create the company folder and archive the JD.** Create `00 Human/30 Projects/Job Search/Applications/[Company Name]/`. Save the full, unedited posting (source URL + fetch date at the top, then the verbatim text) as `00 Human/30 Projects/Job Search/Applications/[Company Name]/[Company Name] - Job Description.md`. Do not summarize - this is the archival copy.
4. **Research the company.** Use WebSearch / WebFetch: what they do, size, stage / funding, products, business model, tech stack, recent news, culture and values, Glassdoor / reputation, green and red flags. Create from `Machine/Templates/Job Company Research.md` and save as `.../[Company Name]/Company Research.md`.
5. **Research the hiring manager.** Identify the most likely hiring manager, team lead, or recruiter from the posting, company site, and LinkedIn. Capture name, title, background, what they likely care about, mutual connections, and talking points. If unconfirmed, say so and list best guesses plus how to find the right contact. Create from `Machine/Templates/Job Hiring Manager Research.md` and save as `.../[Company Name]/Hiring Manager Research.md`.
6. **Summarize the role and recommend.** Map requirements against the user's experience and 30-day goals. Give a clear, honest **APPLY** or **DON'T APPLY** recommendation with reasoning (fit, compensation, growth, alignment to the goal of a signed offer by 2026-07-29). Create from `Machine/Templates/Job Role Summary.md` and save as `.../[Company Name]/Role Summary.md`.

## Shared phase: Apply (the apply half)
Only run once the decision to apply has been made (standalone: the user says yes; tracker: the card is in the **Apply** column). For company `[Company Name]`:
1. **Craft the resume.** Read the user's resumes from `00 Human/30 Projects/Job Search/Resumes/` (most recent as base, older ones for detail). If none exist, ask the user to add resumes there and stop. Tailor to this role: lead with the most relevant experience, mirror the posting's language, quantify impact. Write every line in the user's voice per `VOICE.md` (no em dashes, ever; no sentences starting with "and"; short, punchy). Save the content as a YAML data file matching the template schema (`target_title`, `target_subtitle`, `summary`, `achievements[]` with `label`/`text`, `competencies[]`, `experience[]` with `company`/`location`/`dates`/`role`/`summary`/`bullets[]`) at `.../[Company Name]/[Company Name] - Resume.yaml`. Generate the styled `.docx` (the template owns all layout/styling):
   `Machine/Scripts/resume-fill.py "00 Human/30 Projects/Job Search/Applications/[Company Name]/[Company Name] - Resume.yaml" "00 Human/30 Projects/Job Search/Applications/[Company Name]/chris-monnat-resume([company-slug]).docx"`
   If `docxtpl`/`pyyaml` are missing, tell the user to run `pip3 install --user docxtpl pyyaml` once, then re-run.
2. **Recruiter-audit loop (must reach >= 80/100).** Adopt the recruiter persona below and audit the current resume against the target JD. Loop:
   1. Run the full audit on the latest resume version.
   2. Read out the Phase 2 score.
   3. If the score is **>= 80/100**, stop looping.
   4. If **< 80/100**: apply the Phase 3 surgical rewrites (X-Y-Z) to the weakest bullets in the YAML, fold in the Phase 4 missing ATS keywords **where they are truthful for the candidate**, address the Phase 2 gaps by surfacing real experience the candidate already has (**never fabricate**), regenerate the `.docx`, and re-audit.
   5. **Safety cap:** at most 5 passes. If still < 80, keep the highest-scoring version and tell the user the score plus the specific gaps blocking 80 (usually a genuine experience gap that can't be honestly written around).
   Save the audit from `Machine/Templates/Job Resume Review.md` as `.../[Company Name]/[Company Name] - Resume Review.md`. Record every pass and score in the iteration log; set the `score`, `passed`, and `passes` frontmatter.
3. **Optional cover letter.** Ask whether the user wants one (in tracker mode, a card tagged `#cover` means yes and `#no-cover` means no, no prompt needed). If yes, write it in the user's voice per `VOICE.md`, addressed to the hiring manager from the Research phase when known, connecting their experience to the role and company. Save from `Machine/Templates/Job Cover Letter.md` as `.../[Company Name]/[Company Name] - Cover Letter.md`.
4. **Final AI-smell and voice pass (remediate in place).** Re-read `VOICE.md`. Review the resume YAML and the cover letter (if present) for: VOICE.md violations (especially em dashes - replace every `—`/`–`; banned phrases; no "and"-starts), AI smell (generic buzzwords like "passionate visionary," "leverages synergy," "cutting-edge," "spearheaded," "results-driven," "seamlessly," "robust," "dynamic"; uniform bullet length; repeated openers; tidy rule-of-three lists), and robotic cadence (vary sentence/bullet length). Remediate directly in the source files; if the YAML changed, regenerate the `.docx`. Append a short "Final polish" note to the Resume Review listing what changed. Do not re-score - this pass is about human authenticity.

### Recruiter-audit rubric (use verbatim each pass)
> **SYSTEM ROLE:** You are an elite Tech Recruiter and Hiring Manager with 15 years of experience at Tier-1 firms. You specialize in the "6-Second Scan" - the initial audit that determines if a candidate moves to the "Yes" pile or the "No" pile.
>
> **INPUT DATA:** 1. [RESUME]: the tailored resume. 2. [TARGET JD]: the job description.
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

---

## Standalone flow (argument provided)
1. Run **Context**.
2. Run **Research** on the job in `$ARGUMENTS`.
3. Show the user the recommendation and headline reasons, then ask directly: **"Do you want to apply to this role?"** Wait for the answer.
4. If yes, run **Apply**.
5. Run **Wrap-up**.

## Tracker flow (no argument)
1. Run **Context**.
2. Read the board at `00 Human/30 Projects/Job Search/Tracker.md`. Columns are `## Research`, `## Pending`, `## Apply`, `## Done` (see **Kanban card mechanics**).
3. **Process every card in `## Research`:**
   - Pull the job from the card text (a URL, or a pasted JD). If the card has no URL or JD, leave it in place and note it in the report; do not guess.
   - Run the **Research** phase.
   - Rewrite the card so it carries the company and the verdict, e.g. `[[<Company> - Role Summary]] — APPLY` (or `DON'T APPLY`), keeping the original URL.
   - **Move the card from `## Research` to `## Pending`.**
4. **Process every card in `## Apply`:**
   - Resolve `[Company Name]` from the card (the link / company text written during research) and its folder under `00 Human/30 Projects/Job Search/Applications/[Company Name]/`. If the folder or research is missing, note it and skip.
   - Run the **Apply** phase.
   - Update the card with the final resume review score and a link to the generated `.docx`.
   - **Move the card from `## Apply` to `## Done`.**
5. **Leave `## Pending` and `## Done` cards untouched.** `Pending` is the human decision gate (the user moves a card to `Apply` to greenlight resume generation); `Done` is complete.
6. Run **Wrap-up**.
7. If both `## Research` and `## Apply` are empty, tell the user there is nothing actionable on the board and stop.

## Shared phase: Wrap-up
1. **Update the Job Search project.** In `00 Human/30 Projects/Job Search/Job Search.md`: add/move the company under `## Pipeline` (to `Applied:` when a resume was generated, else note it researched). Add a dated `## Log` entry noting the company, recommendation, materials drafted, and final resume review score.
2. **Log it.** Append a timestamped entry to today's daily note Activity Log: companies handled, recommendations, files created, and scores.
3. **Report back.** Tell the user what was created (vault-relative paths), the recommendations, the final scores, which cards moved and where, and the suggested next step.

## Kanban card mechanics
`Tracker.md` is an Obsidian Kanban file. Columns are `## <Name>` headings; cards are `- ` list items under a heading. To **move a card**, delete its line from under the source heading and add it under the target heading, preserving every other line including the trailing `%% kanban:settings ... %%` block. Keep card checkboxes/markers intact. Edit the file with the Edit tool (exact-string replacement), not by rewriting the whole file, to avoid disturbing the settings block.

## Error Handling
| Failure Point | Recovery |
|--------------|----------|
| URL won't fetch | Ask the user to paste the description text (still archive it in the Research phase) |
| Company / hiring manager not findable | State the gap explicitly; provide best guesses and how to verify |
| No resume on file | Ask the user to add resumes to `00 Human/30 Projects/Job Search/Resumes/` |
| `VOICE.md` missing | Fall back to `00 Human/70 Context/writing-style.md` and tell the user to create `VOICE.md` |
| Tracker card has no URL/JD (Research) | Leave the card in place and report it; do not guess the job |
| Tracker card has no research folder (Apply) | Leave the card in place and report it; the research half must run first |

## Related
- Project - [[Job Search]]
- Board - [[Tracker]]
- Command - `/job-apply`
