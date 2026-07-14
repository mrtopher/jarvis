---
type: resource
source: "https://engineering.salesforce.com/building-enterprise-ai-agents-that-are-both-autonomous-and-reliable/"
date_clipped: "2026-07-13"
project:
tags: [ai-agents, reliability, architecture, enterprise]
---

# Building Enterprise AI Agents That Are Both Autonomous and Reliable

## Summary
> Salesforce AI Research (Phil Mui, SVP & Head of Products and Architecture) on resolving the core tension between agent **autonomy** (usefulness) and **control** (trustworthiness) via "guided determinism" — deterministic orchestration wrapped around probabilistic reasoning so high-stakes workflows stay reliable. Directly relevant to the consulting/platform agent work in [[Dual Logic Platform]].

## Key Points
- **Guided determinism**: deterministic exits despite probabilistic internals — enforce decisions structurally through orchestration, not conversationally through the LLM.
- **Agent Graph Orchestration**: model business processes as graphs with nodes (tasks) + guarded edges (validation gates); no unsupervised model decisions at critical junctures.
- **Specialized subagents** over one general model — routing, verification, escalation each get their own risk/flexibility budget.
- **Fine-tuned smaller models (8–32B) for routing** — ~50ms latency at accuracy, reserving frontier models for where they add value.
- **Prompt-engineering limit**: instructions are probabilistic interpretations, not guarantees — "doom-prompting" can't close reliability gaps.
- **Observability first**: deep tracing, synthetic testing at scale, and LLM-as-judge quality eval for continuous post-deploy evaluation.

## Connections
- Project: [[Dual Logic Platform]]
- Topic: AI agent reliability / orchestration

## Link
https://engineering.salesforce.com/building-enterprise-ai-agents-that-are-both-autonomous-and-reliable/
