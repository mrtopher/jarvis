---
type: resource
source: "https://neon.com/blog/multi-tenant-rag"
date_clipped: "2026-07-13"
project:
tags: [rag, multi-tenant, neon, postgres, architecture]
---

# Multi-Tenant RAG With One Neon Project Per User

## Summary
> Neon blog (by Tony Holdstock-Brown, CEO of Inngest, Nov 2024) proposing a multi-tenant RAG architecture where **each org gets its own dedicated Neon Postgres project** for complete data isolation and guaranteed performance. Directly applicable to any per-tenant SaaS with embeddings — relevant to [[Dual Logic Platform]] and [[CATE]] multi-tenancy decisions.

## Key Points
- **One project per tenant**: each workspace gets its own Neon project (contacts + embeddings tables) — no shared-resource conflicts, guaranteed DB performance.
- **Solves the noisy-neighbor problem** at two levels: DB load isolation + unpredictable LLM-call blast radius.
- **Cost + security isolation**: one tenant's LLM usage can't inflate another's costs; no cross-tenant data access.
- **Per-workspace throttling** (via Inngest): rate-limit by workspace ID (e.g., 10 concurrent / 10s) to respect external API limits.
- **Dynamic connections**: Neon serverless SDK + a helper that resolves the tenant project via the Neon API at runtime.
- **Batch by tenant**: embeddings inserted in workspace-grouped batches (100 docs / 60s window).

## Connections
- Project: [[Dual Logic Platform]]
- Topic: [[CATE]] multi-tenancy
- Topic: RAG data isolation (Neon)

## Link
https://neon.com/blog/multi-tenant-rag
