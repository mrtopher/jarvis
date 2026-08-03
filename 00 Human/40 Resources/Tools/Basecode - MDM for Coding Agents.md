---
type: resource
source: "https://basecode.cloud/"
date_clipped: "2026-08-03"
project:
tags: [ai-agents, governance, observability, platform-engineering, tool]
---

# Basecode - MDM for Coding Agents

## Summary
> Management + observability platform that centralizes control over coding agents (Claude Code, Copilot, Codex, Gemini, others) across an engineering org — "MDM for coding agents." Fleet-wide visibility, gateway-enforced policy/budget guardrails, and portable Agent Profiles stored as plain git repos. Relevant to AI-adoption / governance work: it's the enterprise control plane for the exact "who's running which agent, at what cost, under what policy" problem.

## Key Points
- **Observability & control**: fleet-wide tracking of activity, token spend, and project attribution across devices; real-time logging of every prompt/response/LLM call with latency + cost.
- **Governance**: Agent Profiles as git repos (OpenGAP standard) holding policies, knowledge, skills; approved-stack enforcement across six dimensions; agents auto-refuse off-policy work with no plugins/forks.
- **Policy enforcement**: OPA/Cedar guardrails at the gateway that allow/deny/redact — cannot be disabled locally.
- **Cost management**: hard budget ceilings per group/model/employee enforced pre-request; Complexity Router sends simple tasks to cheaper models, hard reasoning to frontier models; model gateway remaps any agent to any provider via scoped virtual keys.
- **Adoption**: hideable TUI client (additive, works with any IDE) for mid-task agent swapping; centrally managed skills + MCP injection; custom subagents as plain markdown; ships with Architect, a Rust-based coding agent.
- **No lock-in**: built on the Git Agent Protocol (OpenGAP); if you leave, all profiles/policies remain as plain git repos. Live sync over WebSocket (wss://).

## Connections
- Topic: AI governance / enterprise AI adoption (compare vs. building in-house controls)
- Related: [[What Is AI Governance (Docker)]]

## Link
https://basecode.cloud/
