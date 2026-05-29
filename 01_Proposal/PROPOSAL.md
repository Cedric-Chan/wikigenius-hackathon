# WikiGenius — Project Proposal

**Team:** ChickenRice
**Hackathon Direction:** AI-Native Products & Operations
**Product:** WikiGenius

---

## Background

A backend engineer raises an API rate limit from 500 to 1000. The change is correct on its own. What she can't see: a decision doc Product archived three months ago that fixed the ceiling at 500 because anything higher breaks an SLA commitment. Nobody searches for what they don't know exists — so the team ships the contradiction and learns about it in production.

This is the defining failure of team knowledge today. Output cycles have compressed, work has gone async and globally distributed, and AI has multiplied how fast everyone produces — knowledge now scatters across tools, time zones, and people faster than any team can reconcile it. Docs go stale, ownership erodes, no one can say what's authoritative. Every existing tool treats this as a storage problem: better folders, better search, better autocomplete. But the real loss isn't "we couldn't find it" — it's "we didn't know it existed, and it contradicted what we just did." That's not a retrieval gap a search box closes. The bottleneck is no longer execution; it's **knowledge coherence**.

WikiGenius takes a different position. When an AI agent sits inside a team's knowledge layer, it doesn't just retrieve — it participates in setting what the team treats as true: what's current, what's superseded, who's accountable, and how disagreements get resolved. We aren't building a smarter wiki. We're building the layer that keeps a team's shared knowledge from contradicting itself.

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

## 应对信息膨胀：真值无损的知识压缩

### 问题

共享知识空间天然面临信息膨胀：事实不断被修订、决策被推翻、过时的 API 版本和废弃的流程文档持续堆积。传统 wiki 对此的应对是"保留所有版本"，结果是噪声淹没信号——用户无法快速判断"现在什么是对的"。

更根本的张力在于：删除旧信息会丢失历史上下文（"为什么这个决策后来被推翻了？"），保留全部信息则让知识图谱变成一个垃圾场。WikiGenius 需要在这两者之间找到一个平衡——**压缩噪声，但保留真值**。

### 思路

Team Agent 不只是写入新知识的引擎，它同样是**知识压缩的执行者**。当一条变更被接受时，Team Agent 在更新知识图谱的过程中同时执行以下判断：

1. **被取代检测** — 新事实是否使已有事实被取代？如果是，旧事实从"当前公认真值"降级为"已取代的历史事实"，保留在图谱中但不再参与当前一致性校验。
2. **冗余合并** — 多个节点是否表达了同一个事实的不同表述？如果是，合并为单一真值节点，原始表述作为引用子节点保留。
3. **粒度假缩** — 如果知识图谱的某个局部长期没有变更，Team Agent 以更粗的粒度对其进行逻辑概括（"这三年间 API 版本策略经历了 5 次迭代，当前策略为 X"），原始细节下沉到二级索引。

### 核心原则：真值无损

> 任何曾经是"真值"的事实，在压缩后必须可被完整恢复。

这和 Git 的核心理念一致（历史不可篡改），但粒度不同：Git 保护的是文本行级别的修改记录，WikiGenius 保护的是**语义事实级别的真值快照**。用户可以回问到"2025 年 Q4 时，团队对 API 版本策略的公认真值是怎样的？"，系统必须能从压缩后的知识图谱中重建那个时间点的真值状态。

### 技术挑战

- **自动判断被取代范围**：一条局部变更可能影响远端的多个事实节点——"API rate limit 提高到 1000"看似只改了一个数字，但它和被取代的 500 之间可能存在 SLA 承诺、成本估算、压测基准等多条边的逻辑依赖。Team Agent 需要自动识别被取代的边界，既不能漏（保留矛盾），也不能扩（误标记仍有效的事实）。
- **压缩阈值权衡**：过于激进会丢失细粒度可溯源性，过于保守则无法遏制膨胀。这需要一个可配置的压缩策略——可能在 Projects 层面更保守（活跃项目保持细粒度），在 Areas 和 Archives 层面更激进（稳定域和历史档案允许更大粒度假缩）。

---

*Grounded in research on transactive memory systems (Ren & Argote, 2011), the transactive systems model of collective intelligence (Gupta & Woolley, 2021), AI-mediated communication (Hancock et al., 2020), and human–AI trust (Glikson & Woolley, 2020). Full theory-to-design mapping and the 12 design constraints in [`02_Research/academic_foundation.md`](../02_Research/academic_foundation.md).*

*Last updated: 2026-05-29*
