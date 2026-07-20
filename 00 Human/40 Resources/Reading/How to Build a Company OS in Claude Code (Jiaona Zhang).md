---
type: resource
source: "https://www.youtube.com/watch?v=qsDX0PMKcaE"
date_clipped: "2026-07-20"
project:
tags: [ai-strategy, claude-code, operating-model, company-os, video]
---

# How to Build a Company OS in Claude Code (Jiaona Zhang)

## Summary
> YouTube interview on Aakash Gupta's **Product Growth** channel. Guest: **Jiaona Zhang** (JZ), CPO at **Laurel** (AI-native time platform, formerly Time by Ping, founded 2018). She also teaches product at Stanford, Yale, and Reforge; ex-CPO at Linktree; ex-Airbnb/Webflow/Dropbox/WeWork.
>
> Core idea: Laurel built a **company-wide operating system** in GitHub where every function (CS, sales, product, finance, marketing, etc.) has a folder tree of activities, and each activity has a **skill file**. Those skills are surfaced just-in-time inside Slack/email (a daily briefing, a "chief-of-staff-light"), not a separate app. The point is to close the gap between the **1% of AI-pilled power users and the 90-99% who don't know what to use when**, by encoding the 1%'s workflows as shared skills everyone runs.
>
> Directly relevant because this vault is itself a Claude Code operating system. This is the company-scale version of the same pattern, with concrete steps, an adoption model, and org/culture mechanics worth stealing.

## Key Points
- **Company OS structure.** GitHub repo mirrors the org: one folder per function, nested folders per activity, a **skill file** per activity (e.g. CS > renewals > a "walk a renewal correctly" skill). Skills upload into Claude at the org level so anyone can call `/morning-briefing-product` and get their briefing in place.
- **Ontology / work map.** Every function's work is mapped to an ontology of categories and tasks. That map drives the OS and lets leadership say explicitly: do more of the green (agent-assisted, high-leverage) work, stop doing the tedious work (competitive analysis, synthesis, scheduling).
- **Delivery beats interface.** The winning move is surfacing playbooks/automations where people already work (Slack, email), just-in-time. Friction of going to a separate agent UI kills adoption. Build a **mega-agent/router** so people don't have to remember which sub-agent to call.
- **Four levels of AI proficiency** (use to assess a person or a whole org): L1 = chat mode (ChatGPT/Claude Q&A). L2 = automate one workflow. L3 = build apps. L4 = build/ship shared apps to customers.
- **Three steps to build your own OS.** (1) Start small: automate one tedious repeated workflow (their example: a Slack automation that intakes, enriches, triages, and tickets feature requests). (2) Write the function's playbook (Claude drafts a 50-pager in an hour), then audit line-by-line what stays human vs. gets automated, and derive skills from that. (3) Build agents per step, then a router; but they're consolidating tools like Dust into plain Claude skill files as the gap closes.
- **PMs ship to production end-to-end**, front end AND back end, using Devin (treated like a mid-level engineer). Non-engineers (PMs, even CS) ship real features via an enablement guide.
- **Captains model.** Every initiative has a captain = the person whose skill is most critical (engineer for architecture, designer for interaction, PM for content/customer-and-business judgment). You are responsible for end-to-end testing of your own feature.
- **Two-track review.** Small features move fast (an "ask-Devin" channel + PR review, no heavy process). Big/strategic changes get a real **product strategy review + architecture review**. She pushes back hard on "AI-native means no roadmaps/planning" — running fast in different directions gets you nowhere.
- **Culture and org.** Starts top-down (CEO Ryan re-architected the company AI-native). Company-wide quarterly hackathons so everyone is a builder, not just engineers. Create a dedicated **AI operations team** ("AI ops is the new biz ops") — start with one person who demonstrates value, then every function wants "their own Sasha."
- **Humans on what makes you special.** Automate logistics; keep humans on relationship-building. They systematize a value like "unreasonable hospitality" into an OS check (pull gift ideas from Gong transcripts) instead of leaving it in a doc.
- **Hiring signal = screen-share.** Ask candidates to show how they actually use AI. Quickly reveals if they're really L1 vs. building workflows/apps. She favors seasoned "super-IC" **orchestrators** and runs lean (5 PMs, 4 designers) to cut coordination cost. The best PMs get more roles; the rest feel the squeeze.
- **Fundamentals unchanged.** Don't jump to the solution, stay close to the customer, know why and for whom you're building. The tools and speed changed radically; PM 101 did not.

## My angle (for Chris / Dual Logic)
- This is a client-ready blueprint for "AI operating model" consulting: the folder-tree-of-skills-per-function pattern, the human-vs-automate audit off a playbook, and the AI-ops-team org move are all sellable engagements.
- Strong tie to the [[CATE]] / Company OS thesis and to my own vault. The just-in-time-in-Slack delivery lesson is the one I most under-index on.

## Connections
- Project: [[Dual Logic Platform]]
- Concept: [[CATE]] (Company OS thesis) · AI operating model / work-map ontology
- Related reading: [[The AI-Pilled Operating Company]]
- Topic: Company OS / Claude Code skills / AI operations team

## Link
https://www.youtube.com/watch?v=qsDX0PMKcaE

## Transcript
> Full auto-caption transcript pulled via yt-dlp (2026-07-20) and cached at /tmp/yttrans.clean.txt during capture. Re-pull with: `~/.venvs/jarvis/bin/yt-dlp --skip-download --write-auto-subs --sub-langs "en.*" --sub-format vtt <url>`
