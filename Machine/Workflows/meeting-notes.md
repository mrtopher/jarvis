---
type: workflow
status: active
trigger: /meeting-notes
last_verified: "2026-07-07"
tags: [workflow, meeting]
---

# Workflow - /meeting-notes

Turn a meeting transcript or rough notes into a clean meeting record, action items, and person updates. Transcripts come from Fireflies AI (via MCP) or from pasted notes.

## Step 1 - Read context
Read `Machine/Personalization/meeting-notes-prompt.md`.

## Step 2 - Get the transcript
Meetings are transcribed by Fireflies AI. Its MCP tools are namespaced `mcp__claude_ai_Fireflies__*`. Pick a source based on `$ARGUMENTS`:

- **Pasted text** — if the user pasted a transcript or rough notes, use that directly and skip Fireflies.
- **Fireflies transcript ID** — if `$ARGUMENTS` looks like an ID, fetch it directly (see below).
- **Meeting name / date, or empty** — call `fireflies_get_transcripts` to list recent meetings (filter by the date/keyword in `$ARGUMENTS`; default to the most recent few). If the match is ambiguous or `$ARGUMENTS` is empty, show the candidates and ask which to process.

Once a meeting is chosen, pull from Fireflies:
- `fireflies_get_transcript` — full sentences + speakers (the raw transcript).
- `fireflies_get_summary` — Fireflies' own overview, keywords, and action items. Use this to seed Step 3 rather than re-deriving everything from raw text.

If Fireflies is needed but not connected (`! Needs authentication`), stop and tell the user to run `/mcp` → Fireflies → Authenticate, then retry.

## Step 3 - Parse the meeting
Extract (reconcile the Fireflies summary against the raw transcript):
- date
- meeting name
- attendees
- decisions
- action items
- open questions

## Step 4 - Update people notes
Create or update person notes in `00 Human/50 People/`.

## Step 5 - Create tasks
Create one task file per action item in `00 Human/20 Tasks/`.

## Step 6 - Create the meeting note
Save to `00 Human/40 Resources/Meetings/YYYY-MM-DD - [meeting name].md`. When the transcript came from Fireflies, record the source (and the Fireflies meeting ID/link) in the note so it can be traced back.

## Step 7 - Log it
Append to today's Activity Log with the number of tasks and people updated.
