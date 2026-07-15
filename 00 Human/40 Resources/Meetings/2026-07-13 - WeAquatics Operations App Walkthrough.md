---
type: meeting
date: "2026-07-13"
attendees: ["[[David Worrell]]", "[[Emeka Brooks]]", "[[Marcelo Coelho]]", "Imby Daniel", "Elka", "Alexandra", "Tamara", "Kemmer", "Chris Monnat", "[[Faraz Ahmad]]", "[[Peter Dudka]]", "Eric (Dual Logic)", "Brady Fox"]
project: "[[WeAquatics]]"
source: Fireflies
fireflies_id: 01KVZBZ1AYS64054SSRSSV7VG5
fireflies_link: https://app.fireflies.ai/view/01KVZBZ1AYS64054SSRSSV7VG5
tags: [meeting, weaquatics, appsheet]
---

# Walkthrough of WeAquatics Operations App + Admin Automations — 2026-07-13

3:00 PM. Demo of the AppSheet operations app to the WeAquatics team ([[David Worrell]], [[Emeka Brooks]], [[Marcelo Coelho]], Imby Daniel + ops staff), delivered by Dual Logic ([[Faraz Ahmad]] leading the app, Chris + [[Peter Dudka]] + Brady supporting). Related: [[WeAquatics]].

## Summary
Walked WeAquatics through the AppSheet app that consolidates their scattered operational spreadsheets into one reporting/ops tool. Showed the coverage board (replaces manual staffing/coverage tracking) and per-location capacity tracking (configurable per location). Confirmed the operating model: **all operational edits happen in iClass** (source of truth), and the app syncs from iClass on a **24-hour cadence** (matches their current manual rhythm). Covered payroll data integration via the **Rippling API** and the plan to move the team off spreadsheets onto the app with training.

## Decisions
- **iClass stays the system of record.** Operational edits must be made in iClass to preserve data integrity; the app is downstream/read-oriented for reporting.
- **Sync cadence = every 24 hours** from iClass → AppSheet (aligned to current manual process; no real-time need).
- Coverage board replaces manual coverage/staffing tracking; location capacity is configurable per location.
- Payroll data to be integrated via **Rippling API** for consolidated financial views.
- App ownership will transfer from the Dual Logic tenant to a WeAquatics workspace when ready.

## Action items
- **Chris:** Complete the iClass → Google Sheets/AppSheet data scraping + sync once client feedback is in. → [[Complete iClass to AppSheet data sync for WeAquatics]]
- **Chris:** Work with David + MD to integrate the **Rippling payroll API** for consolidated financial views. → [[Integrate Rippling payroll API into WeAquatics AppSheet]]
- **Chris:** Prepare for **monitored real-world testing of the rescheduler automation** with inbox label triggers, targeted next week. → [[Prep monitored real-world rescheduler test with inbox label triggers]]
- **Chris:** Share the data reconciliation + field-mapping spreadsheets with stakeholders and solicit feedback.
- **Faraz:** Send the app-access invite + data-dictionary spreadsheet + feedback Google Doc; monitor and address feedback.
- **David Worrell:** Review the data dictionary + field mappings for missing/unneeded fields; test the app on real data and give feedback via the Google Doc.
- **Peter:** Support rollout/training; assist with app-ownership transfer to WeAquatics.

## Open questions
- Payroll data gaps — final decision on Rippling API access scope.
- Which fields in the data dictionary are missing or unnecessary (awaiting David's review).

## Source
Transcribed by Fireflies AI. Meeting ID `01KVZBZ1AYS64054SSRSSV7VG5` · [transcript](https://app.fireflies.ai/view/01KVZBZ1AYS64054SSRSSV7VG5). (Full transcript too large to inline; note built from the Fireflies summary + action items.)
