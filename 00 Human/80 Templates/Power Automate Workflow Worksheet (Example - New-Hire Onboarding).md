---
type: workflow-worksheet
status: example
client: Sample Co.
process_owner: Dana Reyes (HR Manager)
prepared_by: Chris (Dual Logic)
date: "2026-07-15"
tags: [power-automate, workflow, discovery, example]
---

# Workflow Worksheet - New-Hire Onboarding (EXAMPLE)

> ⚠️ **This is a completed sample** showing how to fill out the worksheet. Copy the blank template for real workflows.

---

## 1. Snapshot
| Field | Answer |
|-------|--------|
| Workflow name | New-Hire Onboarding Kickoff |
| Process owner (business) | Dana Reyes, HR Manager |
| Department / team | People Ops |
| Prepared by | Chris (Dual Logic) |
| Date | 2026-07-15 |
| Priority (High / Med / Low) | High |

---

## 2. Why are we automating this?
> The pain we're solving. Be concrete.

- What's happening today that's slow, error-prone, or annoying? — HR emails IT, Facilities, and the hiring manager separately for every new hire. Requests get missed and new hires show up without a laptop or accounts.
- How often does this run? — ~6–10 new hires/month, spiky around quarter starts.
- Roughly how much time does it take manually each time? — ~45 min of HR coordination per hire, spread over several days of chasing.
- What goes wrong when it's done by hand? — Missed IT tickets, duplicate requests, no single view of what's done, Day-1 surprises.

## 3. What does "done right" look like?
> Success criteria. How will we know the automation worked?

- [x] One HR form submission kicks off every downstream request automatically.
- [x] IT, Facilities, and the manager each get a clear task within minutes.
- [x] HR can see status of all onboarding items in one list.
- [x] Zero "new hire has no laptop on Day 1" incidents.

---

## 4. How it works today (the "as-is")
> Walk through the current manual steps in order. Don't skip the obvious ones.

1. Recruiter tells HR the candidate accepted.
2. HR emails IT to create accounts (email, Teams, systems).
3. HR emails Facilities for desk + badge.
4. HR emails the hiring manager to prep Day-1 plan.
5. HR manually orders a laptop (or asks IT to).
6. HR follows up over the next few days to confirm each is done.
7. HR sends the new hire a welcome email with start details.

---

## 5. The trigger — what kicks this off?
> Every workflow starts with ONE thing.

- [x] Someone submits a form (which form? **"New Hire Intake" Microsoft Form, filled by HR**)
- [ ] On a schedule
- [ ] An email arrives
- [ ] A file is added or changed
- [ ] A record is created or updated
- [ ] A person clicks a button / manually starts it
- [ ] Something happens in another system
- [ ] Other: __________

**Describe the trigger in one sentence:**
> When HR submits the "New Hire Intake" form, the onboarding workflow starts.

---

## 6. The steps — what should happen, in order (the "to-be")

| # | What happens | Who / what does it | System involved |
|---|--------------|--------------------|-----------------|
| 1 | Capture new-hire details (name, role, manager, start date, equipment needs) | HR (via form) | Microsoft Forms |
| 2 | Create a tracking record for this hire | Automation | SharePoint list "Onboarding" |
| 3 | Send IT a task to create accounts (email, Teams, role-based app access) | Automation → IT | Teams / Planner |
| 4 | Send Facilities a task for desk + badge | Automation → Facilities | Teams / Planner |
| 5 | Notify hiring manager to prepare a Day-1 plan | Automation → Manager | Outlook |
| 6 | If a laptop is needed, request equipment (see branch) | Automation | Approvals + Outlook |
| 7 | Once all tasks are marked done, send the new hire a welcome email | Automation | Outlook |
| 8 | Mark the tracking record "Ready for Day 1" | Automation | SharePoint list |

---

## 7. Decisions & branches
> "If ___, then ___, otherwise ___."

| If this is true... | ...then do this | ...otherwise do this |
|--------------------|-----------------|----------------------|
| Role needs a laptop | Send equipment request for manager approval, then order | Skip equipment step |
| Start date is < 5 business days away | Flag as "Rush" and alert HR + IT lead | Proceed normally |
| Role is a manager-level hire | Also create request for admin/system elevated access | Standard access only |

---

## 8. People & approvals

| Person / role | What they do | Approve? | How they're notified |
|---------------|--------------|----------|----------------------|
| IT technician | Create accounts + app access | No | Teams task |
| Facilities coordinator | Desk + badge | No | Teams task |
| Hiring manager | Prep Day-1 plan; approve laptop spend | Yes (equipment) | Outlook + Approvals |
| HR Manager (Dana) | Owns the process, handles exceptions | No | SharePoint status view |

- What happens if an approver doesn't respond? — Reminder to the manager after 24h; escalate to HR Manager after 48h.

---

## 9. Systems & data

**Systems / apps involved (connectors):**
- [x] SharePoint / OneDrive
- [x] Outlook / Exchange
- [x] Teams
- [x] Forms
- [x] Approvals (Power Automate built-in)
- [ ] Excel
- [ ] Dataverse
- [ ] SQL / database
- [ ] Third-party: __________

**Key data / fields that move through the workflow:**

| Field / piece of info | Where it comes from | Where it goes |
|-----------------------|---------------------|---------------|
| Full name, role, department | Intake form | SharePoint record, all tasks |
| Start date | Intake form | Tasks, rush logic, welcome email |
| Manager name/email | Intake form | Manager notification + approval |
| Equipment needs | Intake form | Equipment branch + approval |

---

## 10. Outputs & notifications

- What gets created, updated, sent, or filed? — A SharePoint onboarding record, IT/Facilities tasks, manager Day-1 notice, equipment order (if approved), and a welcome email.
- Who gets notified on success? — HR Manager gets a "Ready for Day 1" confirmation; new hire gets the welcome email.
- Where does the result live? — SharePoint "Onboarding" list, one row per hire, with status.

---

## 11. Exceptions & edge cases
> **This is where flows break — don't skip it.**

| What could go wrong | What should happen instead |
|---------------------|----------------------------|
| Missing / bad data (no manager email) | Don't start; return the form to HR with what's missing |
| A system is down or times out (IT task fails) | Retry once; if still failing, alert HR Manager directly |
| Duplicate entry (same hire submitted twice) | Detect existing record by name+start date; flag, don't duplicate |
| Approver (manager) out of office | Reminder at 24h, escalate to HR Manager at 48h |
| Start date already passed | Flag as "Late start — review" and alert HR |

- Who should be alerted if the whole workflow fails? — HR Manager (Dana) + the Dual Logic support inbox.

---

## 12. Business rules & assumptions

- Every new hire gets an intake form submitted before Day 1 — no verbal-only starts.
- Equipment spend over standard laptop requires manager approval.
- Elevated/admin access is only granted for manager-level roles.

## 13. Out of scope

- Payroll setup (handled in a separate HR system).
- Benefits enrollment.
- Offboarding (separate future workflow).

---

## 14. Open questions / decisions needed

- [ ] Which SharePoint site should host the Onboarding list?
- [ ] Does IT want tasks in Planner or a ticketing system (ServiceNow)?
- [ ] Standard equipment package — confirm the default laptop/monitor spec.

---

## 15. Sign-off
| Role | Name | Date | Approved |
|------|------|------|----------|
| Process owner | Dana Reyes | | ☐ |
| Solution developer | Chris (Dual Logic) | | ☐ |

---

## 16. Developer handoff notes
> Filled in by the builder after the session.

- Suggested trigger type: **When a new response is submitted** (Microsoft Forms).
- Connectors required: Forms, SharePoint, Outlook, Teams/Planner, Approvals.
- Environment / licensing considerations: Standard connectors only — no premium license needed unless ServiceNow is chosen (premium connector).
- Estimated complexity (S / M / L): **M** — several parallel branches + one approval + retry/error handling.
