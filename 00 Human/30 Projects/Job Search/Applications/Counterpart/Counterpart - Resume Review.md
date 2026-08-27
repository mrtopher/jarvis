---
type: research
status: active
company: "Counterpart"
role: "VP of Engineering"
score: 91
passed: true
passes: 1
created: "2026-08-23"
tags: [job-search, resume-review]
---

# Resume Review – Counterpart VP of Engineering

> Brutal recruiter / hiring-manager audit of the tailored resume against the target JD.
> Loop target: **score >= 90/100**.

## Score: **91 / 100**  ·  Passed: **yes**  ·  Passes run: **1**

## Phase 1 – The 6-second recruiter scan
- **Where the eyes stumble:** Nowhere fatal. The header title matches the JD exactly ("VP of Engineering"), the subtitle names the three signals the JD cares about most, and the summary leads with the agents-compound-output thesis. The Phone2Action block at the bottom is thin, but it is correctly placed and reads as early-career context, not a headline.
- **Weakest signal:** The absence of any insurance/fintech/healthcare line. A recruiter scanning for "regulated industry" sees SOC 2 but no domain name. This is a real gap, not a writing miss.
- **AI smell:** Clean. No "spearheaded," "robust," "seamless," "results-driven." The AI language ("governed production," "guardrails," "compound output") reads as the candidate's own operating vocabulary, and it mirrors the JD's framing without parroting exact phrases.

## Phase 2 – Gap analysis
- **3 critical JD skills/outcomes missing or underrepresented:**
  1. Regulated-industry domain (insurance specifically). The JD lists insurance/fintech/healthcare as a strong plus; the resume shows adjacent regulated (media SaaS, B2B) but no direct insurance.
  2. HIPAA and NYC Cybersecurity compliance. The JD names all three (SOC 2, HIPAA, NYC Cyber); the resume can only truthfully claim SOC 2 and general information security.
  3. Explicit "defensible POV on where AI-native engineering is going, and where hype breaks." The resume now gestures at this (the last Dual Logic bullet), but it lands in interviews and the cover letter more than on paper.
- **Impact visibility score (1-100):** 91

## Phase 3 – Surgical rewrite (3 weakest bullets, X-Y-Z formula)
> Applied in the YAML during authoring; documented here.

| # | Before | After |
|---|--------|-------|
| 1 | "Champion LLM-powered code generation in delivery, standardizing reusable agent skills..." | "Built an operating model where agents carry the repeatable work and engineers keep context and ownership, standardizing reusable agent skills, evaluation harnesses, and DevSecOps guardrails that compound output without eroding quality or cost control." (mirrors the JD's "system carries the rest" model) |
| 2 | "Owned the engineering budget through major change... served as the sole technology voice in PE investor and board diligence." | "Owned security and compliance through a hard reset, building SOC 2 controls into the platform architecture rather than bolting them on, and served as the sole technology voice in PE investor and board diligence." (directly answers the JD's "compliance built in, not bolted on" line) |
| 3 | "Drove AI-forward development across an 800-plus employee SaaS org, turning one-off scripts into a shared, evaluated developer platform teams trusted." | Added "...and drew a clear line between where AI earns its keep and where the hype breaks." (answers the JD's "you know where the hype outpaces reality") |

## Phase 4 – Keyword optimization
> Top 5 ATS keywords from the JD. Folded in only where truthful.
- AI-native engineering — present (summary, Dual Logic bullets)
- Developer experience / developer platform — present (Dual Logic, Pipeline 360)
- SOC 2 — present (skill_groups + Pipeline 360 bullet)
- Distributed teams — present (competencies + Industry Dive bullet)
- HIPAA / NYC Cybersecurity — **NOT added** (not truthful for the candidate; flagged as a genuine gap, not written around)

## Phase 5 – Final verdict
> One-sentence pitch for the CEO: A scaled, board-tested engineering leader who already runs an AI-native operating model in production, so he can build Counterpart's agent-compounded org for real instead of pitching a demo, with the one caveat that insurance is a new domain he'll ramp fast.

## Iteration log
| Pass | Score | What changed |
|------|-------|--------------|
| 1 | 91 | Tailored from LeafLink base: retitled to VP of Engineering, reframed summary around agents compounding output, rewrote Dual Logic bullets for the AI-native operating model + hype-vs-reality, added the SOC 2 "built in not bolted on" bullet to Pipeline 360, reordered skill_groups so AI leads. Score cleared 90 on first pass; loop stopped. |

## Accuracy pass
> Honesty/factual audit run after the loop. Not scored.
- **False/misattributed tenure or scope:** None found. No "20 years building AI-first" style claim; AI-native work is scoped to Dual Logic (current) and specific initiatives, not a decades-long track record. The 8-to-40+ growth, under-90-days platform, 15% retention, and 35% time-to-ship all trace to prior resumes.
- **JD parroting rewritten in own words:** The JD phrases "the system carries the rest" and "compound every engineer's output" were deliberately reworded ("agents carry the repeatable work and engineers keep context and ownership"; "compound output without eroding quality or cost control") to avoid coached-sounding echoes.
- **Unfalsifiable self-claims cut:** None asserted. No "trusted," "world-class," "respected." Claims are shown through outcomes.
- **Fabricated/unsupported specifics (or flagged to verify):** HIPAA and NYC Cybersecurity were intentionally NOT claimed (not grounded in the candidate's history). SOC 2 is retained as it traces to Pipeline 360 diligence. **Flag for Chris to confirm:** the SOC 2 claim should reflect real, hands-on control ownership at Pipeline 360, and insurance-domain exposure is absent — be ready to address both in interviews.

## GPTHuman pass
> Optional early mechanical pass on narrative prose only.
- Cover-letter body run through GPTHuman: humanScore 98.53, but it drifted off-voice (British "organisation," "make no bones about it," "old hat," an "And"-started sentence, and it softened "I will not ship you slop and call it speed" into weaker phrasing). Per CLAUDE.md #7, VOICE wins over the black-box score, so the voice-faithful original was kept and the GPTHuman rewrite discarded.
- Resume summary skipped: it carries load-bearing numbers (8, 40+, 90 days) that a black-box rewrite could silently alter. Rule-aligned skip.

## Final polish
> VOICE.md + AI-smell remediation. Not scored.
- Checked for em dashes: none in the resume or cover letter.
- No sentences start with "and."
- Cover letter: removed a colon reveal ("draw the line clearly:" to a period), folded a dramatic fragment ("Not demos. Real components...") into a full sentence, and replaced the banned word "leverage" ("slop dressed as leverage" to "ship you slop and call it speed"). Regenerated the docx.
- Resume: varied bullet length and openers; no rule-of-three filler; no banned buzzwords ("leverage," "robust," "streamline," "cutting-edge," "spearheaded," "seamless").
- Summary rewritten at Chris's request (2026-08-23): the original read as three stacked "At Company X, I did Y" clauses. Replaced with a builder-craft-led intro that leads with identity and the speed-vs-quality craft rather than reciting accomplishments (the metrics still live in the achievements box and experience bullets). Under the 75-word cap, VOICE-clean.
