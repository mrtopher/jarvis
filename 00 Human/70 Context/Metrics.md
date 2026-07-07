---
type: data
tags:
  - metrics
---

# Metrics

Data source for the **[[Operations Dashboard]]** audience panel.

- One row per day. Newest row = "today", second-newest = "yesterday".
- The dashboard reads the **last** row for current values, computes "vs yesterday"
  from the previous row, and "this week" from the row ~7 days back.
- Keep the column order. Add a new row each day (or let `/closeday` append one later).
- Numbers below are placeholders. Replace with your real counts.

| date       | youtube | instagram | threads | x  | tiktok |
| ---------- | ------- | --------- | ------- | -- | ------ |
| 2026-07-05 | 10482   | 159       | 9       | 58 | 1185   |
| 2026-07-06 | 10535   | 161       | 9       | 59 | 1192   |
