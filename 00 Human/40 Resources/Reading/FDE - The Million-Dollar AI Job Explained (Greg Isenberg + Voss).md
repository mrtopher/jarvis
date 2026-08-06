---
type: resource
source: "https://www.youtube.com/watch?v=zXysLUTLjw4"
date_clipped: "2026-08-05"
project:
tags: [resource, forward-deployed-engineer, ai-adoption, consulting, agentic-ai, needs-review]
---

# FDE - The Million-Dollar AI Job Explained (Greg Isenberg + Voss)

## Summary
> Greg Isenberg interviews Voss (founder of Veric Agents, ex-Meta engineer) for a full playbook on the Forward Deployed Engineer role: what it is, why it pays up to ~$1M/year, and a 30-day plan to break in. Core thesis lines up exactly with [[Forward Deployed Executives - The Next Billion-Dollar Opportunity]] and [[The AI-Pilled Operating Company]]: intelligence is commoditized, so the edge moved from who has the model to who can deploy it into a specific business. That deployment skill (consulting judgment + hands-on engineering) is the moat. Directly relevant to Chris's [[Dual Logic Platform]] consulting model (audit-to-deployment, embed with the exec) and his content pillars on AI adoption. Note: the episode is partly promotional (Greg floats a paid FDE program and plugs his agency LCA; Voss is selling Veric Agents), so treat the coaching pitch as marketing, not the substance.

## Key Points
- **Intelligence is commoditized.** Every company can buy the same frontier models and the same stack (Claude Code, Codex, Cursor, Copilot). If everyone has the same intelligence, it can't be the moat. The advantage moves to deployment: where, how, and why a company applies it to its own context. That bridge is the FDE.
- **Origin: Palantir.** Palantir popularized FDE (consulting for the software age): an ontology plus connectors and data links, with engineers deployed on-site to learn workflows and spin up dashboards/agents per client. The thesis is that what worked for Palantir now generalizes, and the AI age demands it 100x more (every company needs custom agents).
- **Three stages of an FDE engagement:**
  1. **Understand the business reality.** The documented process is rarely the real process. A "trigger" like "an email arrives" hides 40+ sender formats, PDFs, screenshots, stale threads, and exceptions that live in one person's head. Sit on-site 8-10 hours (not a 1-hour interview) to see how work actually happens. This is where most time goes; communication and analytical skill matter as much as code.
  2. **FDE judgment: where intelligence belongs and where it doesn't.** Reaction to the "slap AI everywhere / token-max" era (and the MIT stat that 95% of GenAI pilots fail). Of a 10-step workflow, maybe only 3 steps need an LLM's judgment; the rest is deterministic (if/else, API calls). Weigh ROI and risk per step.
  3. **Deployed AI system.** Actually build it. Ranges from no-code workflow assembly (some Palantir FDEs only write SQL/config) to full production code. Loop is audit → eval → deployment.
- **Comp:** $150K base with heavy equity up to ~$1M/year. Called the hottest role in tech, in demand because it's new and because companies realized token-maxing without judgment burns budget (a C-suite exec blew a $10M annual Claude budget in 3 months with nothing to show).
- **Two rare judgment streams in one person:** consulting/communication (workflows, cost, incentives, risk, adoption, internal politics; McKinsey/BCG/Bain are strong here) plus software engineering (models, systems, APIs, evals, guardrails, harnesses, fine-tuning). The million-dollar FDE is the *best* of both, not the average. "Art and science, and you can speak both."
- **Audit as the wedge.** Every engagement starts with a paid audit that maps workflows, exceptions, and an ROI/priority matrix. Clients report the audit was worth 10x the price ("better than McKinsey" because AI is new and no one knows how). Trust-builder. Tip: people are allergic to the word "audit" (tax-audit connotation), so Greg's agency rebranded it as a "sprint."
- **Deploy by integrating, not migrating.** Don't force a move off NetSuite/Salesforce/SAP; build on top and connect their existing stack. Go shadow mode → increasing autonomy → production. Remember the internal champion sees you as a risk and wants to get promoted, not fired: de-risk it (do the audit free, get paid on measurable value) and help them point to a win at review time.
- **Three business metrics that matter:** revenue uplift, risk mitigation, cost savings. Measure every agent against those.
- **Model choice:** be model-agnostic as a *company* (switch to improve accuracy/cost, don't marry one inference provider), but as an *individual starting out*, master ONE model + agent-building platform first (OpenAI or Claude agent SDK), then branch to others. Value isn't agnosticism; it's understanding both sides of the aisle.
- **30-day plan (do the job before you have the title):**
  - **Week 1:** build an agent that completes one real back-office workflow loop (agent looping, tool use, guardrails, context/memory, and an audit trail). If you can't show the client what the agent did, they'll never trust you.
  - **Week 2:** make it recover. Defined JSON schema (not free text), validation, and heavy exception/failure handling. There's one happy path and a thousand unhappy ones; building for the unhappy paths is where the value is.
  - **Week 3:** make it measurable and economical. Retry logic, a golden eval dataset, cheaper models for subtasks (Gemini Flash, etc.), and measure revenue/risk/cost.
  - **Week 4:** defend it like an FDE. Business case, architecture decisions, before/after accuracy (e.g. 70% → 95%), and pitch it to real businesses for blunt feedback.

## Connections
- Project: [[Dual Logic Platform]]
- Person: [[]]
- Company: [[]]
- Topic: [[Forward Deployed Executives - The Next Billion-Dollar Opportunity]], [[The AI-Pilled Operating Company]]

## Link
https://www.youtube.com/watch?v=zXysLUTLjw4
