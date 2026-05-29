# WikiGenius — Project Proposal

**Team:** ChickenRice
**Hackathon Direction:** AI-Native Products & Operations
**Product:** WikiGenius

---

## Background

A backend engineer raises an API rate limit from 500 to 1000. The change is correct on its own. What she can't see: a decision doc Product archived three months ago that fixed the ceiling at 500 because anything higher breaks an SLA commitment. Nobody searches for what they don't know exists — so the team ships the contradiction and finds out in production.

This is the defining failure of team knowledge today. Output cycles have compressed, work has gone async and globally distributed, and AI has multiplied how fast everyone produces — knowledge now scatters across tools, time zones, and people faster than any team can reconcile it. Docs go stale, ownership erodes, no one can say what's authoritative. Every existing tool treats this as a storage problem: better folders, better search, better autocomplete. But the real loss isn't "we couldn't find it" — it's "we didn't know it existed, and it contradicted what we just did." A search box can't close that gap. The bottleneck is no longer execution; it's **knowledge coherence**.

Step back and the pattern is familiar: **every leap in productive force forces a new way of organizing work.** The steam engine produced the factory; the assembly line produced the modern firm. AI is the current leap — but so far it has been aimed almost entirely at individual output (faster drafting, cheaper search), while the *relations* around that output haven't moved. Teams still coordinate knowledge the way they did before their most productive new coworker was an agent: ownership, authority, and "what's true" are still negotiated by hand, out of band, too slowly. When the productive force shifts this much, the way people organize, share, and stay accountable for knowledge has to shift with it — and that new arrangement needs new infrastructure.

WikiGenius is a bet on that infrastructure. When an AI agent sits inside a team's knowledge layer, it doesn't just retrieve — it participates in setting what the team treats as true: what's current, what's superseded, who's accountable, and how disagreements get resolved. We aren't building a smarter wiki. We're building the coordination layer that keeps a team's shared knowledge coherent while AI accelerates everything around it.

---

## Three Shifts We're Betting On

1. **From documents to graph.** File trees encode parent–child paths; real knowledge is a web of references, dependencies, and contradictions. One decision radiates into requirements, API design, test strategy, and runbooks at once. WikiGenius organizes by knowledge's functional role — active Projects, ongoing Areas, reference Archives — not by folder path.
2. **From "people search" to "the agent surfaces."** The largest loss isn't failed search — it's not knowing you should search. WikiGenius runs continuous consistency scanning: the moment a change collides with an existing fact, the agent raises it, unprompted.
3. **From "who wrote what" to "what's true now."** Git answers who changed which line. The more valuable question in team knowledge is which version the team currently stands behind. WikiGenius shifts the core problem from version history to **truth maintenance**.

---

## What We're Building

WikiGenius is an AI-native team knowledge product built on a two-tier agent system. A **Team Wiki Agent** acts as the mega agent — owning the knowledge graph, managing access control, and continuously evaluating whether incoming changes stay consistent with existing knowledge. Each member operates through a personal **User Agent** that understands their role and working context, handles local queries, and escalates conflicts or gaps upward.

The split is deliberate: the User Agent augments the individual (assistive AI), while the Team Agent connects related work and diagnoses contradictions (coach and diagnostic AI). WikiGenius is not the team's memory — documents do that. It is not the team's brain — people do that. It's the team's **consistency layer**: the immune system that keeps shared knowledge from quietly contradicting itself.

---

## Knowledge Structure

Organised in three layers inspired by PARA and GitHub repo best practices:

- **Projects** — active or archived, each with an owner, lifecycle status, and optional cross-team membership. Contains Overview, README, Requirements, Decisions, Issues & Changes, and Resources.
- **Areas** — ongoing functional domains (e.g. Engineering Standards, Risk Policy) with role-based permissions, never archived.
- **Resources & Archives** — cross-project reference knowledge and read-only historical records.

---

## How Knowledge Enters: Digest, Don't Pile

A wiki that appends every submission verbatim becomes a landfill, and a landfill costs more to maintain than it's worth. So WikiGenius treats documents as **living knowledge containers**, not inboxes. When raw input arrives — an article, a log, a decision, a chat thread — the User Agent **digests** it into the graph in three moves:

1. **Decompose** — break the input into atomic claims, one assertion each, so every piece can be judged and placed on its own.
2. **Match** — for each claim, find where it already lives in the knowledge graph: the node it enriches, the fact it updates, or the existing claim it contradicts.
3. **Merge** — fold the claim into that node to enrich what's there. A new node is created *only* when nothing fits.

A merge is a **proposed change, not a write** — it flows into the same three-dimensional evaluation every change faces (consistency, authority, impact scope; below). Decompose-Match-Merge is the *ingestion* half of that pipeline, not a parallel system: by the time a claim reaches evaluation, the Match step has already found its neighborhood and flagged whether it collides with anything, which is exactly what the consistency check needs.

The discipline throughout is **restraint** — keep the core knowledge and the context needed to act on it, drop the rest. This is the write-time half of fighting knowledge bloat; truth-lossless compression (below) is the maintenance-time half. Together they keep the graph small enough to stay trustworthy, with knowledge filed by what it's *for* (its PARA layer), not by who submitted it.

---

## Core Interaction Flow

User Agents accept both natural language input and file uploads (logs, notebooks, etc.) with user-declared context. Queries are handled synchronously; change submissions are async — the Team Agent evaluates in the background and notifies the User Agent when resolved. A member can submit a change, close the laptop, and let their agent carry the negotiation forward.

When a conflict is detected, both parties are notified and asked to align. If they agree, the Team Agent updates the doc. If not, a ticket is created and assigned up the permission chain. During this period, only the affected section enters a frozen state — the rest of the document remains fully readable and writable. Once resolved, queued writes are re-evaluated and the section is unfrozen.

---

## Permission Model

Three tiers:

| Role | Scope |
|------|-------|
| Space Admin | Governs Areas, Resources, Archives; final arbitrator for unresolved conflicts |
| Project Owner | Governs their Project and all content within it |
| Member | Submits changes via User Agent for Team Agent evaluation |

Cross-team conflicts escalate to all relevant Project Owners, then to Space Admin if unresolved. Permission tiers are not just access control — they answer "if this turns out wrong, who is accountable?" with a specific human role, never "the agent."

---

## Change Evaluation Criteria

When a User Agent submits a change, the Team Agent evaluates across three dimensions:

1. **Consistency** — semantic and logical conflict check against existing knowledge.
2. **Authority** — whether the submitter's role has write permission for that section.
3. **Impact scope** — local update vs. structural change (higher threshold for the latter).

The Team Agent suggests and routes; it does not silently overwrite a human's work. Reversible decisions are one click to undo; irreversible ones (like supersession) require explicit confirmation. Authorship and accountability stay with people.

---

## Fighting Information Bloat: Truth-Lossless Compression

### The problem
A shared knowledge space bloats by nature: facts get revised, decisions get reversed, dead API versions and abandoned process docs pile up. The traditional wiki answer — "keep every version" — buries signal under noise, and no one can tell what's true *now*.

The deeper tension: deleting old information loses the context for *why* ("why was this decision reversed?"), but keeping everything turns the knowledge graph into a junkyard. WikiGenius has to sit between the two — **compress the noise, preserve the truth.**

### The approach
The Team Agent isn't only an engine for writing new knowledge; it's the agent of compression. When a change is accepted, while updating the graph it also runs three judgments:

1. **Supersession detection** — does the new fact retire an existing one? If so, the old fact is demoted from "current accepted truth" to "superseded historical fact": kept in the graph, but no longer part of live consistency checks.
2. **Redundancy merge** — do multiple nodes state the same fact in different words? Merge them into a single truth node, keeping the original phrasings as cited children.
3. **Granularity abstraction** — has a region of the graph gone untouched for a long time? The Team Agent summarizes it at a coarser grain ("over three years the API-versioning policy iterated five times; current policy is X"), with the original detail demoted to a secondary index.

### The core principle: truth-lossless
> Any fact that was ever "truth" must be fully recoverable after compression.

This shares Git's spirit — history is immutable — but works at a different grain: Git protects line-level edits; WikiGenius protects **semantic truth snapshots**. A member can ask "what did the team hold as true about the API-versioning policy in Q4 2025?" and the system must reconstruct that point-in-time truth from the compressed graph.

### Technical challenge
- **Bounding what gets superseded.** One local change can ripple to distant nodes — "raise the API rate limit to 1000" looks like one number, but the retired 500 may be wired by edges to SLA commitments, cost estimates, and load-test baselines. The Team Agent has to find the supersession boundary precisely: not too narrow (leaving contradictions), not too wide (flagging still-valid facts as dead).
- **Compression threshold.** Too aggressive loses fine-grained traceability; too conservative fails to curb bloat. This needs a configurable policy — likely conservative in Projects (active work stays fine-grained) and more aggressive in Areas and Archives (stable domains and history tolerate coarser abstraction).

---

## The Hard Problem

The core technical challenge is the multi-agent coordination protocol: when does a User Agent act locally, when does it escalate, and how does the Team Agent arbitrate conflicting updates from multiple users at once — keeping the knowledge graph coherent as the team scales. This is the part with no off-the-shelf answer, and it's where we'll spend our depth.

---

## Where This Goes

The first version keeps one team's knowledge coherent. The direction is larger. As AI agents become standing coworkers rather than occasional tools, a team's knowledge layer stops being a filing cabinet and becomes the surface where humans and agents actually coordinate — where they propose, contest, and agree on what's true. WikiGenius is built for that world: not a place to store what a team knew, but the infrastructure for how an AI-era team keeps knowing together. Get the coordination layer right, and docs, search, and dashboards become commodities sitting on top of it.

---

*Grounded in research on transactive memory systems (Ren & Argote, 2011), the transactive systems model of collective intelligence (Gupta & Woolley, 2021), AI-mediated communication (Hancock et al., 2020), and human–AI trust (Glikson & Woolley, 2020). Full theory-to-design mapping and the 12 design constraints in [`02_Research/academic_foundation.md`](../02_Research/academic_foundation.md).*

*Last updated: 2026-05-29*
