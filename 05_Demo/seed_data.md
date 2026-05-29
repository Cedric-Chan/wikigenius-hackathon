# Demo Seed Data — B1 fixtures

> **What this is.** The exact content to preload before the demo, so the live run only has to process **one** new change (Bella's 6→1). Everything else — the shared fact, its history, the 3 referencing docs, the reverted attempt, roles — is seeded.
>
> Scenario source: [`../03_Design/b1_demo_scenario.md`](../03_Design/b1_demo_scenario.md). Schemas align with [`../03_Design/ingest_pipeline.md`](../03_Design/ingest_pipeline.md) (claims), [`../03_Design/coordination_protocol.md`](../03_Design/coordination_protocol.md) (change-rows), and [`../04_Build/experiments/graphiti_spike.md`](../04_Build/experiments/graphiti_spike.md) (bi-temporal episodes).
>
> All data is **synthetic**.

---

## 1. Space & PARA node tree (Lark Wiki)

```
Knowledge Space: "PayWallet Team"
├── Projects/
│   ├── Growth/        → DOC-BD-THRESHOLD     (owner: Bella's team; Project Owner approves)
│   └── Product/       → DOC-PM-PRD           (owner: Priya)
├── Areas/
│   └── Risk-Policy/   → DOC-AF-POLICY        (owner: Adam; never archived)
└── Archives/
    └── Incidents/     → DOC-INC-2025-0814    (read-only history)
```

## 2. Roles / permissions

| Person | Role (tier) | Scope |
|--------|-------------|-------|
| Bella | Member | submits changes via User Agent |
| Adam | Project Owner — Risk-Policy area | owns FACT-ONBOARD-MIN |
| Priya | Project Owner — Product | owns the PRD |
| Rex | Space Admin | final arbitrator |

---

## 3. Knowledge-graph facts (bi-temporal; Graphiti episodes)

| id | claim | valid_at | invalid_at | provenance |
|----|-------|----------|-----------|------------|
| `FACT-ONBOARD-MIN@v0` | High-risk new merchants need ≥ **3 months** history + Tier-2 KYC | 2024-03-01 | **2025-08-14** (superseded) | human:bd-2024, src:DOC-BD-THRESHOLD |
| `FACT-ONBOARD-MIN@v1` | High-risk new merchants need ≥ **6 months** history + Tier-2 KYC | 2025-08-14 | *(current)* | human:adam, src:INC-2025-0814 |
| `FACT-FRAUD-4X` | Merchants below the history floor show **4× chargeback-fraud** rate | 2025-08-14 | *(current)* | human:adam, src:INC-2025-0814 |
| `INC-2025-0814` | Fraud incident: under-seasoned high-risk merchants drove a chargeback spike | 2025-08-10 | — | archive |

**Edges:** `FACT-ONBOARD-MIN@v1 —supersedes→ @v0`; `@v1 —justified_by→ FACT-FRAUD-4X`; `FACT-FRAUD-4X —derived_from→ INC-2025-0814`; `@v1 —referenced_by→ {DOC-BD-THRESHOLD, DOC-AF-POLICY, DOC-PM-PRD}`.

---

## 4. Documents (each a Lark Doc; references the shared fact)

- **DOC-BD-THRESHOLD** (Growth) — "Merchant Onboarding Threshold": *"High-risk category merchants: minimum **6 months** operating history (ref FACT-ONBOARD-MIN)."*
- **DOC-AF-POLICY** (Risk-Policy) — "Fraud Strategy & Onboarding Policy": owns FACT-ONBOARD-MIN + the 4× evidence + link to INC-2025-0814.
- **DOC-PM-PRD** (Product) — "Onboarding Flow PRD": flow step *"if operating_history < threshold(FACT-ONBOARD-MIN) → route to manual review."* (assumes the gate exists)
- **DOC-INC-2025-0814** (Archives) — the incident write-up.

---

## 5. Change board (coordination_protocol Base table)

| change_id | node_id | proposed | submitter | status | parent | provenance | when |
|-----------|---------|----------|-----------|--------|--------|-----------|------|
| `CHG-2025Q4-001` | FACT-ONBOARD-MIN | 6 → 3 months | Bella | **rejected** (reverted by Risk) | — | human:bella, decided:adam | 2025-11-20 |
| `CHG-DEMO-001` | FACT-ONBOARD-MIN | **6 → 1 month** | Bella | **submitted** ← live trigger | — | agent-assisted:bella | demo t0 |

> `CHG-2025Q4-001` is the **"this was tried before and reverted"** beat (Beat 4). `CHG-DEMO-001` is the only thing processed live.

---

## 6. The planted contradiction (what makes the demo fire)

`CHG-DEMO-001` lowers the floor to 1 month → directly contradicts `FACT-ONBOARD-MIN@v1` (6 months) and undercuts `FACT-FRAUD-4X`. Because `@v1` is `referenced_by` 3 docs, the change is **structural** (Beat 3), not local. This is the single fact that, when processed live, triggers Beats 2→5.

---

## 7. Minimal vs full seed

- **Minimal (must-have for the golden path):** roles, `FACT-ONBOARD-MIN@v0/@v1`, `FACT-FRAUD-4X`, 3 referencing docs, `CHG-2025Q4-001`, `CHG-DEMO-001`.
- **Nice-to-have:** `INC-2025-0814` doc body, extra unrelated nodes to make the graph view look real.

---

*Last updated: 2026-05-29*
