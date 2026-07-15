---
type: meeting
date: "2026-07-14"
attendees: ["[[Pradeep Mishra]]", "[[Muskann Badjatia]]", "Chris Monnat"]
project: "[[WeAquatics]]"
source: Fireflies
fireflies_id: 01KXDTNNHGVMBWJRTWQXXWBCKZ
fireflies_link: https://app.fireflies.ai/view/01KXDTNNHGVMBWJRTWQXXWBCKZ
tags: [meeting, weaquatics]
---

# WeAquatics Sync — 2026-07-14

9:00 AM. Short standup with [[Pradeep Mishra]] + [[Muskann Badjatia]] ([[Exactink]]) on the rescheduler workstream. Related: [[WeAquatics]].

## Summary
The class-name update is running but slower than expected — the first location alone had ~200 classes; 3–4 locations done, still within budget. Chris laid out the remaining path to close the rescheduler loop: run a real end-to-end test with instructor names now that iClass data is correct, then have the agent consume the user's emailed choice, use a makeup token to book, and finally hook up the email listener. Chris is confident it can wrap this week if the class-name job finishes cleanly today.

## Decisions
- Next steps in order: (1) let the class-name update finish, (2) run a positive end-to-end test pulling instructor names from iClass, (3) agent consumes the user's reply, validates the chosen slot in iClass, uses a makeup token to book, (4) hook up the email listener to trigger the whole flow.
- **Late-reply handling:** users get a **24-hour** window. If they reply after 24h, still run the single-slot availability validation in iClass — if the slot is available, book it regardless of lateness; if not available, escalate to a human. Chris explicitly wants to avoid re-running the whole option-generation cycle.
- **Conflict handling:** no locking. Booking always starts by looking up that one session in iClass and confirming availability; unavailable → escalate to ops. Keep it single-pass, no multi-cycle agent.

## Action items
- **Chris:** Record an iClass makeup-token **allocation walkthrough video** for Pradeep (asked for it by "tomorrow" so he can build the workflow while the class-name job runs). → tracked in [[Record and send token-process walkthrough video]]
- **Chris:** Book a follow-up sync for Thursday morning to review the allocation workflow.
- **Pradeep:** Once the class-name job finishes, start the validation flow and build the allocation workflow from Chris's video.

## Open questions
- None outstanding — mechanics agreed; execution depends on the class-name job completing.

## Source
Transcribed by Fireflies AI. Meeting ID `01KXDTNNHGVMBWJRTWQXXWBCKZ` · [transcript](https://app.fireflies.ai/view/01KXDTNNHGVMBWJRTWQXXWBCKZ).
