---
type: resource
status: active
source: meeting
date_clipped: "2026-07-07"
project: WeAquatics
tags: [meeting, weaquatics, client]
---

# WeAquatics × Commit Swimming Platform Eval

> Platform evaluation call: [[WeAquatics]] (with [[Dual Logic]] advising) evaluating **Commit Swimming** as a swim team management platform. Feeds the end-of-July [[WeAquatics]] recommendation.

## Attendees
- **WeAquatics:** [[David Worrell]] (Owner), [[Malanda Worrell]], [[Jared (WeAquatics)|Jared]] (technical), imby@weaquatics.com, Coach Solomon (nxlvlswim@gmail.com)
- **Dual Logic (advising):** Chris Monnat (technical advisor)
- **Commit Swimming (vendor):** [[Calvin Fridirici]]

## Summary
Commit positions as the #2 US swim team management platform (2M+ users, 3M workouts, 300+ clubs + national federations). Demoed integrated meet management (Hy-Tek imports, filtered invites, per-meet messaging), automated billing via Stripe with group-specific fees and real-time adjustments, a workout builder with pacing/performance tracking, granular staff permissions, and a family parent portal. Onboarding ~3 weeks. **Team Premium is $2,490/yr** (incl. hosted website, up to 3 team sites, 15 users/site; extra users cost more); Team Basic drops hosting.

## Decisions
- **Prioritize the swim team on Commit now; defer swim lessons.** Commit's lessons module lacks the complex instructor scheduling WeAquatics needs (75 instructors, 19 locations); an improved lessons module is planned for summer.
- Commit is a credible fit for the swim team workstream; move toward adoption planning.

## Action Items (from Fireflies, by owner)
- **Calvin Fridirici (Commit):** follow up with David on open questions + next steps for adoption; investigate programmatic/API report access.
- **David Worrell:** provide roster + reporting requirements for onboarding/integrations.
- **Jared (WeAquatics):** support technical questions; review Commit's fit for the lesson progress-tracking checklist.
- **Malanda Worrell:** prepare additional operational questions; coordinate comms + billing workflows.
- **Commit support team:** provide personalized video tutorials for billing, group assignments, onboarding.
- **David + team:** decide adoption timeline (swim team first).
- **Chris / Dual Logic (advisory):** [[Fold Commit Swimming eval into WeAquatics recommendation]]; [[Assess Commit Swimming API and export limits for WeAquatics]].

## Open Questions
- API access is paid and limited; today it's mostly manual CSV exports. Can Commit expose programmatic report access for automation (Zapier / n8n / Sage Intacct)? Calvin to investigate.
- When do Commit's lessons features mature enough to migrate the lessons side (75 instructors, 19 locations)?
- No live Meet Mobile results integration — results upload post-meet. Acceptable for WeAquatics?

## Source
- Fireflies transcript ID: `01KWVXRC14X3PB89EMSB442SRB`
- Recording: [Zoom](https://us02web.zoom.us/j/89886688983?pwd=AY2ttL4v8TlL0PHaMAFEaRXivqHLcQ.1) · 62 min · 2026-07-07
