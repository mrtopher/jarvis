---
type: research
status: active
company: "Gravie"
role: "VP, Platform & Architecture"
source_url: https://www.gravie.com/
created: "2026-08-27"
tags: [job-search, company-research]
---

# Company Research – Gravie

## Snapshot
- **What they do:** Health benefits company for small and midsize businesses (SMB). Two flagship products: **Comfort** (a level-funded health plan with $0 out-of-pocket cost on most common services) and an **ICHRA** platform (Individual Coverage Health Reimbursement Arrangement). Plus **Gravie Care** (year-round licensed advocate/service team) and a member mobile app.
- **Size / stage:** Late-stage private / growth-equity. Headcount estimates vary widely by source: ~450 to ~740 (see note below). Founded 2013.
- **Funding / ownership:** Privately held, VC/growth-equity backed. Total capital raised reported at **$463M** as of July 2026 (some databases cite higher cumulative figures of $500M+ including debt facilities — unconfirmed which is apples-to-apples). Most recent round led by **General Atlantic** (announced July 30, 2026).
- **HQ / locations:** Minneapolis, Minnesota.
- **Remote policy:** Offers remote, hybrid, and in-office roles. The target VP role is listed as Minneapolis; remote/hybrid appears available for engineering. (Confirm remote eligibility for this specific VP role.)

## Products & business model
> Gravie sells **employer-sponsored health benefits to SMBs**, positioning itself as rebuilding the health insurance stack around the consumer. Two core lines:
> - **Comfort** — a level-funded health plan marketed as $0 cost on the most common services (primary care, mental health, specialists, labs/imaging, generic drugs). Company claims ~94% of office visits covered at no cost and ~15% average total premium savings for employers. GM: Stephanie Schreiber.
> - **ICHRA** — lets employers fund tax-advantaged reimbursements so employees buy individual-market plans; marketed as more predictable cost with claimed savings up to ~29% at renewal. GM: Mimi Sibley. Gravie is riding a strong ICHRA adoption tailwind (ICHRA reportedly grew 34% among large employers and 52% among other employer types in 2025).
> - **Gravie Care** — licensed, year-round advocate team (service/retention layer).
> - **Member app** — digital ID, coverage lookup, provider search, claims tracking, plus partner-delivered virtual care (Teladoc), digital PT (Sword), fitness (FitOn).
>
> **Business model:** insurtech / benefits administration for SMB employers, monetizing through plan administration and the level-funded/ICHRA products. Market is health benefits for the 50–1,000-employee segment where ACA premium spikes are driving employers toward alternatives.
>
> **AI features:** No specific AI product launch confirmed in public sources as of Aug 2026. Do not assume an AI roadmap exists publicly; treat as an open question for interviews.

## Tech stack
> Discoverable from job posts, StackShare-type listings, and Glassdoor:
> - **Cloud/infra:** AWS, Kinesis, continuous delivery pipelines.
> - **Languages/frameworks:** Clojure and ClojureScript (newer services; re-frame on the front end), plus legacy Java / Spring Boot, TypeScript / React, Groovy.
> - **Codebase maturity (per Glassdoor engineering reviews):** roughly split — ~50% newer Clojure (well-regarded by engineers) and ~50% older platform that reviewers say "should have been migrated off years ago." Reviewers also flag that application teams are "just starting to think about scaling" and that local dev experience is weak/"non-existent."
>
> This is directly relevant to a **Platform & Architecture VP**: there is real modernization, scaling, and developer-experience work to own — a genuine mandate, but also technical debt.

## Culture & values
> - Mission framing: "build a health plan everyone can love"; consumer-centric; plans "designed to be used, not avoided."
> - Job posts describe culture as **non-hierarchical, merit-driven, "opinionated but kind," high-performance, fast-paced.**
> - Glassdoor pros: "good people," intelligent/hardworking/mission-driven teams, benefits, flexibility/remote options.
> - Cultural caution: some reviewers say leadership "preaches culture" but under-invests (e.g., "occasional pizza party isn't culture"), and note limited stated DEI initiatives.

## Reputation
> **Glassdoor:** ~**3.3 / 5 overall** (≈106 reviews); ~3.4/5 US-only (≈65 reviews). Sub-scores: culture & values ~3.1, work-life balance ~3.2, career opportunities ~2.9.
>
> **Recurring cons (important for a senior leader):**
> - **Leadership churn** — reviewers cite "lots of churn in leadership at all levels" and decisions kept private / company "blindsided."
> - **Layoffs** — multiple reviews reference repeated layoffs, some describing them as abrupt and poorly documented.
> - **Compensation** — reviews mention "low salary," "no budget for raises," and that investment concentrates at/above middle-management.
> - **Busy-season load** — work-life balance degrades heading into fall open enrollment.
>
> **Positive signal:** newer CEO Steve Wolin (ex-Oscar Health COO) is credited by some reviewers with bringing sharper focus to the business.

## Recent news
- **Jul 30–31, 2026:** New funding round led by **General Atlantic** (with FirstMark participation); total capital raised reported at **$463M**. Round size not disclosed.
- **Jul 2026:** Appointed **Eric Murphy** (former Optum executive) to the Board of Directors.
- **Jun 25, 2025:** Prior round reported as a **Series G, $150M**.
- **Early 2025:** **Steve Wolin** (former COO, Oscar Health) named CEO, replacing co-founder **Abir Sen**, who moved to Executive Chairman.
- **2025–2026:** Positioned around ICHRA growth as ACA/individual-market premiums spike for 2026.

## Green flags
- **Well-capitalized and growth-stage** — fresh General Atlantic round; strong ICHRA market tailwind; not a runway-risk seed startup.
- **Clear, substantive architecture mandate** — mixed old/new codebase, early-stage scaling, and weak developer experience mean a Platform & Architecture VP has real, high-leverage work (modernization off legacy, scaling, dev-experience/platform investment).
- **No named CTO/VP Eng publicly** — leadership page lists a **Chief Architect (Michael Cameron)** but no CTO or VP Engineering; Gravie has openly recruited a "VP of Software Engineering." Suggests **senior eng leadership is thin / this could be a top-of-org technical seat** with broad ownership.
- **Modern, engineer-respected core stack** (Clojure/ClojureScript on AWS) — attractive to strong ICs; a lever for hiring.
- **Experienced operator CEO** (Wolin, ex-Oscar Health) — healthcare-scale credibility; credited with focus.
- **Minneapolis HQ, remote-friendly** — lower-cost talent market, less bidding war than coasts.

## Red flags
- **Repeated layoffs + leadership churn** in reviews — a senior leader should probe stability, mandate durability, and how prior eng leaders exited. "Decisions kept private / blindsides" is a governance smell.
- **Compensation reputation** — reviews cite low pay and no raise budget below senior levels; may constrain the VP's ability to hire/retain and to fund a platform team. **The posted band ($270–360K + equity + bonus) is solid for Minneapolis** but the org's broader comp philosophy could make backfilling and team-building harder.
- **Significant legacy tech debt** — ~half the platform is legacy that reviewers say is overdue for migration; scaling is nascent. Green-flag mandate and red-flag risk are the same fact: expect a heavy modernization lift with limited slack.
- **Culture-vs-reality gap** — "preaches culture but under-invests"; DEI concerns. Diligence the leadership team's actual investment in engineering.
- **Ambiguous top-of-eng structure** — no public CTO. Clarify: does this VP report to CEO or CFO? Is there a CTO being hired above? Is "Chief Architect" a peer, a report, or the de facto tech lead?

## Engineering-org maturity signals (summary)
- **Named eng leadership is thin publicly:** Chief Architect (Michael Cameron) exists; **no CTO or VP Engineering listed**, and the company has actively recruited a VP of Software Engineering. This VP, Platform & Architecture role likely sits near the top of the technical org.
- **Codebase is mid-transition:** ~50% modern Clojure, ~50% legacy overdue for migration; scaling and platform/developer-experience are early. Consistent with a **mid-stage, still-maturing eng org**, not a hardened platform team.
- **Fit read for a hands-on platform/architecture VP:** Strong on paper — real mandate, modern-ish stack, capital to fund it. The role wants an owner who can both set architecture direction and get hands dirty on legacy migration, scaling, and dev experience. Primary risks are organizational (layoff/leadership churn, comp philosophy, mandate durability) rather than technical.

## Sources
| Source | Type | Key Takeaway |
|--------|------|-------------|
| gravie.com (home, /ichra/, /story/, /members/) | Company site | Products (Comfort, ICHRA, Gravie Care), mission, leadership (no CTO/VP Eng listed; Chief Architect exists) |
| fintech.global (2026-07-31) | News | General Atlantic-led round; total raised $463M |
| prnewswire / streetinsider (2026-07) | Press release | General Atlantic round + Eric Murphy (ex-Optum) to board |
| Crunchbase / PitchBook / Tracxn | Funding DBs | Series G $150M (Jun 2025); investor list incl. FirstMark, AXA VP, Trinity Capital |
| prnewswire (2025) / coverager | News | Steve Wolin (ex-Oscar COO) named CEO; Abir Sen → Chairman |
| Wikipedia / Twin Cities Alumni | Profile | Founded Nov 2013 by Abir Sen, Jill Prevost, Marek Ciolko; initial FirstMark funding |
| Revelio Labs / LinkedIn / Datanyze | Headcount DBs | Headcount estimates range ~450–740 (varies by methodology) |
| startup.jobs / Lever / clojurejobboard (job posts) | Job listings | Stack: AWS, Clojure/ClojureScript, Kinesis, Java/Spring Boot, TypeScript/React; "non-hierarchical, merit-driven" culture |
| Glassdoor (multiple review pages) | Reviews | ~3.3/5; pros: good people, stack; cons: layoffs, leadership churn, low pay, legacy tech debt |
