---
type: workflow-worksheet
status: draft
client:
process_owner:
prepared_by:
date: "{{date:YYYY-MM-DD}}"
tags: [power-automate, workflow, discovery]
---

# Workflow Worksheet - {{title}}

> Plain-language planning sheet. Fill this out **with the business owner before any development**. One worksheet per workflow. If a section doesn't apply, write "N/A" — don't leave it blank.

---

## 1. Snapshot
| Field | Answer |
|-------|--------|
| Workflow name | |
| Process owner (business) | |
| Department / team | |
| Prepared by | |
| Date | |
| Priority (High / Med / Low) | |

---

## 2. Why are we automating this?
> The pain we're solving. Be concrete.

- What's happening today that's slow, error-prone, or annoying?
- How often does this run? (e.g. 10x/day, weekly, per new hire)
- Roughly how much time does it take manually each time?
- What goes wrong when it's done by hand? (missed steps, delays, errors)

## 3. What does "done right" look like?
> Success criteria. How will we know the automation worked?

- [ ]
- [ ]
- [ ]

---

## 4. How it works today (the "as-is")
> Walk through the current manual steps in order. Don't skip the obvious ones.

1.
2.
3.
4.

---

## 5. The trigger — what kicks this off?
> Every workflow starts with ONE thing. Check the closest match and describe it.

- [ ] On a schedule (e.g. every morning at 8am, 1st of the month)
- [ ] Someone submits a form (which form? _______________)
- [ ] An email arrives (to which inbox? matching what? _______________)
- [ ] A file is added or changed (where? _______________)
- [ ] A record is created or updated (in which system? _______________)
- [ ] A person clicks a button / manually starts it
- [ ] Something happens in another system (which? _______________)
- [ ] Other: _______________________________________________

**Describe the trigger in one sentence:**
>

---

## 6. The steps — what should happen, in order (the "to-be")
> Number the steps the automation will perform. One action per row. Keep it in plain English.

| # | What happens | Who / what does it | System involved |
|---|--------------|--------------------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 7. Decisions & branches
> Anywhere the path splits. Write these as "If ___, then ___, otherwise ___."

| If this is true... | ...then do this | ...otherwise do this |
|--------------------|-----------------|----------------------|
| | | |
| | | |

---

## 8. People & approvals
> Who needs to act, approve, or be kept in the loop.

| Person / role | What they do | Approve? | How they're notified (email / Teams / etc.) |
|---------------|--------------|----------|---------------------------------------------|
| | | | |
| | | | |

- What happens if an approver doesn't respond? (reminder after ___ / auto-approve / escalate to ___)

---

## 9. Systems & data
> The apps this touches and the information that moves between them.

**Systems / apps involved (connectors):**
- [ ] SharePoint / OneDrive
- [ ] Outlook / Exchange
- [ ] Teams
- [ ] Excel
- [ ] Forms
- [ ] Dataverse
- [ ] SQL / database
- [ ] Third-party: _______________
- [ ] Other: _______________

**Key data / fields that move through the workflow:**

| Field / piece of info | Where it comes from | Where it goes |
|-----------------------|---------------------|---------------|
| | | |
| | | |

---

## 10. Outputs & notifications
> What the workflow produces and who hears about it.

- What gets created, updated, sent, or filed at the end?
- Who gets notified on success? How?
- Where does the result live? (folder, list, record, inbox)

---

## 11. Exceptions & edge cases
> What could go wrong, and what should happen when it does. **This is where flows break — don't skip it.**

| What could go wrong | What should happen instead |
|---------------------|----------------------------|
| Missing / bad data | |
| A system is down or times out | |
| Duplicate entry | |
| Approver is out of office | |
| | |

- Who should be alerted if the whole workflow fails?

---

## 12. Business rules & assumptions
> Constraints, policies, and things we're taking as given.

-
-

## 13. Out of scope
> What this workflow will NOT do (protects against scope creep).

-
-

---

## 14. Open questions / decisions needed
> Anything unresolved that blocks the build.

- [ ]
- [ ]

---

## 15. Sign-off
| Role | Name | Date | Approved |
|------|------|------|----------|
| Process owner | | | ☐ |
| Solution developer | | | ☐ |

---

## 16. Developer handoff notes
> Filled in by the builder after the session — technical translation, not for the client.

- Suggested trigger type:
- Connectors required:
- Environment / licensing considerations:
- Estimated complexity (S / M / L):
