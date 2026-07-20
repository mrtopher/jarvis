---
type: content
channel: webinar
status: planning
date: "2026-07-20"
topic: Live demo script for the agentic browser automation webinar
pillar: adopting AI well
tags: [content, webinar, demo-script]
---

# Demo Script - Agentic browser automation webinar

Companion to [[2026-07-20 - agentic-browser-automation|Webinar - The Browser Does the Busywork]]. This scripts the 10-minute live demo segment. Driver: the `agent-browser` skill.

## Scenario decision

**Chosen: multi-portal invoice consolidation.** The agent logs into two vendor accounts, pulls the latest invoice line items from each, and writes them into one Google Sheet.

Why this one over web-form triage:
- It is the literal task in every promo asset. "Copy the number, paste it into the system that refuses to talk to the first one." The demo closes the loop the emails and posts opened.
- It shows the new part clearly: the agent reads a page, decides, clicks, types, and works across more than one site.
- It scores three yeses on the fit test, so it doubles as a live worked example of the framework.

**Backup scenario (if consolidation setup slips): web-form triage.** The agent reads a small stack of demo contact-form submissions and sorts each into a category (sales, support, spam) in a sheet. Simpler to stage, same teaching beats.

## Safety setup (non-negotiable)

- Two **sandbox vendor accounts you own**, seeded with **fake invoice data**. No real vendor, no real customer, no real dollar figures.
- The destination Google Sheet is a **throwaway**, not connected to anything real.
- Nothing on screen is a production login or real payment data. Say this out loud during the demo. It is itself a lesson in responsible deployment.
- Browser profile is clean: no saved passwords for real accounts, no personal tabs, no email signed in.

## Pre-flight checklist

- [ ] Rehearse the full run end to end at least twice on the actual demo machine and network.
- [ ] Record a clean backup screen capture of a successful run. This is your parachute if the live network or a login fights back.
- [ ] Confirm the sandbox accounts are logged out at the start (so the login step is visible) but credentials are ready to paste.
- [ ] Zoom the browser to a size the back row can read. Increase font.
- [ ] Silence notifications. Close every tab that is not the demo.
- [ ] Have the backup recording cued to one keystroke away.

## The task, in plain English

> "Go to Vendor A and Vendor B. For each, open the most recent invoice. Pull every line item: description, quantity, unit price, total. Put them all in one Google Sheet, one row per line item, with a column for which vendor it came from. Flag any total that does not match quantity times unit price."

That last clause is the recovery hook. See below.

## Run of show (10 minutes)

| Time | On screen | Chris says (beats, not a script to read) |
|------|-----------|------------------------------------------|
| 0:00-1:00 | Show the empty Google Sheet and the two vendor portals logged out. | "This is the busywork. Two portals, one sheet, and a human who copies numbers between them every week. Watch what happens when an agent does it instead. Everything here is a sandbox, fake data, no real accounts." |
| 1:00-2:30 | Kick off the agent with the plain-English task. It navigates to Vendor A and logs in. | "Notice I did not write code. I described the task the way I would to a new hire. It is reading the page and deciding where to click. That is the difference between this and a script." |
| 2:30-4:30 | Agent opens the latest invoice, extracts line items, writes them to the sheet. | "It is reading the invoice, pulling structured data out of a messy page, and writing it into the sheet. This is question two from the fit test in action: the rules fit on an index card, so it stays reliable." |
| 4:30-6:00 | Agent moves to Vendor B. **Planned stumble here.** | See "The stumble" below. |
| 6:00-8:00 | Agent finishes Vendor B, flags the mismatched total. | "There it is. It caught a total that does not add up and flagged it instead of trusting the page. That flag is the guardrail. The agent is not just doing the work, it is checking the work." |
| 8:00-9:00 | Show the finished sheet, both vendors, flagged row highlighted. | "One sheet, two portals, a few minutes, and a human never touched it. That hour is back on your team's calendar." |
| 9:00-10:00 | Back to the fit test slide. | "Run the three questions on that task and it was three yeses. That is why it worked. Now let me show you a task that would have failed." (Bridge to limits or Q&A.) |

## The stumble (the whole point of the demo)

Engineer one recoverable snag at Vendor B and let the audience watch the recovery. Pick one:

- **Layout drift:** Vendor B lists invoices in a different order or under a different label, so the "most recent" is not where the agent first looked. It re-reads the page and corrects.
- **Slow load:** the invoice page loads slowly and the agent waits and retries instead of grabbing an empty page.
- **The mismatch flag:** the seeded fake invoice has a total that does not equal quantity times unit price. The agent flags it rather than copying a wrong number through.

Recommended: use **the mismatch flag** as the primary teaching moment (it shows judgment and self-checking), and keep **layout drift** in your pocket if it happens naturally.

What to say when it stumbles: "This is the part demos usually cut. It hit something unexpected. Watch. It did not plow ahead and copy a bad number. It slowed down and flagged it. That is exactly the behavior you want, and it is exactly the behavior you have to design for."

## If the live run fails

Do not fight it on stage. One sentence and cut: "The live network is having a moment, which honestly proves the point about brittleness. Here is a clean run I recorded earlier." Roll the backup capture and narrate over it. The lesson lands either way.

## What the demo proves (tie-backs)

- The agent reads and reacts to the page, so it is not a brittle script. (What it actually is.)
- It succeeded because the task passed all three fit questions. (The framework, live.)
- It caught its own error instead of trusting the page. (Oversight as a feature.)
- The stumble and recovery show the honest limits without a slide. (Where the hype fails.)

## Notes
- Voice check vs VOICE.md on the spoken beats: no em dashes, no "and"-starts, short punchy. PASS.
- BLOCKERS before the session: (1) stand up the two sandbox accounts with fake invoices, (2) seed one invoice with a deliberate total mismatch, (3) build the throwaway destination sheet, (4) two full rehearsals plus the backup recording.
