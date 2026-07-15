---
type: research-brief
status: active
question: "How to price out n8n workflow automation work for a client"
audience: vendor
handoff_doc: "https://docs.google.com/document/d/1l8idGSDdsVh1VdRTYrL78M11FVAezV_24vo9JlbsRD0/edit"
date: "2026-07-14"
tags: [research, automation, pricing, n8n, dual-logic, needs-review]
---

# Research Brief - Pricing n8n Workflow Automation Work

## Question
> How should n8n workflow automation work be priced for a client, and what guidance can be handed to a vendor or subcontractor delivering that work? Scope: pricing models, 2026 rate benchmarks, complexity tiers, and the factors that move price.

## Answer (TL;DR)
> Do not sell hours, sell outcomes. Price per workflow or per project with a fixed scope, then attach a monthly retainer for monitoring and changes. Use hourly only for discovery or ambiguous scope. In 2026, US automation consultants run $80-150/hr, one-time n8n workflows run roughly $200-1,500 for simple builds up to $8,000-25,000+ for production AI agents, and ongoing retainers run $1,000-3,000/mo (agencies $5,000-15,000/mo). Price on complexity, integration count, reliability/compliance needs, and how much ownership (docs, monitoring, training) the client wants.

## Key findings
- **Five pricing models, ranked for this work:**
  1. **Per-workflow (fixed)** - clean unit of value; best default for well-scoped builds.
  2. **Project/fixed-bid** - a bundle of workflows with one scoped price; best for multi-system builds.
  3. **Monthly retainer** - continuous monitoring, fixes, and small changes; predictable revenue, and automations need care after launch.
  4. **Tiered packages** - Basic (1 workflow) / Pro (3 workflows + integration) / Enterprise (custom + access control); good for productizing.
  5. **Hourly** - only for discovery or genuinely ambiguous scope; caps upside and punishes speed, so avoid as the primary model.
  - Value-based pricing (a slice of the hours or cost saved) is the highest-margin option when you can quantify the client's savings.
- **2026 hourly benchmarks:** US $80-150/hr; freelance marketplaces $40-100/hr; LATAM nearshore $25-40/hr.
- **2026 one-time build benchmarks (n8n / general automation):**
  - Simple Zapier-style workflow: $300-1,000
  - One-time n8n workflow (typical): $200-1,500
  - Lead-routing automation: $700-2,500
  - CRM enrichment: $1,500-4,000
  - Document processing: $4,000-12,000
  - Production AI agent workflow: $8,000-25,000+
  - Simple 2-system integration w/ basic error handling: $5,000-10,000 (agency framing)
  - Complex multi-system + AI + conditional routing + compliance + monitoring: $25,000-50,000+
  - Zapier-to-n8n migration (~2 weeks): $5,000-15,000
- **Retainers:** individual/consultant $1,000-3,000/mo; agency $5,000-15,000/mo. HiresLink-style hour bundles: $700/mo for 10h, $1,200/mo for 20h, $2,000/mo for 40h (effective $50-70/hr).
- **Five price drivers (charge more as each rises):**
  1. **Technical depth** - Zapier-only is cheaper than API-heavy n8n, custom code, or LLM/agent workflows.
  2. **Business function / domain** - RevOps, finance, healthcare, legal need domain understanding and cost more.
  3. **Reliability / risk** - internal reporting is low-risk; anything touching payments, patient data, legal intake, or customer comms demands error handling, monitoring, and a premium.
  4. **Engagement model** - freelancer < nearshore < agency for the same scope.
  5. **Ownership level** - documentation, production monitoring, and training all add scope and price.
- **Platform cost is a pass-through, not the fee.** n8n Cloud is ~€24/mo (Starter, 2,500 executions) up to €800/mo (Business); self-hosted Community Edition is free software on a $3-7/mo server. Bill executions/infra to the client separately from your build fee.

## Recommendation
> For Dual Logic or a vendor pricing this work: lead with **per-workflow or fixed project pricing** off a short paid discovery, add a **monthly retainer** for monitoring and changes, and reserve **hourly** for discovery only. Anchor the number to the client's saved hours/cost (value), not your effort. Bill n8n hosting/executions as a pass-through. Push scope up (and price up) whenever integrations, risk/compliance, or ownership (docs, monitoring, training) increase.

## My angle
> Relevant to [[Dual Logic Platform]] delivery: this is the rubric for pricing our own automation deliverables and for briefing a subcontractor so their pricing aligns with how we scope and sell. Also a strong `/content` candidate for Joe CEO ("what automation work actually costs, and why hourly is the wrong lens").

## Open questions / gaps
- Is this a subcontractor we are hiring (so the doc sets what we will pay), or our own client-facing pricing (so the doc sets what we charge)? The framework serves both, but the "recommended number" differs.
- No hard data on Chris's own target margin or blended rate. Confirm before quoting a specific client.
- Rate ranges are US/marketplace aggregates from vendor blogs (directional, not a market survey). Treat as anchors, validate against 2-3 real quotes.

## Sources
| Source | Type | Key takeaway |
|--------|------|-------------|
| lowcode.agency / openhosst / goodspeed (n8n pricing 2026) | Vendor blogs | Platform cost: €24-€800/mo cloud, free self-hosted; executions-based |
| softhubtools / ritz7 / zyntohub (n8n earnings 2026) | Vendor blogs | Per-workflow $200-1,500; retainers $1,000-3,000/mo; agency $5,000-15,000/mo |
| hireslink.com (cost to hire AI automation consultants 2026) | Vendor blog | Hourly $80-150 US / $40-100 marketplace / $25-40 LATAM; complexity tiers; 5 price drivers |
| intuz.com (cost of workflow automation) | Vendor blog | Simple integration $5,000-10,000; complex + AI + compliance $25,000-50,000+ |

## Connections
- Project: [[Dual Logic Platform]]
- Topic: automation, pricing, n8n
- Handoff: https://docs.google.com/document/d/1l8idGSDdsVh1VdRTYrL78M11FVAezV_24vo9JlbsRD0/edit
