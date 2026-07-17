---
type: meeting
date: "2026-07-17"
attendees: ["Chris Monnat", "[[Peter Dudka]]", "[[Nate Gersten]]"]
project: "[[Ridgewells]]"
source: Fireflies
fireflies_id: 01KXEXS2BGRT1QN4C3R8NKTERX
fireflies_link: https://app.fireflies.ai/view/01KXEXS2BGRT1QN4C3R8NKTERX
tags: [meeting, cate, ridgewells]
---

# Weekly CATE Sync — 2026-07-17

10:30 AM. Weekly sync on the [[CATE]] build for the [[Ridgewells]] project with [[Peter Dudka]] ([[Dual Logic]]) and [[Nate Gersten]] ([[Ridgewells Catering]]). Focus: staging environment now live, plus the plan to get product in front of launch partners in August.

## Summary
Chris shipped the big infra milestone this week: the staging environment is live, giving a full local → staging → production deployment pipeline. Feature development slowed on purpose while waiting on partner feedback. Staging is at staging.app.kthq.com; production will be app.kthq.com; the marketing site is khq.com. The agent's menu/proposal output is not yet polished, so Nate can click around but should not judge output quality yet. The team set a two-track partner plan: a focused first demo with Stavros / M Culinary (Nate's warm lead, ready around July 21) gated on Chris getting staging demo-ready, and broader intro outreach to other ESEP orgs and Miami-conference contacts for early August. A workshop-style feedback session is set for Tuesday July 21 at 10:00 AM on Teams.

## Decisions
- **Three environments live:** development (local), staging (staging.app.kthq.com, test-only, volatile data), production (app.kthq.com, real clients — not stood up yet). Release flow: local → staging → sign-off → production.
- **Integration is push-only:** Kate pushes finished menus into catering software via API (Cater Expert today, ~1/3 of the market). No data is pulled back. Integration burden sits on the catering-software side, not ours.
- **Two-track partner rollout:** (1) demo with Stavros / M Culinary once staging is demo-ready, (2) start intro outreach to other ESEP orgs + Miami-conference contacts for first/second week of August.
- **Stavros gets a low-pressure dry-run call next week** (roadmap + open feedback), which is NOT gated on further functionality — separate from the full demo.
- **Next working session:** Tuesday July 21, 10:00 AM, Microsoft Teams, workshop-style to gather team feedback.

## Action items
- **Chris:** Feed Ridgewells' 3-year menu history Excel + the new tailored proposal example into the CATE agent as training data. → [[Train CATE agent on Ridgewells menu history and proposal examples]]
- **Chris:** Get the staging environment demo-ready — verify menu/proposal generation can reproduce prior "beat the event designer" quality before it goes in front of Stavros; tune the agent after Tuesday's feedback. → [[Get CATE staging demo-ready for Stavros]]
- **Chris:** Prepare a demo of current features + upcoming improvements for the launch-partner calls.
- **Peter:** Revise + send the launch-partner communication template (two-call process: quick overview, then deeper team demo) to schedule early-August intro calls. Remove the placeholder Tuesday invite once Nate sends the real one.
- **Peter:** Schedule the Stavros dry-run / intro call for next week.
- **Nate:** Send the Teams invite for the Tuesday 10:00 AM session. Test proposal/menu generation in staging and send feedback. Begin outreach/pitch prep for other launch partners (next up: Behind the Scenes, San Diego) and coordinate the Stavros call.

## Open questions
- **CaterEase API:** M Culinary (and others) run on CaterEase, not Cater Expert. Need those vendors to open APIs for the menu push. Flagged as a recurring blocker for adoption across partners.
- Will staging reliably reproduce the prior menu-generation win before the Stavros demo? Depends on the post-feedback tuning pass.

## Source
Transcribed by Fireflies AI. Meeting ID `01KXEXS2BGRT1QN4C3R8NKTERX` · [transcript](https://app.fireflies.ai/view/01KXEXS2BGRT1QN4C3R8NKTERX).
