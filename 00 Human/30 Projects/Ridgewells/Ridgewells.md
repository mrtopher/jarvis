---
type: project
status: active
date_started: "2026-07-06"
due_date:
area: Business
tags: [project, client]
---

# Ridgewells

## Goal
> Build a SaaS application for Ridgewells that they can spin off as a standalone company, [[CATE]].

## Context
> [[Ridgewells Catering]] is a catering company and [[Dual Logic]] client. We are building them a SaaS application ([[CATE]]) which they intend to spin off as a new company. Design system work ("CATE 2.0") is in progress with [[Nate Gersten]].

## Tasks
- [ ] Advance CATE 2.0 design system (with [[Nate Gersten]])

## People
- [[Nate Gersten]] (design system)

## Related
- Company: [[Ridgewells Catering]] (client) / [[CATE]] (planned spin-off)
- Topic: [[CATE]]

## Notes
- CATE = the SaaS product being built, which Ridgewells plans to spin off as its own company.

## Log
### 2026-07-06
- Created via /new. Ridgewells is a catering-company client; we're building the CATE SaaS app for spin-off. Design system ("CATE 2.0") in progress with Nate.
### 2026-07-06 (repo sync 18:01)
- Commits (45): `2c6bd44` feat(web): AI menu generation — streaming gen, review UI, e2e (U6–U8) (#19); `cd7c93f` feat(web): proposals + AI generation foundation (catalog-grounded menu-gen, Phase 1) (#18); `627dcd5` feat(web): real-world catalog + CSV import, Settings IA, (app) rename, auth fix (#17); `36ed7ae` chore(dev): project-scoped committed .mcp.json for InsForge + pnpm doctor (#16); `602cf96` feat(web): catalog & house-style management + tenant-content schema (AI menu-gen U1+U2) (#15); `e977ee8` docs(design-system): add CATE 2.0 design-system showcase source (#14); `de9917d` chore(dev): point local templates at the InsForge dev branch (#13); `5241a88` feat(web): member & role management + Super Admin overview (auth Phase 3) (#11); `8dca5bf` docs: add weekly progress reports + first report (week ending 2026-06-26) (#12); `693aca8` Merge pull request #10 from cate-hq/docs/insforge-signup-lockdown-learning; `ec1272c` docs: tighten invite email-proof wording + time-bound the probe finding (CodeRabbit); `6268bbb` docs: capture InsForge signup-lockdown learning + seed CONCEPTS.md; `584e571` Merge pull request #9 from cate-hq/claude/friendly-keller-3c5593; `f0b67a2` fix(web): canonical-origin invite links + cleanup on email reject (CodeRabbit); `dcb8428` test(web): cover the /team route-level owner gate (CodeRabbit nitpick) (+30 more)
- Merged PRs (17): #19 feat(web): AI menu generation — streaming gen, review UI, e2e (U6–U8); #18 feat(web): proposals + AI generation foundation (catalog-grounded menu-gen, Phase 1); #17 feat(web): real-world catalog + CSV import, Settings IA, (app) rename, auth loop fix; #16 chore(dev): project-scoped committed .mcp.json for InsForge + pnpm doctor; #15 feat(web): catalog & house-style management + tenant-content schema (AI menu-gen U1+U2); #14 docs(design-system): add CATE 2.0 design-system showcase source; #13 chore(dev): point local templates at the InsForge dev branch; #12 docs: weekly progress report convention + first report (week ending 2026-06-26); #11 feat(web): member & role management + Super Admin overview (auth Phase 3); #10 docs: capture InsForge signup-lockdown learning + seed CONCEPTS.md
- Open issues (2): #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-07 (repo sync 09:35)
- Commits (30): `aaead0a` fix(web): harden probe-signup config restore (CodeRabbit); `98a8e4f` fix(web): harden invite flow per code review (single-use, idempotency, hardening); `cd0596d` feat(web): invite flow + signup lockdown (auth follow-up, Phase 2); `1fbe96d` chore: bootstrap local secrets from Proton Pass (fix worktree env gap) (#7); `73180fd` Merge pull request #6 from cate-hq/claude/competent-newton-b294a1; `c8633ff` fix(web): address CodeRabbit review on password reset (PR #6); `b9b25ab` feat(web): self-service password reset (auth follow-up, Phase 1); `76a9719` Merge pull request #4 from cate-hq/chore/protect-main-with-git-hooks; `b09c161` fix: make hook install cross-platform (drop POSIX `|| true`); `1e0b4f1` chore: block direct commits/pushes to main with git hooks; `547dfca` Merge pull request #3 from cate-hq/mrtopher/User-types-authentication; `fbdb514` fix(web): address CodeRabbit review on auth foundation; `5ba7301` feat(web): multi-tenant authentication foundation on InsForge; `a72c283` docs: add user-types authentication foundation plan; `a5bc3d2` Merge pull request #2 from cate-hq/docs/exports-map-convention (+15 more)
- Merged PRs (6): #7 chore: bootstrap local secrets from Proton Pass (fix worktree env gap); #6 feat(web): self-service password reset (auth follow-up, Phase 1); #4 chore: block direct commits/pushes to main with git hooks; #3 feat(web): multi-tenant authentication foundation on InsForge; #2 docs: exports-map contract probe convention; #1 feat: shared @repo/ui design system + dashboard route
- Open issues (2): #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-13 (repo sync 09:49)
- Commits (7): `9ee75ab` feat(web): PostHog product analytics — Phase 1 (#28); `d60cec2` refactor(web): remove AI-suggested dishes from proposals (catalog-only) (#27); `5a5ab16` docs(progress): add executive status report (week ending 2026-07-10) (#23); `fbd6e25` Merge pull request #22 from cate-hq/docs/menu-gen-eval-plan; `b7c75d6` docs(evals): plan + client-inputs checklist for menu-gen quality evaluation; `73c947d` refactor(web): modals + numbered pager for the Menu Items tab (#21); `f9d4bce` feat(web): catalog-only menu generation toggle (disable AI-suggested dishes) (#20)
- Merged PRs (6): #28 feat(web): PostHog product analytics (Phase 1); #27 refactor(web): remove AI-suggested dishes from proposals (catalog-only); #23 docs(progress): executive status report — week ending 2026-07-10; #22 docs(evals): menu-gen quality evaluation plan + client-inputs checklist; #21 refactor(web): modals + numbered pager for the Menu Items tab; #20 feat(web): catalog-only menu generation toggle (disable AI-suggested dishes)
- Open issues (5): #26 Posthog Analytics; #25 Proposals - Menu Generation; #24 AI menu/catalog analyzer; #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-14 (repo sync 11:52)
- Commits (1): `2a7fbcc` feat(dev): multi-environment deployment — local (self-hosted Docker) → staging → prod (#29)
- Merged PRs (1): #29 feat(dev): multi-environment deployment — local (self-hosted Docker) → staging → prod
- Open issues (5): #26 Posthog Analytics; #25 Proposals - Menu Generation; #24 AI menu/catalog analyzer; #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-15 (repo sync 10:27)
- Commits (3): `8205276` fix(local-dev): correct apply:schema command + add alt-port launch config (#32); `99e63be` refactor(web): rename live wordmark to CATE 2.0 (#30); `0c46c71` ci(deploy): auto-deploy to staging on merge to main (#31)
- Merged PRs (3): #32 fix(local-dev): correct apply:schema command + add alt-port launch config; #31 ci(deploy): auto-deploy to staging on merge to main; #30 refactor(web): rename live wordmark to CATE 2.0
- Open issues (5): #26 Posthog Analytics; #25 Proposals - Menu Generation; #24 AI menu/catalog analyzer; #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-16 (repo sync 09:25)
- Commits (3): `5bf558b` refactor(env): inline non-secret staging/prod values; vault holds secrets only (#35); `307b33c` fix(doctor): make hints environment-aware; drop Proton Pass noise on local (#34); `c918421` docs(conventions): refresh worktree/env doc to the non-secret local model (#33)
- Merged PRs (3): #35 refactor(env): inline non-secret staging/prod values; vault holds secrets only; #34 fix(doctor): make hints environment-aware; drop Proton Pass noise on local; #33 docs(conventions): refresh worktree/env doc to the non-secret local model
- Open issues (5): #26 Posthog Analytics; #25 Proposals - Menu Generation; #24 AI menu/catalog analyzer; #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
### 2026-07-17 (repo sync 10:12)
- Commits (2): `076fc6c` Update 2026-07-17.md; `cd0182f` docs(progress): add executive status report (week ending 2026-07-17) (#36)
- Merged PRs (1): #36 docs(progress): executive status report (week ending 2026-07-17)
- Open issues (5): #26 Posthog Analytics; #25 Proposals - Menu Generation; #24 AI menu/catalog analyzer; #8 Revisit transactional email provider; #5 Enable GitHub branch protection on main after GitHub Team upgrade
- Docs mirrored to `repo-docs/` from cate-hq/platform.
