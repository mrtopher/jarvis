---
type: resource
source: "https://pivotal.substack.com/p/on-data-quality-1-basics"
date_clipped: "2026-07-14"
project:
tags: [data-quality, data-platform, ai-strategy, needs-review]
---

# On Data Quality - The Fundamentals

## Summary
> Pivotal (Substack) piece by **Abraham Thomas**, June 27, 2026. Thesis: "data has no innate quality" - quality emerges from use case. Core definition: **"data quality is that which increases data value."** Proposes a **four-level ladder** rather than treating quality as one attribute. Relevant to Chris's data-platform work (Pipeline 360 ingestion/validation/processing) and to AI-data grounding for client engagements ([[Dual Logic Platform]]).

## Key Points
- **Core reframe:** quality is not intrinsic; it is defined by fitness for a use case. "Data quality is that which increases data value."
- **1. Granular / unit-level:** individual records judged on accuracy, precision, recency, consistency, plausibility. Context-dependent.
- **2. Aggregate / corpus-level:** coverage, deduplication, representativeness, cross-record consistency, distributions, stability over time. Is the whole dataset complete and clean?
- **3. Fitness-for-purpose:** the data-application interaction - informational fit (relevance, sufficiency) + operational fit (availability, compliance, usability).
- **4. Business-outcome:** does the data deliver measurable value? Needs adoption, decision impact, positive material outcomes.
- **Critical insight:** the levels are **"ordered and dependent"** - "Quality is a ladder. The lower rungs enable the higher ones; the higher rungs justify the lower ones." Failure modes: obsessing over low-level metrics (achieves nothing) or jumping to outcomes without foundational hygiene.

## Why it matters to me
- Clean mental model for data-platform work (ingestion, validation, processing) and for grounding AI/RAG on trustworthy data.
- The "quality ladder" is a CEO-legible frame for why data hygiene is not busywork - a good `/content` or client-conversation tool.

## Connections
- Topic: data quality, data platforms, AI grounding
- Project: [[Dual Logic Platform]]
- Candidate `/content` idea: "Data quality is a ladder, not a checkbox" for Joe CEO.

## Link
https://pivotal.substack.com/p/on-data-quality-1-basics
