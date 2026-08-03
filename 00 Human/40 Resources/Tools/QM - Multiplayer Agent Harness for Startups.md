---
type: resource
source: "https://github.com/yc-software/qm"
date_clipped: "2026-08-03"
project:
tags: [ai-agents, agent-harness, slack, platform-engineering, open-source, tool]
---

# QM - Multiplayer Agent Harness for Startups

## Summary
> Open-source (MIT) "multiplayer agent harness" for deploying AI agents across a whole org instead of as one-off personal assistants. Every employee gets an isolated workspace but can also collaborate with the agent in shared Slack channels and projects. A headless core owns identity + policy; per-scope sandboxes isolate execution. Relevant to the AI-adoption / governance lane: it's the org-wide deployment layer for "agents as a team capability," the shape enterprises reach for once personal-assistant pilots plateau.

## Key Points
- **Personal + shared scopes**: isolated memory and file access per employee; shared channels/projects for collaboration.
- **Unified identity**: one identity across Slack and the web UI.
- **Admin-controlled security postures**: Strict, Auto, or Dangerous modes set the guardrail level.
- **Automation**: background crons and watches; custom internal web apps.
- **Model-agnostic**: runs Pi, OpenCode, Codex, and Claude Code.
- **Stack**: TypeScript/Node + Fastify backend, PostgreSQL for sessions/state, Vite + Lit frontend, Slack (Bolt) integration, optional AWS/Fly deploy.
- **Adoption path**: use a separate deployment repo or a private fork, with tooling to sync upstream while keeping customizations private.

## Connections
- Topic: AI governance / enterprise AI adoption (org-wide agent deployment vs. personal assistants)
- Related: [[Basecode - MDM for Coding Agents]] (governance/control plane), [[Flue - The Open Agent Framework]]

## Link
https://github.com/yc-software/qm
