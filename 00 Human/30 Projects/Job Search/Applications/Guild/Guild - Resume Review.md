---
type: research
status: active
company: "Guild"
role: "VP of Engineering"
score: 90
passed: true
passes: 2
created: "2026-07-28"
tags: [job-search, resume-review]
---

# Resume Review – Guild VP of Engineering

> Brutal recruiter / hiring-manager audit of the tailored resume against the target JD.
> Loop target: **score >= 80/100**.

## Score: **90 / 100**  ·  Passed: **yes**  ·  Passes run: **2**

## Phase 1 – The 6-second recruiter scan
- **Where the eyes stumble:** Almost nowhere on the top third. Title matches the req exactly ("VP of Engineering"), the subtitle names Engineering Leadership + Platform + AI, and the summary opens on the JD's own verbs (plan, build, ship; reliability vs growth bets; platform so teams ship without fighting the plumbing). The only micro-stumble is that "manager of managers" and the 15% retention win sit late in the summary; a scanner sees them but they could land sooner.
- **Weakest signal:** No GraphQL anywhere. It is a named preferred competency and its absence is the one thing a technical screener will notice. Secondary: no EdTech / workforce-education domain, so the "members and employer partners" fluency is implied, not shown.
- **AI smell:** Clean. No "spearheaded," "robust," "leverage," "seamless," "cutting-edge," or tidy rule-of-three padding. Bullets vary in length and lead with concrete outcomes and mechanisms.

## Phase 2 – Gap analysis
- **3 critical JD skills/outcomes missing or underrepresented:**
  1. **GraphQL** — named in Preferred Competencies, entirely absent from the resume. Not in `Skills.md`, so it cannot be added honestly. Genuine gap; handle in interview (API/schema design depth on REST + serverless is the honest bridge).
  2. **EdTech / workforce-education / B2B2C marketplace domain** — no direct tenure. Mitigated by real consumer-facing B2B2C scale (Industry Dive, Phone2Action), but the specific "members + employer partners" two-sided model is not shown.
  3. **Estimation / release readiness / incident response as a headline metric** — all three are present in the bullets (sprint predictability in 60 days, release readiness, incident response, SRE) but none is quantified as a marquee outcome. Adequate, not loud.
- **Impact visibility score (1-100):** 88. Excellent match on every *required* qualification (VP multi-team scope, manager of managers, ambiguity-to-outcomes, deep technical credibility, cross-functional partnership) and on most *preferred* ones (AWS serverless via Lambda, Aurora-compatible PostgreSQL, internal developer platform, AI-native SDLC/agentic/guardrails, B2B2C growth-product engineering). Only GraphQL and domain are true gaps, both soft/preferred, so no honest rewrite raises the score meaningfully. Loop stops at pass 1.

## Phase 3 – Surgical rewrite (3 weakest bullets, X-Y-Z formula)
> No rewrite pass required (score >= 80 on pass 1). Bullets already follow an outcome-first, mechanism-backed shape. Not fabricating GraphQL or EdTech domain to inflate the score.

| # | Before | After |
|---|--------|-------|
| 1 | (n/a — no pass needed) | — |
| 2 | (n/a) | — |
| 3 | (n/a) | — |

## Phase 4 – Keyword optimization
> Top 5 ATS keywords from the JD vs the resume.
- **GraphQL** — MISSING. Not truthfully available; left out on purpose. The only unaddressed JD keyword.
- **Aurora** — PRESENT (as "PostgreSQL / Amazon Aurora"; honest, since Aurora is Postgres-compatible and Chris ran Postgres on AWS).
- **AWS serverless / Lambda** — PRESENT (summary, skills, Pipeline 360 bullet).
- **AI-native / agentic workflows / platform guardrails** — PRESENT (Dual Logic bullets, achievement, skills).
- **Internal developer platform / CI/CD / shared services / testing** — PRESENT (achievement + Industry Dive + Pipeline 360 bullets, skills line).
- **B2B2C / growth-product engineering** — PRESENT (summary, Industry Dive summary, skills line).

## Phase 5 – Final verdict
> A player-coach VP of Engineering who has already done the exact job Guild is hiring for: owning product + platform, building the paved-road internal platform so teams ship faster, hardening reliability while funding growth bets, and driving responsible AI-native delivery, with a proven manager-of-managers record of stabilizing and growing teams through change.

## Iteration log
| Pass | Score | What changed |
|------|-------|--------------|
| 1 | 88 | Initial tailored ATS resume. Strong required-qualification match; only soft gaps (GraphQL, EdTech domain), neither honestly closable. No rewrite loop run. |
| 2 | 90 | `no-ai-slop` de-duplication pass. Removed cross-section verbatim repetition (each signature phrase now anchored once in the summary): "wrestling the plumbing," "harden the core / fund the bet," "read by millions." Reworded Achievement 2 so it no longer near-duplicates the Pipeline 360 bullet, and swapped the fake-strong verb "Drove" for "Led." No facts changed and no gap closed; the +2 reflects cleaner phrasing a recruiter would otherwise ding, not GraphQL or domain movement. |

## Final polish (AI-smell + voice pass)
- Re-read `VOICE.md` and reviewed both the resume YAML and the cover letter YAML.
- No em dashes anywhere (only hyphenated compounds); no sentences start with "and"; no banned words (leverage, robust, spearheaded, seamless, cutting-edge, streamline, foster, etc.).
- Bullet openers vary within every role; no uniform length or rule-of-three padding.
- Cover letter's "AI done fast is not the same as AI done well" is Chris's own conviction from `VOICE.md`, kept as authentic voice.
- No edits required; no `.docx` regeneration needed.

## No-AI-slop de-duplication pass (post-review)
- Ran the `no-ai-slop` skill in detect mode over the resume prose (summary, achievements, experience bullets). Keyword lists (competencies, skill_groups) are out of scope.
- Individual sentences were already clean at forensic/strict tiers; the finding was document-level repetition of the writer's own best phrases across sections, which reads copy-pasted rather than deliberate.
- Fixes applied and `.docx` regenerated: anchored "wrestling the plumbing," "harden the core / fund the bet," and "read by millions" in the summary and varied each echo; reworded Achievement 2 off the Pipeline 360 bullet; "Drove" → "Led" in Achievement 4.
- All numbers and named facts (35 percent, 90 days, 8-figure line, 8→40-plus, 15 percent, 800-plus, The Trade Desk) preserved.
