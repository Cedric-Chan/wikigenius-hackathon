# Demo Script — B1 golden path (~4 min)

> Beat-by-beat run-of-show for the B1 incident ([`../03_Design/b1_demo_scenario.md`](../03_Design/b1_demo_scenario.md)), on the seeded data ([`seed_data.md`](seed_data.md)). **One golden path. Everything else is a distraction.** The conflict gets *resolved on screen* (per demo discipline).

---

## Setup (before you start)

- **Seed loaded** ([`seed_data.md`](seed_data.md)): the shared fact + history, 3 referencing docs, the reverted 2025-Q4 attempt, roles. Only `CHG-DEMO-001` is processed live.
- **Two surfaces visible:**
  - **A — WikiGenius HTML dashboard** (beautiful-html-templates): graph view, "What the Team Agent is doing" feed, conflict timeline, "Why this?" panel, PARA node-count status.
  - **B — Lark IM** (where the agent pings land).
- **Backup video recorded** of this exact path.

---

## The golden path

| # | ~t | On screen | What happens | Narrator (talking point) |
|---|----|-----------|--------------|--------------------------|
| **0** | 0:00 | Dashboard: healthy graph, PARA counts | Set the stage | "One payments org. Growth, Product, Risk — three teams, separate docs, nobody reads each other's. Watch one routine edit." |
| **1** | 0:20 | Bella's User Agent (chat) | Bella: *"lower high-risk merchant onboarding to 1-month history"* → submits → **closes laptop** | "She's chasing a growth target, submits through her agent, and walks into a meeting. This is async — her agent carries it from here." |
| **2** 🦸 | 0:50 | Dashboard feed lights up → **Lark IM** ping to Bella **and** Adam | Team Agent runs the consistency check, finds the contradiction, **freezes only that section**, pings both — unprompted | "Nobody asked it to check. It found that her change contradicts an anti-fraud policy she never knew existed — and it froze just that section, not the doc. This is the wedge: not search, **coherence**." |
| **3** | 1:40 | Dashboard graph: the fact lights up with **3 inbound references** | Agent shows FACT-ONBOARD-MIN is referenced by BD + Anti-fraud + **PM's PRD** → flags **structural**, pulls in Priya | "It's not one doc's problem. The same fact is wired into three teams. So this isn't a local edit — it's a change to shared truth, and everyone who depends on it is now in the loop." |
| **4** | 2:20 | "Why this?" panel → **timeline** | Ask *"why 6 months?"* → replays: 3mo (2024) → **6mo after incident INC-2025-0814** → *"BD tried 6→3 in 2025-Q4; reverted by Risk"* | "Here's the part a wiki can't do: the **history of the truth**. Why the rule exists, and — the kicker — this exact change was tried before and reverted. Chesterton's fence, with receipts." |
| **5** | 3:00 | Lark IM thread → dashboard resolves | Bella + Adam negotiate in-thread → conditional compromise (**3mo + monitoring + lower initial limit**); (mention: deadlock → escalates to Rex) → **fact updates once, 3 docs re-align, section unfreezes**, provenance stamped | "They settle in the thread — or it escalates to the risk lead. One decision updates the single source of truth, all three docs re-align automatically, and the record shows who decided and why. Accountability stays with people." |
| **6** | 3:40 | Dashboard: green, graph consistent | Close | "A silent contradiction — and a repeat of a past mistake — caught before it shipped. That's WikiGenius: the team's consistency layer." |

🦸 **Hero moment = Beat 2** (the unprompted catch) reinforced by **Beat 4** (truth time-travel). If short on time, never cut these two.

---

## Talking points (what judges must remember)

1. **Not RAG, not a smarter wiki — a consistency layer.** It catches "we didn't know it existed and it contradicted what we just did."
2. **The agent surfaces, unprompted.** The biggest loss isn't failed search — it's not knowing you should search.
3. **Truth has history.** It can reconstruct what the team held true at any past point, and why (Graphiti bi-temporal).
4. **Coordination is the hard part, and it's shown** — freeze, cross-team negotiate, escalate, re-align — not just claimed.
5. **Humans stay accountable.** The agent suggests and routes; people decide; provenance records who.

---

## Failure drills / discipline

- If the live agent stalls on Beat 2 → cut to **backup video** of this path; keep narrating.
- Do not open other docs, other conflicts, or settings. One path.
- Q&A prep (esp. "why two agents not one?", "how is this not Notion AI?") → `qa_prep.md` (todo).

---

*Last updated: 2026-05-29*
