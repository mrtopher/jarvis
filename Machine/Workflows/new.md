---
type: workflow
status: active
trigger: /new
last_verified: "2026-05-01"
tags: [workflow, capture, routing]
---

# Workflow - /new

Capture and route a raw input into the right notes with as little friction as possible.

## Step 1 - Accept the dump
Do not ask clarifying questions first.

If `/new` is run with no input (or explicitly to "triage the inbox"), instead read the unprocessed captures in `00 Human/00 Inbox/Inbox.md` (bullets under `## Unprocessed`) and treat each one as an input to route. These are quick captures from the Operations Dashboard.

## Step 2 - Classify the pieces
Split the input into any mix of:
- task
- frog
- project update
- person update
- resource
- idea/inbox
- general log entry

## Step 3 - Route each piece
- Tasks -> `00 Human/20 Tasks/`
- Frogs -> today's daily note `## 🐸 Frogs to Eat`
- Project updates -> project note log
- People -> `00 Human/50 People/`
- Resources -> `00 Human/40 Resources/`
- Ideas worth keeping raw -> promote to a full note in `00 Human/00 Inbox/` using the `Inbox Capture.md` template

## Step 3b - Clear routed items from the running inbox
If an item came from `00 Human/00 Inbox/Inbox.md` (the `## Unprocessed` list), remove its bullet once it has been routed. A capture is "processed" when it has become a task, project update, person/resource note, or a promoted Inbox Capture note. The bullet count under `## Unprocessed` is what the Operations Dashboard shows as the inbox backlog, so keeping it accurate is what makes "inbox zero" real.

## Step 4 - Add links where obvious
Link to the projects or people you just created or found.

## Step 5 - Log the run
Append a timestamped note to today's Activity Log summarizing what was routed.

## Step 6 - Report back
Tell the user what was created, updated, or left ambiguous.
