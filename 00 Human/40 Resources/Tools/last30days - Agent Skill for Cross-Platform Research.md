---
type: resource
source: "https://github.com/mvanhorn/last30days-skill"
date_clipped: "2026-08-03"
project:
tags: [ai-agents, agent-skill, research, claude-code, tool]
---

# last30days - Agent Skill for Cross-Platform Research

## Summary
> Open-source AI agent skill (`/last30days`) that researches any topic across Reddit, X, YouTube, TikTok, Hacker News, Polymarket, arXiv, GitHub, and the web in parallel — then an "AI agent judge" scores results by real engagement (upvotes, likes, money on the line) and synthesizes one grounded brief. Portable `SKILL.md` spec installable across Claude Code, Codex, Cursor, Copilot, Gemini CLI, and 50+ Agent Skills hosts. GitHub Trending #1 repo of the day.

## Key Points
- **Thesis**: Google aggregates editors; this searches *people*. Scores content by what real people engage with, not editorial ranking.
- **The unlock**: no single AI has native access to all these walled gardens (Reddit, X, TikTok, YouTube, etc.). Bring-your-own keys/browser sessions lets an agent search all of them at once and score them against each other.
- **Install (Claude Code)**: `/plugin marketplace add mvanhorn/last30days-skill` → `/plugin install last30days` (auto-updates via marketplace).
- **Install (other hosts)**: `npx skills add mvanhorn/last30days-skill -g` (`-g` = global/user-wide).
- **Zero config to start**: Reddit, HN, Polymarket, GitHub work immediately; a setup wizard unlocks X, YouTube, TikTok, arXiv, Techmeme in ~30s.
- **Runtime spec** lives in `skills/last30days/SKILL.md` — source of truth for the v3 pipeline.
- **Use case shown**: pre-meeting research that surfaces what a person is *actually* doing this month across platforms, vs. a stale LinkedIn from Google.

## Connections
- Topic: Agent Skills ecosystem (same primitive as this vault's `/` workflows/skills)
- Personal fit: continuous AI-landscape research + LinkedIn content sourcing (find what the community surfaced first)

## Link
https://github.com/mvanhorn/last30days-skill
