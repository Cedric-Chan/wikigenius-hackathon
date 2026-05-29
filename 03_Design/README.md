# 03 — Design

Product spec, system architecture, and agent protocol design live here.

> **Start here:** [`design_readiness.md`](design_readiness.md) — what must be decided before/early in the design phase (🔴 blocking decisions + 🟡 design inputs).

## Current design docs

| File | Description |
|------|-------------|
| [`design_readiness.md`](design_readiness.md) | Blocking decisions + design inputs, with live progress status. |
| [`ingest_pipeline.md`](ingest_pipeline.md) | **"Digest, don't pile"** — Decompose→Match→Merge as the *front half* of the change pipeline (User Agent ingestion → existing 3-dim evaluation), graph-grounded Match, agent-behavior `+` ops, native promotion gate (answers D2). |
| [`lark_wiki_mvp.md`](lark_wiki_mvp.md) | Lark Wiki as carrier: concept→Lark-primitive mapping with **real lark-cli v1.0.43 commands**, permission mapping, two-tier agent flow, hackathon MVP shape (answers B3). |

## Suggested contents

- `product_spec.md` — features, user stories, acceptance criteria, non-goals
- `ux_flows.md` — key user journeys (query, submit change, conflict resolution, escalation)
- `system_architecture.md` — services, data flow, deployment shape
- `agent_protocol.md` — User Agent ↔ Team Agent contract; local-vs-escalate decision rules; conflict arbitration
- `data_model.md` — knowledge graph schema, Projects/Areas/Resources/Archives, permissions table
- `wireframes/` — sketches, mockups, screenshots

## Loose questions to answer here

- What's the exact JSON shape of a change submission, and what fields does the Team Agent need to evaluate it?
- How is the "frozen section" boundary defined — by heading, by semantic block, by edit range?
- What's the fallback when the Team Agent itself is uncertain (e.g., the change is plausible but ambiguous)?
- How does a User Agent learn its user's role and working context without manual setup?
