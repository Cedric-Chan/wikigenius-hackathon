# WikiGenius — Project Proposal

**Team:** ChickenRice
**Hackathon Direction:** AI-Native Products & Operations
**Product:** WikiGenius

---

## Background

The way teams work is changing fast. Global distribution, async collaboration, and AI-driven productivity have compressed output cycles while scattering knowledge across tools, time zones, and people. The result: docs go stale, ownership breaks down, and no one knows what's authoritative. The bottleneck is no longer execution — it's knowledge coherence.

We believe the AI era demands a fundamentally different approach to how teams manage information. Productivity reshapes structure: when knowledge flows reliably, teams coordinate at a different speed.

---

## What We're Building

WikiGenius is an AI-native team knowledge product built around a two-tier agent system. A **Team Wiki Agent** acts as the mega agent, owning the knowledge graph, managing access control, and continuously evaluating whether incoming changes are consistent with existing docs. Each team member operates through a personal **User Agent** that understands their role and working context, handles local queries, and escalates conflicts or gaps up to the Team Agent.

---

## Knowledge Structure

Organised in three layers inspired by PARA and GitHub repo best practices:

- **Projects** — active or archived, each with an owner, lifecycle status, and optional cross-team membership. Contains Overview, README, Requirements, Decisions, Issues & Changes, and Resources.
- **Areas** — ongoing functional domains (e.g. Engineering Standards, Risk Policy) with role-based permissions, never archived.
- **Resources & Archives** — cross-project reference knowledge and read-only historical records.

---

## Core Interaction Flow

User Agents accept both natural language input and file uploads (logs, notebooks, etc.) with user-declared context. Queries are handled synchronously; change submissions are async — the Team Agent evaluates in the background and notifies the User Agent when resolved.

When a conflict is detected, both parties are notified and asked to align. If they agree, the Team Agent updates the doc. If not, a ticket is created and assigned up the permission chain. During this period, only the affected section enters a frozen state — the rest of the document remains fully readable and writable. Once resolved, queued writes are re-evaluated and the section is unfrozen.

---

## Permission Model

Three tiers:

| Role | Scope |
|------|-------|
| Space Admin | Governs Areas, Resources, Archives; final arbitrator for unresolved conflicts |
| Project Owner | Governs their Project and all content within it |
| Member | Submits changes via User Agent for Team Agent evaluation |

Cross-team conflicts escalate to all relevant Project Owners, then to Space Admin if unresolved.

---

## Change Evaluation Criteria

When a User Agent submits a change, the Team Agent evaluates across three dimensions:

1. **Consistency** — semantic and logical conflict check against existing docs
2. **Authority** — whether the submitter's role has write permission for that section
3. **Impact scope** — local update vs. structural change (higher threshold for the latter)

---

## The Hard Problem

The core technical challenge is the multi-agent coordination protocol: when does a User Agent act locally, when does it escalate, and how does the Team Agent arbitrate conflicting updates from multiple users simultaneously — keeping the knowledge graph coherent as the team scales.

---

*Last updated: 2026-05-28*
