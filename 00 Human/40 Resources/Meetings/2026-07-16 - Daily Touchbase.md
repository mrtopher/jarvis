---
type: meeting
date: "2026-07-16"
attendees: ["[[Faraz Ahmad]]", "Peter", "Chris Monnat"]
project: "[[WeAquatics]]"
source: Fireflies
fireflies_id: 01KXGV2MT92GACJS0P9PEKXATW
fireflies_link: https://app.fireflies.ai/view/01KXGV2MT92GACJS0P9PEKXATW
tags: [meeting, weaquatics]
---

# Daily Touchbase — 2026-07-16

1:00 PM. Working session with [[Faraz Ahmad]] on the [[WeAquatics]] AppSheet data pipeline. Peter on invite.

## Summary
Focused on locking down the data sources and report-to-table mappings for the AppSheet app. Plan: each iClass report gets a report ID and column-level mapping so it links cleanly to its AppSheet table. Payroll data is defined, but some data (like instructor certifications) lives in team spreadsheets, and leads come from an external CRM (whether leads data is even needed for AppSheet is still open). New iClass reports are needed for some pulls. Build approach: automated workflows in n8n + Nova Act microservices, but the initial full data load may be done manually (CSV experiments), deferring automated workflows to incremental updates. Immediate priorities: update the spreadsheet with report IDs, run a manual CSV merge experiment, and stand up staging data tables in n8n.

## Decisions
- Each iClass report gets a **report ID + column-level mapping** in the spreadsheet so it maps to the right AppSheet table.
- **Initial full data load may be manual** (merge iClass CSVs by hand); automated n8n workflows are for incremental updates going forward.
- Build the n8n staging data tables to match the data-dictionary structure (all columns, even if empty).

## Action items
- **Faraz:** Add a report-ID column to the spreadsheet; build an organized report-ID + column-mapping structure for the AppSheet tables by the 10:00 AM sync; experiment with merging multiple iClass CSVs into one clean programs-table CSV (using Claude); start creating the n8n data tables to match the data dictionary; confirm he can run n8n workflows locally. Ping Chris in Slack with any blockers.
- **Chris:** Re-send Faraz the iClass login credentials; send Faraz the n8n platform login; monitor Faraz's progress and help with script development once the mappings are finalized; co-lead the 10:00 AM sync.

## Open questions
- Is leads data (from the external CRM) actually needed for AppSheet?
- Which additional iClass reports need to be created for the remaining data pulls?

## Source
Transcribed by Fireflies AI. Meeting ID `01KXGV2MT92GACJS0P9PEKXATW` · [transcript](https://app.fireflies.ai/view/01KXGV2MT92GACJS0P9PEKXATW).
