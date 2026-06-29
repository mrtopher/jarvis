---
type: workflow
status: active
trigger: /today
last_verified: "2026-05-01"
tags: [workflow, planning, daily]
---

# Workflow - /today

Morning planning workflow. Build today's plan using live vault state plus the compiled personalization file.

## Step 1 - Get today's date
Use `YYYY-MM-DD`.

## Step 2 - Sync the vault from git
Pull the latest so the day starts from current state across devices.
- Run: `git pull --rebase`
- If there is nothing to pull, it is a no-op. Continue.
- If the pull fails (no remote, offline, or conflicts), do not block the workflow. Note in the plan that the git sync was skipped and continue with the local vault state.

## Step 3 - Read compiled today prompt
Read `Machine/Personalization/today-prompt.md` first.
This is the only personalization file `/today` should need by default.

## Step 4 - Check or create today's note
Look for `00 Human/10 Daily Notes/YYYY-MM-DD.md`.
- If it exists, read it.
- If not, create it from `00 Human/80 Templates/Daily Template.md`.

## Step 5 - Read recent execution state
Read the last 3 daily notes before today and pull forward:
- unchecked tasks
- unchecked frogs
- blockers worth carrying

## Step 6 - Read open work
Read:
- pending task files in `00 Human/20 Tasks/`
- active project notes in `00 Human/30 Projects/`

## Step 7 - Pull today's Google Calendar
Import real commitments so the plan and time blocks fit the actual day.
- Run: `gcalcli --nocolor --calendar "chris@duallogic.ai" agenda today tomorrow --tsv --details location`
  (`--nocolor` and `--calendar` must come before `agenda`. Scoping to chris@duallogic.ai returns only Chris's own meetings: no other calendars, no holidays, no cross-calendar duplicates. `--tsv` gives clean columns: start_date, start_time, end_date, end_time, title, location.)
- Keep only rows where `start_date` equals today's date (Step 1). The range can return tomorrow's rows too.
- The TSV times are 24-hour. Convert every time to 12-hour format with AM/PM when presenting and writing (e.g. `14:30` -> `2:30 PM`, `12:00` -> `12:00 PM`, `06:30` -> `6:30 AM`). No leading zero on the hour.
- Treat timed events as fixed commitments and anchor the day around them. All-day rows with no `start_time` (e.g. "Home") are context, not commitments.
- If the command fails (gcalcli not installed or not authenticated), skip it. Do not block the workflow. Note in the plan that calendar import was unavailable.
- One-time setup is documented in `System/Setup Guide.md` (Google Calendar import).

## Step 8 - Build the plan
Use the compiled today prompt plus the real vault state to determine:
- The ONE Thing
- Top priorities
- Frogs
- Today's tasks
- Quick wins
- Time blocks if the compiled prompt says to use them, scheduled around the calendar events from Step 7
- Watch-outs or drift warnings

## Step 9 - Present the plan
Use this format:

```
## Today's Plan - [Day, Date]

### The ONE Thing
> ...

### Top Priorities
1. ...
2. ...
3. ...

### Frogs to Eat
- [ ] ...

### Today's Tasks
- [ ] ...

### Quick Wins
- [ ] ...

### Watch Out
- ...

### Time Blocks
| Time | Block | Why |
|------|-------|-----|
```

## Step 10 - Write to today's note
After presenting the plan, ask whether to write it into today's note.
If yes, update:
- `## 🎯 Today's Focus`
- `## 🐸 Frogs to Eat`
- `## ✅ Today's Tasks`
- `## ⚡ Quick Wins`
- `## 📅 Calendar` with the imported Google Calendar events (Step 7) plus any time blocks created

Append to Activity Log:
`- [HH:MM] /today - plan written.`
