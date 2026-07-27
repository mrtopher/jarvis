---
type: resource
source: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
date_clipped: "2026-07-27"
project:
tags: [reading, ai, data, ai-agents, standards, context-engineering]
---

# How the Open Knowledge Format Can Improve Data Sharing (Google Cloud)

## Summary
> Google Cloud blog introducing the Open Knowledge Format (OKF, v0.1, published 2026-06-12): an open, vendor-neutral spec that turns the informal "LLM wiki" pattern into a portable standard for giving AI agents curated context. OKF represents knowledge as plain Markdown files that both humans and machines can read, so the same knowledge (table definitions, metrics, business concepts, join paths) can be shared across agents, LLMs, tools, and organizations without proprietary accounts or SDKs. The data-sharing angle: a vendor can ship a catalog export as OKF and your agent consumes it directly with no integration work, and BigQuery table/metric definitions can live as a bundle committed next to the SQL they describe, reviewed via pull requests.

## Key Points
- **What it is:** a simple, vendor-neutral Markdown spec for representing curated knowledge for AI agents. Not tied to any cloud, database, model provider, or agent framework; never requires a proprietary account or SDK to read, write, or serve.
- **Problem it solves:** organizational knowledge (schemas, metric definitions, semantics) is scattered and locked in proprietary tools, so every agent/team re-does the context work. OKF makes that context portable and version-controllable.
- **BigQuery reference implementation:** an enrichment agent walks a BigQuery dataset, drafts an OKF concept doc per table/view, then a second LLM pass crawls authoritative docs to enrich each concept with citations, schemas, and join paths.
- **Data-sharing model:** definitions export as a bundle committed alongside the SQL; changes reviewed through pull requests (knowledge treated like code). Vendors ship catalog exports as OKF that agents consume directly.
- **Why it matters now:** as agents move to production, the bottleneck is curated context, not raw data. A shared, human-readable standard for that context is the missing piece (a "semantic/knowledge layer" for agents).

## Connections
- Project: consulting / client AI-agent + data-platform work (Dual Logic)
- Topic: context engineering / knowledge layer for AI agents; data governance; open standards
- Related: [[Building a Context Layer From the Ground Up (Gorgias)]] (same theme: curated context as the real work behind reliable agents)
- Related: [[What Is AI Governance (Docker)]] (governance/versioning of what agents are allowed to know)
- Related: [[On Data Quality - The Fundamentals]] (quality of the underlying definitions OKF exports)

## Link
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
