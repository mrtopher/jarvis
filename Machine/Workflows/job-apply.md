---
type: workflow
status: active
trigger: /job-apply
last_verified: "2026-07-06"
review_loop: "resume audit must reach >= 90/100 (max 5 passes)"
modes: "standalone (job passed as argument) | tracker (no argument, drives the Kanban board)"
tags: [workflow, job-search, research, application]
---

# Workflow - /job-apply

Turn a job posting into company + hiring-manager + role research, give a clear apply / don't-apply recommendation, and - when chosen - craft a tailored resume, critique it with a recruiter audit until it scores >= 90/100, write an optional cover letter, run an accuracy and honesty pass, and finish with an AI-smell and voice pass. The full job description is archived up front so it survives a dead URL, and everything written follows `VOICE.md`.

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
- `00 Human/30 Projects/Job Search/Skills.md` - **the authoritative list of the candidate's skills** (grouped, deduplicated). Resume `competencies[]` must be drawn only from this file. If missing, fall back to skills evidenced in the resumes under `00 Human/30 Projects/Job Search/Resumes/`.

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
1. **Craft the resume.** Read the user's resumes from `00 Human/30 Projects/Job Search/Resumes/` (most recent as base, older ones for detail). If none exist, ask the user to add resumes there and stop. Tailor to this role: lead with the most relevant experience, mirror the posting's language in the bullets and competencies, quantify impact. Write every line in the user's voice per `VOICE.md` (no em dashes, ever; no sentences starting with "and"; short, punchy). **The `summary` field is an easy-read introduction, not a keyword list.** Model its voice on the summaries in `00 Human/30 Projects/Job Search/Resumes/`: open with a punchy identity line, weave two or three quantified wins into flowing prose, name one marquee achievement (e.g. the Pipeline 360 platform), and close with a "Known for..." line tying the work to business outcomes. Never scrape or list JD keywords in the summary (no "Deep on X, Y, Z" tech piles) - ATS/keyword matching belongs in `competencies[]` and the experience bullets. **Hard length cap: 3 to 4 sentences, 75 words maximum (aim for ~60). The summary paragraph consistently overflows, so keep it tight; `resume-fill.py` prints a LENGTH WARNING when it runs over. If it exceeds 75 words, cut the weakest clause rather than reflowing.** **`achievements[]` renders as the shaded "Signature Achievements" box, each as `label: text`. Supply four entries. The `label` is a short bold tag (two to four words, no ending punctuation). The `text` is one or two flowing sentences that must NOT contain a colon - the template already prints the `label:` colon, so a colon in `text` produces an ugly double-colon line. Pick the four strongest, most role-relevant wins from the resume, lead each with a quantified outcome, and do not restate the `label` verbatim at the start of the `text`.** **Build `competencies[]` only from `00 Human/30 Projects/Job Search/Skills.md`:** select the entries that best match the JD (prefer the categories nearest the role's seniority), keep the wording as it appears there, and never invent a competency the candidate does not list. **`competencies[]` renders as a three-column "Signature Strengths & Competencies" grid: supply exactly 15 items (5 per column). Every item must be a high-level, strategic skill and short enough to sit on one line - no specific technologies, tools, platforms, or languages (no "AWS," "Kubernetes," "PostgreSQL," "Python"); those signals live in the experience bullets. Keep each entry concise (roughly under 26 characters) so it never wraps.** If the JD calls for a skill that is genuinely absent from `Skills.md`, do not add it - flag the gap in the Resume Review instead. **Also build `skill_groups[]` for the ATS template (the default): a short, keyword-rich Skills line grouped into four to five categories (five is the hard maximum). Each entry is `label` (the category name, e.g. "Product & Delivery," "Platforms," "AI," "Data," "Security & Compliance") plus `entries` (a comma-separated string of the concrete skills under it). Draw the wording from `00 Human/30 Projects/Job Search/Skills.md`, but unlike `competencies[]` this line SHOULD name specific tools, platforms, and languages (AWS, GCP, PostgreSQL, BigQuery, CI/CD) because ATS keyword-matching rewards them. Reorder the categories so the ones the JD cares about most come first. Do not use the YAML key `items` for the skills - it collides with a Python dict method and renders wrong; the key is `entries`. **Hard length cap: at most 5 categories, and each `entries` string stays under 80 characters so no Skills row wraps long. The Skills section consistently overflows; when a category runs over, cut the weakest keywords or merge categories rather than spilling. `resume-fill.py` prints a LENGTH WARNING per over-budget line.**** `competencies[]`/`target_subtitle` feed the styled template and `skill_groups[]` feeds the ATS template - produce all of them so either template renders from the same YAML. **The `target_subtitle` is the shaded line under the name: set it to exactly three high-level skills from `00 Human/30 Projects/Job Search/Skills.md`, joined with ` | `, chosen to match the role and pulled verbatim from the file. Keep it strategic - no specific tools, platforms, or technical skills (no "Kubernetes," "AWS," "SRE"); those belong in `competencies[]` and the bullets. The three must be thematically distinct: never repeat a leading word (not "Platform Strategy" + "Platform Modernization") and never let two items cover the same theme - each slot should add a new signal.** Save the content as a YAML data file matching the template schema (`target_title`, `target_subtitle`, `summary`, `achievements[]` with `label`/`text`, `competencies[]`, `skill_groups[]` with `label`/`entries`, `experience[]` with `company`/`location`/`dates`/`role`/`summary`/`bullets[]`) at `.../[Company Name]/[Company Name] - Resume.yaml`. Generate the `.docx` (the template owns all layout/styling):
   `Machine/Scripts/resume-fill.py "00 Human/30 Projects/Job Search/Applications/[Company Name]/[Company Name] - Resume.yaml" "00 Human/30 Projects/Job Search/Applications/[Company Name]/chris-monnat-resume([company-slug]).docx"`
   **Template choice.** By default this renders the simple, ATS-friendly template (`Machine/Templates/resume-ats.docx`, single column, categorized Skills line). Use the styled template (shaded boxes + competency grid) ONLY when the user asks for it - standalone: the user says "styled", "fancy", or "non-ats"; tracker: the card is tagged `#styled`. To use it, append `--template "Machine/Templates/resume-reference.docx"` to the command above. The same YAML feeds both, so no content changes are needed to switch.
   If `docxtpl`/`pyyaml` are missing, tell the user to run `pip3 install --user docxtpl pyyaml` once, then re-run.
2. **Recruiter-audit loop (must reach >= 90/100).** Adopt the recruiter persona below and audit the current resume against the target JD. Loop:
   1. Run the full audit on the latest resume version.
   2. Read out the Phase 2 score.
   3. If the score is **>= 90/100**, stop looping.
   4. If **< 90/100**: apply the Phase 3 surgical rewrites (X-Y-Z) to the weakest bullets in the YAML, fold in the Phase 4 missing ATS keywords **only when they appear in `00 Human/30 Projects/Job Search/Skills.md` or are otherwise truthful for the candidate** (never add a competency or keyword the candidate does not actually have), address the Phase 2 gaps by surfacing real experience the candidate already has (**never fabricate**), regenerate the `.docx`, and re-audit.
   5. **Safety cap:** at most 5 passes. If still < 90, keep the highest-scoring version and tell the user the score plus the specific gaps blocking 90 (usually a genuine experience gap that can't be honestly written around).
   Save the audit from `Machine/Templates/Job Resume Review.md` as `.../[Company Name]/[Company Name] - Resume Review.md`. Record every pass and score in the iteration log; set the `score`, `passed`, and `passes` frontmatter.
3. **Optional cover letter.** Ask whether the user wants one (in tracker mode, a card tagged `#cover` means yes and `#no-cover` means no, no prompt needed). If yes, write it in the user's voice per `VOICE.md`, addressed to the hiring manager from the Research phase when known, connecting their experience to the role and company. Save the content as a YAML data file matching the cover-letter schema (`date`, `salutation`, `paragraphs[]` one entry per body paragraph, `closing`, `signer`) at `.../[Company Name]/[Company Name] - Cover Letter.yaml`, then generate the styled `.docx` (the template reuses the resume's name/contact header banner and owns all layout):
   `Machine/Scripts/cover-letter-fill.py "00 Human/30 Projects/Job Search/Applications/[Company Name]/[Company Name] - Cover Letter.yaml" "00 Human/30 Projects/Job Search/Applications/[Company Name]/chris-monnat-cover-letter([company-slug]).docx"`
   If `docxtpl`/`pyyaml` are missing, tell the user to run `pip3 install --user docxtpl pyyaml` once (or use the project venv at `~/.venvs/jarvis`), then re-run.
4. **GPTHuman humanize pass (optional early pass, remediate in place).** As a mechanical first pass on the *narrative prose only*, run the resume `summary` and the cover-letter body through GPTHuman: `~/.venvs/jarvis/bin/python "Machine/Scripts/humanize-text.py" --text "<prose>"`, then paste the returned text back into the YAML field(s). **GPTHuman requires more than 300 characters of input**, so run the cover letter as one block (all `paragraphs[]` joined), not paragraph by paragraph, and split the result back into paragraphs afterward; if the resume `summary` is under ~300 chars the script skips it (that is fine). **Do NOT** run bullets, `competencies[]`, `skill_groups[]`, dates, titles, or any metric-bearing line through it - a black-box rewrite can silently alter numbers and scope. GPTHuman is not the final authority: run it BEFORE the accuracy and voice passes below so both re-check its output (it can reintroduce em dashes, generic phrasing, or drift a claim). Regenerate the affected `.docx` after editing. Needs `GPTHUMAN_API_KEY` (env or the gitignored `Machine/Scripts/.secrets`); if the key is missing or the call fails, **skip gracefully**, keep the current YAML, tell the user why, and continue.
5. **Accuracy and honesty pass (always run, remediate in place).** Before the voice pass, audit every line of the resume YAML (and the cover letter YAML, if present) for factual truth and honest self-representation. This pass is non-negotiable - a resume that scores 90 on impact can still contain a false claim, so run it every time. Flag and fix:
   - **False or misattributed tenure/scope.** A duration or scale attached to the wrong thing (e.g. "20 years building AI-first orgs" when AI-first is recent; "led hundreds of engineers" when the real number is ~40). The number must attach to what it is actually true of. AI-first / agentic work is the candidate's *current* mode, not a 20-year track record.
   - **JD parroting.** Bullets that echo the posting's exact phrasing (e.g. "throughput, quality, and predictability aren't trade-offs") instead of describing the candidate's own work. Rewrite in the candidate's own words; mirroring the JD reads as coached, not credible.
   - **Unfalsifiable self-claims.** Asserted traits like "credible," "respected," "trusted by senior engineers," "world-class." A resume shows these through outcomes; it never asserts them. Cut the claim or replace it with the concrete result that earns it.
   - **Fabricated or unsupported specifics.** Metrics, dates, titles, employers, or technologies not grounded in the source resumes or `Skills.md`. Every number and claim must trace to real experience. Watch for employment-date gaps between roles.
   Cross-check load-bearing facts against `00 Human/30 Projects/Job Search/Resumes/` and `00 Human/30 Projects/Job Search/Skills.md`. When a fact cannot be verified, flag it to the user rather than shipping it. Remediate directly in the source files; if a YAML changed, regenerate the affected `.docx`. Append an "Accuracy pass" note to the Resume Review listing every correction (and any fact flagged for the user to confirm).
6. **Final AI-smell and voice pass (remediate in place).** Re-read `VOICE.md`. Review the resume YAML and the cover letter YAML (if present) for: VOICE.md violations (especially em dashes - replace every `—`/`–`; banned phrases; no "and"-starts), AI smell (generic buzzwords like "passionate visionary," "leverages synergy," "cutting-edge," "spearheaded," "results-driven," "seamlessly," "robust," "dynamic"; uniform bullet length; repeated openers; tidy rule-of-three lists), and robotic cadence (vary sentence/bullet length). Remediate directly in the source files; if a YAML changed, regenerate the affected `.docx` (resume and/or cover letter). Append a short "Final polish" note to the Resume Review listing what changed. Do not re-score - this pass is about human authenticity.

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
