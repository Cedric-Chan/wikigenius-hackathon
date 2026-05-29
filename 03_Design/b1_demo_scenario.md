# B1 — Demo Wedge Scenario (CONFIRMED, defaults locked 2026-05-29)

> **Status: CONFIRMED.** Built from the chosen directions (A cross-team contradiction + D shared-fact ripple + B truth time-travel), defaults locked. Drives Option 2 → demo script ([`../05_Demo/demo_script.md`](../05_Demo/demo_script.md)) + seed data ([`../05_Demo/seed_data.md`](../05_Demo/seed_data.md)).
>
> **Design goal of B1.** One coherent, realistic incident that showcases WikiGenius's core highlights and maps to a genuine multi-team pain — single narrative thread, not three stapled scenarios.

---

## 1. Setting

A payments / digital-wallet org with the classic large-team problem: **growth, product, and risk live in separate docs and rarely read each other's.** Three functions touch the same underlying "merchant onboarding" knowledge, each from their own angle:

- **BD / Growth** — owns the merchant **onboarding access threshold** doc.
- **Anti-fraud / Risk** — owns the **fraud strategy & policy facts** (why the thresholds exist).
- **Product (PM)** — owns the **onboarding-flow PRD**, which *assumes* those thresholds.

They all depend on **one shared fact**, copied and referenced across their docs — and that is exactly what breaks.

---

## 2. The shared fact (single source of truth)

> **FACT-ONBOARD-MIN:** "New merchants in high-risk categories must have ≥ **6 months** operating history + Tier-2 KYC before onboarding. Rationale: merchants below this bar show **4×** chargeback-fraud rate."

Referenced by three teams' documents:
| Team | Document | How it uses the fact |
|------|----------|----------------------|
| BD | Merchant Onboarding Threshold | sets the 6-month gate |
| Anti-fraud | Fraud Strategy Config + Policy | owns the rationale + the 4× evidence |
| Product | Onboarding-flow PRD | flow logic assumes the 6-month gate exists |

Its **provenance & history** (used in Beat 4):
- 2024-03: floor was **3 months** (early growth phase).
- 2025-08: raised to **6 months** after fraud incident **INC-2025-0814**.
- 2025-Q4: BD already tried lowering it once → **reverted** by Risk.

---

## 3. Cast

| Role | WikiGenius tier | In the story |
|------|-----------------|--------------|
| **Bella (BD manager)** | Member | Lowers the threshold to hit a growth target |
| **Adam (anti-fraud owner)** | Project Owner (Risk) | Owns FACT-ONBOARD-MIN and its rationale |
| **Priya (PM)** | Project Owner (Product) | Owns the PRD that assumes the threshold |
| **Rex (risk lead)** | Space Admin | Final arbitrator if they can't align |

---

## 4. The narrative arc (one incident, five beats)

**Beat 1 — The trigger (async, A).**
Bella, chasing a Q2 merchant-growth KPI, asks her User Agent to edit the Onboarding Threshold doc: minimum operating history **6 → 1 month**. She submits and leaves for a meeting. *(Showcases: async submission — submit and walk away.)*

**Beat 2 — The unprompted catch (A).**
The Team Agent's consistency check finds the change contradicts **FACT-ONBOARD-MIN** (anti-fraud's policy). It does **not** silently apply or silently reject. It **freezes only the affected section**, and pings **both Bella and Adam** in Lark IM, unprompted: *"This change collides with an anti-fraud policy — here's the conflict."* *(Showcases: cross-team semantic contradiction; the agent surfaces what no human knew to look for; section freeze; suggest-not-overwrite.)*

**Beat 3 — The ripple: it's not a local edit (D).**
WikiGenius shows the contradiction isn't one doc's problem: **FACT-ONBOARD-MIN is referenced by 3 teams** (BD, anti-fraud, PM PRD). Supersession-scope detection flags this as a **structural change to shared truth**, not a local update — so it clears a **higher bar** and pulls in every dependent owner. Priya (PM) is notified her PRD's assumption is about to break. *(Showcases: single-source-of-truth, supersession-scope detection — Proposal's "auto-bound what gets superseded"; impact-scope dimension; cross-team common understanding.)*

**Beat 4 — The "why": truth time-travel (B).**
Bella (or Adam) asks: *"Why is the floor 6 months — has it always been?"* WikiGenius **replays the fact's history**: 3mo (2024) → **6mo after incident INC-2025-0814 (2025-08)** → and *"BD tried lowering this in 2025-Q4; it was reverted by Risk."* Chesterton's fence with receipts. *(Showcases: truth-lossless time-travel — Graphiti bi-temporal; provenance; "what was true when, and who decided".)*

**Beat 5 — Negotiate, escalate, re-align (coordination protocol).**
Bella and Adam negotiate in-thread and reach a **conditional compromise**: lower to **3 months** **but** add enhanced monitoring + a lower initial transaction limit for <6-month merchants. If they can't agree, it **escalates to Rex (Space Admin)** per the permission chain. On resolution, the **single shared fact updates once**, all three teams' docs re-align automatically, the section unfreezes, and provenance records who decided and why. *(Showcases: async multi-party negotiation; escalation up the permission chain; accountability/provenance; the [`coordination_protocol.md`](coordination_protocol.md) state machine end-to-end.)*

---

## 5. User stories (each with real meaning)

- **BD:** *As a BD manager lowering the onboarding bar to hit a growth target, I want to be warned the instant my change collides with an anti-fraud policy I didn't know existed — and shown why it exists — so I don't trade one quarter of growth for a fraud incident.*
- **Anti-fraud:** *As the owner of a fraud-control threshold, I want to be pulled in automatically the moment anyone weakens it anywhere, so a hard-won control added after an incident is never silently undone.*
- **PM:** *As a PM whose onboarding flow assumes a threshold I don't own, I want to know the moment that assumption is about to change, so my PRD never silently drifts from reality.*

---

## 6. Without WikiGenius (the real pain this kills)

Today: Bella's change ships. BD and anti-fraud don't read each other's docs. The 6-month rationale is buried in an archived policy; nobody links it to BD's threshold doc or Priya's PRD. The reverted 2025-Q4 attempt is forgotten. Fraud rises weeks later; the post-mortem discovers the silent contradiction — and that the same mistake was made and reverted once before. **The loss isn't "we couldn't find it" — it's "nobody knew it existed and it contradicted what we just shipped."**

---

## 7. WikiGenius highlights demonstrated (coverage map)

| Highlight | Beat | Design doc |
|-----------|------|------------|
| Cross-document semantic contradiction | 2 | consistency core ([`../02_Research/tech_references.md`](../02_Research/tech_references.md)) |
| Agent surfaces unprompted | 2 | Proposal "Three Shifts" #2 |
| Section freeze (not whole-doc) | 2,5 | [`coordination_protocol.md`](coordination_protocol.md) §3 |
| Single source of truth + supersession-scope | 3 | Proposal truth-compression |
| Impact-scope (local vs structural) | 3 | Proposal Change Evaluation |
| Truth time-travel + provenance | 4 | tech_references §2 (Graphiti) |
| Async multi-party negotiation + escalation | 5 | [`coordination_protocol.md`](coordination_protocol.md) §2,§5,§6 |
| Accountability to a human role | 5 | constraint C10 |

---

## 8. Seed data (→ [`../05_Demo/seed_data.md`](../05_Demo/seed_data.md))

- **FACT-ONBOARD-MIN** node (6-month floor + 4× rationale) with its 3-step history (Beat 4).
- **3 referencing docs**: BD threshold doc, anti-fraud strategy/policy, PM onboarding PRD — all linked to the shared fact.
- The **2025-Q4 reverted attempt** as a superseded historical change.
- Roles/permissions: Bella=Member, Adam & Priya=Project Owners, Rex=Space Admin.
- The **planted contradiction**: Bella's pending 6→1 change.

---

## 9. Locked defaults (confirmed 2026-05-29)

| Item | Locked value |
|------|--------------|
| Domain framing | Generic payments / digital-wallet org |
| History floor | **6 → 1 month** (compromise lands at 3 months) |
| Fraud multiple | **4×** chargeback-fraud rate |
| Incident ref | **INC-2025-0814** (2025-08) |
| Beat-5 compromise | 3-month floor + enhanced monitoring + lower initial limit for <6mo merchants |
| Names | Bella (BD) / Adam (anti-fraud) / Priya (PM) / Rex (Space Admin) |
| **C concurrency beat** | **Excluded** from B1 (kept as a future beat) |

---

*Last updated: 2026-05-29*
