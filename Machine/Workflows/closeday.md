---
type: workflow
status: active
trigger: /closeday
last_verified: "2026-07-07"
tags: [workflow, eod, daily]
---

# Workflow - /closeday

End-of-day workflow. Close today's note using the compiled closeday prompt plus the actual state of the day.

## Step 1 - Read compiled closeday prompt
Read `Machine/Personalization/closeday-prompt.md` first.
This is the only personalization file `/closeday` should need by default.

## Step 2 - Read today's daily note
Open `00 Human/10 Daily Notes/YYYY-MM-DD.md`.
If it does not exist, create it from the daily template.

## Step 3 - Find carry-overs
Pull unchecked items from:
- `## 🐸 Frogs to Eat`
- `## ✅ Today's Tasks`
- `## ⚡ Quick Wins`

## Step 3b - Review the inbox
Read `00 Human/00 Inbox/Inbox.md` and count the bullets under `## Unprocessed`.
- If there are none, note "inbox clear" and continue.
- If there are captures, list them and ask whether to triage now. If yes, route each via `/new` (which will remove the bullet as it processes it). Anything left stays in the inbox for tomorrow.

## Step 3c - Import today's meetings from Fireflies
Meetings are transcribed by Fireflies AI (MCP tools namespaced `mcp__claude_ai_Fireflies__*`). Turn any of today's transcripts that match today's meetings into meeting notes automatically.

1. Read the meeting names from today's `## 📅 Calendar` section.
2. Call `fireflies_get_transcripts` filtered to today's date to list what Fireflies captured.
3. Match Fireflies transcripts to the calendar meetings by name (fuzzy — Fireflies titles won't match exactly; a partial/keyword match is fine).
4. For each match with no existing `00 Human/40 Resources/Meetings/YYYY-MM-DD - [name].md`, run the `/meeting-notes` workflow with that Fireflies transcript ID to create the meeting note, tasks, and people updates. Skip anything already imported (this step is idempotent).
5. If a Fireflies transcript has no calendar match, list it and ask whether to import it anyway.
6. If Fireflies is not connected (`! Needs authentication`), skip this step and note it — do not block closeday.

Fold action items from imported meetings into the carry-overs staged in Step 6.

## Step 4 - Ask the end-of-day questions
Ask one question at a time.
Always ask:
1. "What got done today that you're glad about?"
2. "What got in the way or is still stuck?"
3. "One sentence on how today felt overall."

If the compiled closeday prompt says metrics matter, ask only the relevant metric follow-up.

## Step 5 - Update today's note
Fill in `## 🧠 End of Day` and, if relevant, `## 📈 Metrics Snapshot`.
Append to Activity Log:
`- [HH:MM] /closeday - day closed and carry-overs staged.`

## Step 6 - Stage tomorrow
Create tomorrow's note if needed and pre-populate `## ✅ Today's Tasks` with carry-overs.

## Step 7 - Back up the vault to git
Commit and push the day's changes so nothing is lost across devices.
- Stage everything: `git add -A`
- Commit: `git commit -m "closeday: YYYY-MM-DD"` (use today's date)
- Push: `git push`
- If there is nothing to commit, skip the commit and push. Continue.
- If commit or push fails (no remote, offline, or auth issue), do not block the workflow. Note that the git backup was skipped so it can be retried later.

## Step 8 - Close
Report back with:
- wins logged
- carry-overs staged
- tomorrow note ready
- inbox status (cleared, or N items left to triage)
- meetings imported from Fireflies (N, with names — or none / skipped and why)
- git backup status (pushed, or skipped and why)
