---
type: concept
status: active
tags: [concept, product, cate]
---

# CATE

## Core Claim
> CATE (repo: `cate-platform`) is an AI workspace that collapses hours of manual catering-event planning (menus, mood boards, cost calculations) into minutes inside a single connected workspace.

## Context
> The SaaS product [[Dual Logic]] is building for the [[Ridgewells Catering]] client, which they intend to spin off as a standalone company. Delivered via the [[Ridgewells]] project; code and docs live in the GitHub repo `cate-hq/platform` (mirrored read-only into that project's `repo-docs/`).

## Key Points
- **Target problem:** Catering planners work each event across disconnected tools (menu creation, mood boards, cost calcs) with nothing tying them together. Slow and fragmented.
- **Approach:** AI generation turns tool-by-tool manual work into minutes in one workspace.
- **Primary user:** Catering company event planners turning an inquiry into a client-ready deliverable (menu + mood board + costs) without adding staff.
- **Three tracks:** AI Generation (the speed bet), Workspace & Event Management (the connected home for deliverables), Cost Calculators (fast, trustworthy pricing).
- **Key metrics:** time to client-ready deliverable, completion rate, deliverables per planner/week.
- **Core domain model:** Account (one catering company / tenant) -> Membership/Roles (Account Owner, Account User, Super Admin) -> Proposal (one event engagement, holds the brief + Status + Value + Menu) -> Menu (AI-generated, catalog-sourced or proposed-new items) grounded on the Account's Catalog + Style profile.
- **Stack:** Turborepo + pnpm monorepo, Next.js (App Router) + TypeScript at `apps/web`, InsForge backend.

## Connections
- [[Ridgewells]] (delivery project)
- [[Ridgewells Catering]] (client, planned spin-off owner)
- [[Dual Logic]] (builder)
- [[Nate Gersten]] (design system)

## Open Questions
- Spin-off timing/structure: when does CATE become its own company, and who staffs it?
- Go-to-market beyond Ridgewells: is CATE sold to other caterers, or Ridgewells-owned first?
