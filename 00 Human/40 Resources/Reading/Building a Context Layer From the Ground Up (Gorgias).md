---
type: resource
source: "https://medium.com/gorgias-engineering/building-a-context-layer-from-the-ground-up-d6f72713915a"
date_clipped: "2026-07-24"
project:
tags: [ai-agents, context-engineering, rag, architecture, bigquery]
---

# Building a Context Layer From the Ground Up (Gorgias)

## Summary
> Yochan Khoi (Gorgias Engineering) on how they built a "context layer" for an internal AI agent that answers business questions across departments. The context layer is all the information the agent needs to produce good answers: databases, docs, call transcripts, event data, and third-party integrations, unified into one queryable system. Relevant to context-engineering and agent-reliability work.

## Key Points
- **Context layer defined**: the full collection of information an AI app needs to answer well, not just a vector store.
- **Three-part design**:
  - `ctx__model_metadata` — a table describing every data table: when to use it, how to use it, example queries.
  - `ctx__instructions` — hierarchical, on-demand topic instructions by department, using progressive disclosure to avoid context bloat.
  - **Skill instructions** — step-by-step playbooks for complex, multi-step questions with structured outputs and verification checks.
- **BigQuery + native vector search** for unstructured content, rather than a separate vector DB or direct MCP connections.
- Document the most frequently queried tables first.
- **Progressive disclosure** (hierarchical, on-demand instructions) improves both reliability and cost.
- Structure instructions around *how users ask questions*, not how the data is maintained.
- Organized, maintainable context beats one massive prompt.

## Connections
- Topic: context engineering / AI agent architecture
- Related: [[Building Enterprise AI Agents That Are Both Autonomous and Reliable]]

## Link
https://medium.com/gorgias-engineering/building-a-context-layer-from-the-ground-up-d6f72713915a
