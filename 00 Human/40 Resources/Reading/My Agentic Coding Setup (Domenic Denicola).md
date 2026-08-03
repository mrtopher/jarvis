---
type: resource
source: "https://domenic.me/agentic-coding-setup/"
date_clipped: "2026-08-03"
project:
tags: [ai-agents, agentic-coding, developer-workflow, claude-code, reading]
---

# My Agentic Coding Setup (Domenic Denicola)

## Summary
> Practitioner walkthrough by **Domenic Denicola** of a personal architecture for running frontier coding agents autonomously and working across desktop, laptop, and phone. Core move: a disposable Linux VM on a home desktop, reachable everywhere over Tailscale, with agents run in bypass-permissions mode and git worktrees fanning out parallel work streams. Concrete, opinionated tooling choices; a useful reference for what a serious agentic-coding rig looks like in mid-2026.

## Key Points
- **Disposable VM**: Ubuntu Server on Hyper-V on a home desktop; treat it as throwaway and push to GitHub often as the safety net.
- **Access anywhere**: Tailscale VPN links desktop, laptop, and phone to the VM — enables fixing a prod bug from a phone on a train.
- **Agents**: Claude Code and ChatGPT's Codex CLI as the harnesses; run in "bypass permissions" mode to cut interruptions (accepts the risk because agents behave aligned in practice, mitigated by frequent pushes).
- **Parallelism**: git worktrees for concurrent agent work streams. Warns off the Claude desktop app's worktree handling (it nests worktrees inside projects and causes conflicts).
- **Remote workflow**: ChatGPT app over SSH for better session syncing; review code via VS Code Remote-SSH into the VM.
- **Preview servers**: Portless (`tportless`) exposes dev servers on Tailscale URLs as secure contexts, avoiding port collisions between parallel agents.
- **Config sync**: chezmoi syncs dotfiles, agent configs, and skills across machines via a private GitHub repo.

## Why it matters to me
- Reference architecture for running Claude Code agents autonomously and portably — directly relevant to Chris's own agentic-coding practice and the [[Dual Logic Platform]] AI-native dev story.
- The bypass-permissions + frequent-push + disposable-VM pattern is a concrete take on the agent-guardrails question (compare vs. org-level control planes like [[Basecode - MDM for Coding Agents]]).

## Connections
- Topic: agentic coding / AI-native developer workflow
- Related: [[Basecode - MDM for Coding Agents]], [[QM - Multiplayer Agent Harness for Startups]]

## Link
https://domenic.me/agentic-coding-setup/
