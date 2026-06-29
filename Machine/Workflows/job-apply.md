---
type: workflow
status: active
trigger: /job-apply
last_verified: "2026-06-29"
tags: [workflow, job-search, research, application]
---

# Workflow - /job-apply

Turn a job posting (URL or pasted description) into company + hiring-manager + role research, give a clear apply / don't-apply recommendation, and - if the user chooses to apply - craft a tailored resume and optional cover letter.

## Step 1 - Read context
Read these so the research and recommendation reflect the user's actual situation, goals, and voice:
- `Machine/Personalization/operator-profile.md` (current role, 30-day goals, target areas)
- `00 Human/70 Context/business-profile.md` (background, strengths)
- `00 Human/70 Context/writing-style.md` (voice for the cover letter)
- `00 Human/30 Projects/Job Search/Job Search.md` (active pipeline and goal)

## Step 2 - Get the job input
The input is in `$ARGUMENTS`.
- If it is a URL, use WebFetch to retrieve the posting and extract the full description.
- If it is pasted text, use it directly.
- If nothing usable was provided, ask the user to paste the job description or a link, then stop until they do.

## Step 3 - Identify the role and company
From the posting, extract: company name, role title, location / remote policy, seniority, compensation (if listed), and the key requirements and responsibilities. Determine the canonical company name to use for the folder.

## Step 4 - Create the company folder
Create `00 Human/30 Projects/Job Search/[Company Name]/`. All research and application files for this job live here.

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
- Write the tailored content as a YAML data file matching the template schema (`target_title`, `target_subtitle`, `summary`, `achievements[]` with `label`/`text`, `competencies[]`, `experience[]` with `company`/`location`/`dates`/`role`/`summary`/`bullets[]`). Save as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Resume.yaml`
- Generate the styled `.docx` by pouring that YAML into the house template (`Machine/Templates/resume-reference.docx`), which owns all layout and styling:
`Machine/Scripts/resume-fill.py "00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Resume.yaml" "00 Human/30 Projects/Job Search/[Company Name]/chris-monnat-resume([company-slug]).docx"`
- If `docxtpl`/`pyyaml` are missing, tell the user to run `pip3 install --user docxtpl pyyaml` once, then re-run.

## Step 10 - Optional cover letter
Ask whether the user wants a cover letter. If yes, write it in their voice (per `writing-style.md`), addressed to the hiring manager from Step 6 when known, connecting their experience to the role and company. Save from `Machine/Templates/Job Cover Letter.md` as:
`00 Human/30 Projects/Job Search/[Company Name]/[Company Name] - Cover Letter.md`

## Step 11 - Update the Job Search project
In `00 Human/30 Projects/Job Search/Job Search.md`:
- Add the company under `## Pipeline` (move it to `Applied:` if the user applied, otherwise note it as researched).
- Add a dated entry to the `## Log` noting the company, the recommendation, and whether materials were drafted.

## Step 12 - Log it
Append a timestamped entry to today's daily note Activity Log summarizing: company researched, recommendation, and which application files were created.

## Step 13 - Report back
Tell the user what was created (with vault-relative paths), the recommendation, and the suggested next step.

## Error Handling
| Failure Point | Recovery |
|--------------|----------|
| URL won't fetch | Ask the user to paste the description text |
| Company / hiring manager not findable | State the gap explicitly; provide best guesses and how to verify |
| No resume on file | Ask the user to add resumes to `00 Human/30 Projects/Job Search/Resumes/` |

## Related
- Project - [[Job Search]]
- Command - `/job-apply`
