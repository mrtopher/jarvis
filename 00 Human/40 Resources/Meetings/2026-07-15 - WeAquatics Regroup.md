---
type: meeting
date: "2026-07-15"
attendees: ["[[Pradeep Mishra]]", "[[Muskann Badjatia]]", "Chris Monnat"]
project: "[[WeAquatics]]"
source: Fireflies
fireflies_id: 01KXHN1SDYYMVATBTHHE2C24WP
fireflies_link: https://app.fireflies.ai/view/01KXHN1SDYYMVATBTHHE2C24WP
tags: [meeting, weaquatics]
---

# WeAquatics Regroup — 2026-07-15

9:00 AM. [[Pradeep Mishra]] + [[Muskann Badjatia]] ([[Exactink]]) on the rescheduler workstream. Related: [[WeAquatics]].

## Summary
Walked Pradeep and Muskann through the existing n8n rescheduler build so they can pick up the Nova Act workstream. Covered the email-intake-and-acknowledge flow, the job-queue-worker pattern, and how the intake form lets them test without live email. Flagged that the inbox model changed (shared `info@` inbox with label-based routing, not a dedicated rescheduler inbox), and that the old build is over-complicated and likely needs simplifying. Muskann raised a relationship check-in about future work.

## Decisions
- Inbox approach changed: rescheduling messages now arrive at a shared general inbox (likely `info@weaquatics...`), not a dedicated one. The job should act only on messages **labeled "reschedule"** (labeled by a human or by Gemini), not on every message.
- Avoid stacking AI on AI. Peter/client already run Gemini on that inbox. Coordinate so Gemini labels and the n8n job simply picks up labeled messages, rather than a second AI pass.
- The two workflows Pradeep/Muskann need: **Email Intake & Acknowledge** and **Job Queue Worker** (which kicks off the Nova Act job).
- Testing path: use the n8n intake form (parent name, email, child name, location, date requested) to insert a record into the job-queue data table, then run the Nova Act workflow manually. No email needed to test.
- Cost model: only AI nodes (agent/LLM, running Sonnet) and Nova Act scripts on Bedrock Agent Core incur cost. Running cheap so far; not a concern.
- Existing build is conceptual, never run end to end, and probably over-complicated. Expect to simplify/rebuild.

## Action items
- **Chris:** Move the remote n8n login/credentials into the shared WeAquatics vault so Pradeep + Muskann get access (~5 min after call). → [[Share remote n8n login to WeAquatics vault]]
- **Chris:** Deliver the token-process walkthrough recording to the team today. → [[Record and send token-process walkthrough video]]
- **Chris:** Email the client this morning confirming the class-name functionality is complete; invite questions/concerns. → [[Email WeAquatics client - class-name feature complete]]
- **Pradeep:** Study the Email Intake and Job Queue Worker flows once credentials land; investigate whether a Gmail label trigger or a polling check is the right trigger; learn how the AWS Nova Act instance is invoked.

## Open questions
- Is a Gmail **label** an available n8n trigger, or does the job have to poll the inbox every few minutes for newly labeled messages?
- Exact shared inbox address and the finalized "reschedule" label/filter criteria.

## Relationship note
Muskann asked for feedback ~1.5 months in and signaled interest in a long-term, multi-project relationship (not just AI: WordPress, custom frameworks, custom apps). Chris said things are going well, more work is coming this month into next, and he'll keep Exactink in the loop on opportunities. Worth tracking as a bench/vendor relationship.

## Source
Transcribed by Fireflies AI. Meeting ID `01KXHN1SDYYMVATBTHHE2C24WP` · [transcript](https://app.fireflies.ai/view/01KXHN1SDYYMVATBTHHE2C24WP).
