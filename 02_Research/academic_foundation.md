# Academic Foundation: WikiGenius Design × Organizational Communication Theory

**Purpose.** This document consolidates the scholarly foundation for WikiGenius — a two-tier AI agent system for team knowledge management. It is organized in two parts:

- **Part I — Literature Map:** Maps WikiGenius's design decisions to established theoretical anchors in organizational communication, coordination, transactive memory, AI-mediated communication, and human–AI trust.
- **Part II — Design Constraints:** Extracts 12 actionable constraints the literature imposes on WikiGenius's design, each with a concrete test and failure mode.

**Scope.** Eight peer-reviewed articles: five from *Academy of Management Annals*, one from *Organization Studies*, one from *New Media & Society*, one from *Journal of Computer-Mediated Communication*, and one from *Proceedings of the Human Factors and Ergonomics Society Annual Meeting* (with its 2023 *Topics in Cognitive Science* extension noted).

**如何阅读.** 中文读者可先看 [`academic_takeaways_zh.md`](academic_takeaways_zh.md) 获取快速摘要，再回到本文阅读完整论证。

---

# Part I — Literature Map

## I.1 Research Significance

The dominant framing of "AI at work" in trade discourse treats AI as a tool that increases individual productivity — better autocomplete, faster drafting, cheaper search. WikiGenius takes a different position: when AI agents are introduced into the team's knowledge layer, they do not merely amplify existing roles. They participate in the **constitution** of the team itself — who knows what, who is accountable for what, what counts as the team's shared "truth", and how disagreements are resolved.

This framing connects WikiGenius directly to five converging streams:

- **The CCO (Communicative Constitution of Organization) perspective** argues that organizations are produced *in* communication rather than serving as containers within which communication happens. Schoeneborn, Kuhn, and Kärreman (2019) summarize this as the proposition that "*organization happens in communication*" (p. 476, citing Cooren, Bartels, & Martine, 2017). They further note that "an array of participants — human as well as nonhuman — engage" in the practices that constitute organizational meaning (p. 476). WikiGenius's Team Agent is, in this sense, not infrastructure for the organization but a *constitutive actor* in it.

- **The transactive memory systems (TMS) literature** provides the canonical account of how teams encode "who knows what" as a collective resource. Ren and Argote (2011) define a TMS as "a shared system that people in relationships develop for encoding, storing, and retrieving information about different substantive domains" (p. 191), with three transactive processes — directory updating, information allocation, and retrieval coordination. They close with an explicit call: Web 2.0 technologies such as wikis "have the potential to automatically populate directories of who knows what" (p. 218), but "[w]hether the opportunities are realized depends on how the tools are used, a topic on which additional research is needed" (p. 219). WikiGenius is a structural answer to that open call.

- **The transactive systems model of collective intelligence (TSM-CI)** extends TMS into the human–AI domain. Gupta and Woolley (2021), elaborated by Gupta, Nguyen, Gonzalez, and Woolley (2023), articulate three systems — transactive memory, transactive attention, and transactive reasoning — and identify three roles for AI: *Assistive AI* (augmenting individual capability), *Coach AI* (nudging collaboration behaviours), and *Diagnostic AI* (monitoring collective process).

- **The AI-Mediated Communication (AI-MC) framework** defines a new mode of interpersonal communication in which "*an intelligent agent operates on behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication goals*" (Hancock, Naaman, & Levy, 2020, p. 89). WikiGenius's User Agent is a textbook instance of AI-MC operating at organizational scale.

- **The coordination literature** identifies three integrating conditions — accountability, predictability, and common understanding — through which interdependent work becomes coherent (Okhuysen & Bechky, 2009). WikiGenius's permission tiers, conflict arbitration protocol, and knowledge-graph-as-shared-truth map cleanly onto these three conditions.

- **Trust in AI** is what determines whether such mechanisms are accepted. Glikson and Woolley (2020) distinguish cognitive trust — driven by "AI's tangibility, transparency, reliability, and immediacy behaviors" (p. 627) — from emotional trust, which additionally depends on anthropomorphism.

The contribution WikiGenius can claim is not "another AI knowledge tool" but a working instance of how *production relations inside a team are reshaped when communicative AI becomes a co-constitutive participant in the team's knowledge work*.

---

## I.2 Design ↔ Theory Cross-Check Matrix

| # | WikiGenius design decision | Primary anchor(s) | What the anchor supports | What it does NOT support |
|---|---|---|---|---|
| D1 | Two-tier agent system (User Agent + Team Agent) | Gupta & Woolley, 2021; Hancock et al., 2020; Csaszar & Steinberger, 2022 | Separating an agent that *operates on behalf of an individual communicator* (Hancock) from one that performs organization-level *aggregation and representation* (Csaszar); the TSM-CI framework's distinction between individual-augmenting and collective-augmenting AI roles (Gupta & Woolley). | The specific number of tiers or the particular hand-off protocol. |
| D2 | Knowledge graph as the single source of truth | Ren & Argote, 2011; Csaszar & Steinberger, 2022; Schoeneborn et al., 2019 | Treating the team's knowledge representation as a first-class organizational artifact — a "retention bin or knowledge repository" (Ren & Argote, 2011, p. 193); as one of the three "fundamental processes in organizations" (Csaszar); as an "authoritative text" (Schoeneborn). | Any particular schema or storage format. |
| D3 | User Agent as personalized communication mediator | Hancock et al., 2020; Guzman & Lewis, 2020 | The agent's intermediary role: modifies/augments/generates messages on behalf of the user (Hancock); is interpreted as a "communicative subject" rather than a tool (Guzman). | The agent's specific NLP capabilities. |
| D4 | Team Agent as autonomous arbiter / consistency keeper | Schoeneborn et al., 2019; Gupta & Woolley, 2021; Guzman & Lewis, 2020 | Nonhuman agency as constitutive of organization (Schoeneborn); the Coach AI and Diagnostic AI roles that "nudge coordination behaviors" and "monitor collective effort, strategy, and skill use" (Gupta & Woolley, 2021, Fig. 2); machines as communicators that automate communication and dependent social processes (Guzman). | The legitimacy of any specific arbitration rule — empirical justification still required. |
| D5 | Permission tiers (Admin / Project Owner / Member) | Okhuysen & Bechky, 2009; Schoeneborn et al., 2019 | Accountability as the integrating condition that "addresses the question of who is responsible for specific elements of the task" (Okhuysen & Bechky, 2009, p. 483); authority deriving from the authoritative text (Schoeneborn). | The specific three-tier design. |
| D6 | Conflict arbitration (frozen sections, escalation) | Okhuysen & Bechky, 2009 | The integration of common understanding, predictability, and accountability through which coordination is accomplished. | Any particular UX of escalation. |
| D7 | Truth-lossless compression / supersession / history reconstruction | Ren & Argote, 2011; Csaszar & Steinberger, 2022 | The structural component of TMS as a knowledge directory distinct from individual memories (Ren & Argote); representation as one of the three "fundamental processes in organizations" (Csaszar). | Specific deduplication or versioning algorithms. |
| D8 | Trust and acceptance of Team Agent decisions | Glikson & Woolley, 2020 | The cognitive-trust dimensions (tangibility, transparency, reliability, task characteristics, immediacy behaviors) the Team Agent must satisfy. | Quantitative thresholds — these are empirical questions left open. |
| D9 | Async multi-agent coordination (Team Agent monitoring across users) | Gupta & Woolley, 2021 | The Transactive Attention System (TAS) account of how collectives "signal and update attentional priorities" (Gupta & Woolley, 2021, p. 672) and exhibit "burstiness" — alternating periods of independent and synchronous work. | The specific notification UX or polling cadence. |

---

## I.3 Anchor Stream Overview

**Stream A — Organization theory × AI (Csaszar & Steinberger, 2022).** Reads "the organization itself as a kind of AI", arguing that the OT canon has long borrowed from AI ideas — search, representation, aggregation — without acknowledging it. Useful for framing WikiGenius's *system-level* design as itself an information-processing architecture.

**Stream B — Communicative Constitution of Organization (Schoeneborn, Kuhn, & Kärreman, 2019).** A perspective paper synthesizing a decade of CCO work. Crucial for theorizing the Team Agent as a participant in organizational constitution.

**Stream C — Coordination (Okhuysen & Bechky, 2009).** The canonical *Annals* review of how interdependent work becomes coherent. Provides the three integrating conditions used as a checklist against which WikiGenius's coordination affordances are evaluated.

**Stream D — AI-mediated and human–machine communication (Hancock et al., 2020; Guzman & Lewis, 2020).** Two complementary research agendas covering the *individual interaction layer* of WikiGenius.

**Stream E — Trust in AI (Glikson & Woolley, 2020).** The *Annals* synthesis of empirical work on human trust in AI. Provides the dimensions WikiGenius must design against.

**Stream F — Transactive memory systems and the TSM-CI extension to AI (Ren & Argote, 2011; Gupta & Woolley, 2021; Gupta et al., 2023).** The most directly relevant stream. Ren and Argote provide the canonical TMS framework; Gupta and Woolley build the human–AI extension. WikiGenius can be positioned as a working implementation of the agenda these papers articulate.

---

## I.4 Anchor Cards

### Card A — Csaszar & Steinberger (2022)

**Citation.** Csaszar, F. A., & Steinberger, T. (2022). Organizations as artificial intelligences: The use of artificial intelligence analogies in organization theory. *Academy of Management Annals*, 16(1), 1–37.

**Core claim.** Over 100 organization-theory works depend on AI ideas, grouped into "10 AI approaches that speak to three fundamental processes in organizations: search, representation, and aggregation" (p. 1). The paper argues that the popular framing of AI as merely lowering the "cost of making predictions" misses its effect on "the type of knowledge the organization can represent and on the organization's search and aggregation processes" (p. 2).

**Why it matters.** WikiGenius is a *representation and aggregation* system. Csaszar and Steinberger's three-process scheme gives a defensible vocabulary for what the Team Agent does at the system level.

**Maps to design decisions.** D1, D2, D7.

### Card B — Glikson & Woolley (2020)

**Citation.** Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660.

**Core claim.** The review proposes a framework distinguishing cognitive trust — shaped by "AI's tangibility, transparency, reliability, and immediacy behaviors" (p. 627) — from emotional trust, additionally shaped by anthropomorphism.

**Why it matters.** Whether members accept Team Agent decisions is a function of how trust is *designed*:

- **Tangibility** — the agent's presence must be visible in the UI.
- **Transparency** — its reasoning for arbitration outcomes must be inspectable.
- **Reliability** — its behaviour must be consistent over time.
- **Task characteristics** — its scope of authority must match what users believe it is qualified to decide.
- **Immediacy behaviors** — its responsiveness and acknowledgement of user input matter.

**Maps to design decisions.** D8 primarily; also D4 (Team Agent as arbiter).

### Card C — Guzman & Lewis (2020)

**Citation.** Guzman, A. L., & Lewis, S. C. (2020). Artificial intelligence and communication: A Human–Machine Communication research agenda. *New Media & Society*, 22(1), 70–86.

**Core claim.** AI does not "fit neatly into paradigms of communication theory that have long focused on human–human communication" (p. 70). The HMC approach treats AI as a *communicative subject* — not a mere channel — along three dimensions: functional, relational, and metaphysical.

**Why it matters.** The Team Agent is an entity users *talk to* and that talks back, makes judgments, and intervenes. Guzman and Lewis's framework licenses the move to theorize the Team Agent as a communicative subject.

**Maps to design decisions.** D3, D4.

### Card D — Hancock, Naaman, & Levy (2020)

**Citation.** Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100.

**Core claim.** AI-MC is "interpersonal communication in which an intelligent agent operates on behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication goals" (p. 89). Three characterizing dimensions: *magnitude*, *media type*, and *optimization goal*.

**Why it matters.** WikiGenius's User Agent is an AI-MC system at organizational scale, raising the agency question — *who* is accountable for a contribution that has been agent-modified? WikiGenius's answer (the human author remains accountable) is a defensible position, not a settled fact.

**Maps to design decisions.** D1, D3.

### Card E — Okhuysen & Bechky (2009)

**Citation.** Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502.

**Core claim.** Coordination is "the process of interaction that integrates a collective set of interdependent tasks" (p. 463). Three *integrating conditions*:

- **Accountability** "addresses the question of who is responsible for specific elements of the task" (p. 483).
- **Predictability** "enables interdependent parties to anticipate subsequent task related activity by knowing what the elements of the task are and when they happen" (p. 486).
- **Common understanding** provides a shared perspective on how the work fits together (p. 487).

**Why it matters.** Direct mapping to WikiGenius:
- *Accountability* ↔ permission tiers + author attribution (D5).
- *Predictability* ↔ async notifications + frozen-section signals (D6).
- *Common understanding* ↔ knowledge graph + Team Agent consistency enforcement (D2, D6).

**Maps to design decisions.** D5, D6 (primary); D2 (common understanding).

### Card F — Schoeneborn, Kuhn, & Kärreman (2019)

**Citation.** Schoeneborn, D., Kuhn, T. R., & Kärreman, D. (2019). The communicative constitution of organization, organizing, and organizationality. *Organization Studies*, 40(4), 475–496.

**Core claim.** The CCO perspective asks "how organization happens in communication" (p. 476). Meaning resides "in the practices in which an array of participants — human as well as nonhuman — engage" (p. 476).

**Why it matters.** This is the most ambitious anchor. If the Team Agent participates in the communicative practices that constitute the team's knowledge truth, it is not infrastructure — it is part of how the team comes into being as an organization. Two implications:
1. Team Agent design decisions are constitutive choices about what kind of organization is being produced.
2. Teams using WikiGenius exhibit different *degrees of organizationality* depending on how the agents are configured.

**Maps to design decisions.** D2, D4, D5.

### Card G — Ren & Argote (2011)

**Citation.** Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229.

**Core claim.** Reviewing 76 papers, the authors define a TMS as "a shared system that people in relationships develop for encoding, storing, and retrieving information about different substantive domains" (p. 191). Two components: a *structural* component (directory of who knows what) and three *transactive processes* — directory updating, information allocation, retrieval coordination (p. 192).

They close with an open call: "the communication capabilities afforded by Web 2.0 technologies such as wikis... have the potential to automatically populate directories of who knows what... Whether the opportunities are realized depends on how the tools are used, a topic on which additional research is needed" (pp. 218–219).

**Why it matters.** WikiGenius's knowledge graph *is* the structural component; the User Agent + Team Agent system operationalises the three transactive processes computationally. The three behavioral indicators (specialization, credibility, coordination) provide a research-grade evaluation frame.

**Maps to design decisions.** D2, D7, D1.

### Card H — Gupta & Woolley (2021), with extension Gupta et al. (2023)

**Citation.** Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674. Extended in Gupta, P., Nguyen, T. N., Gonzalez, C., & Woolley, A. W. (2023). Fostering collective intelligence in human–AI collaboration: Laying the groundwork for COHUMAIN. *Topics in Cognitive Science*, 17(2), 189–216.

**Core claim.** The TSM-CI framework articulates three transactive systems — memory, attention, and reasoning — and three AI roles:

- **Assistive AI** — "augments individuals' production capabilities".
- **Coach AI** — "predicts and nudges coordination behaviors". The paper notes that "some new tools enhance [transactive memory] by sensing the content of one member's work and proactively alerting them to related information team members might have" (p. 673).
- **Diagnostic AI** — "monitors collective effort, strategy, and skill use".

**Why it matters.** Mapping to WikiGenius is clean:
- **User Agent** = Assistive AI (augmenting individual contribution).
- **Team Agent** = Coach AI + Diagnostic AI (connecting work, monitoring consistency, surfacing conflicts).
- **Knowledge graph** = TMS directory; **conflict arbitration** = TRS; **async notifications + frozen sections** = TAS mechanisms.

Two cautions:
1. "supplying too many connections could easily lead to overload" (p. 673) → bounds suggestion volume.
2. "Systems that would deprive workers of their autonomy... can undermine their sense of internal motivation" (p. 674) → bounds arbitration scope.

**Maps to design decisions.** D1, D4, D9; also imposes design constraints on D4 and D6.

---

## I.5 Reverse Check — Unsupported Design Decisions

| Design feature | Status | Notes |
|---|---|---|
| Two-tier agent system | Well-supported — Gupta & Woolley's TSM-CI provides the framework; Hancock and Csaszar each support one tier. | |
| Knowledge graph as truth | Well-supported — Ren & Argote, Csaszar, Schoeneborn triangulate. | |
| Truth-lossless compression / supersession | Adequately supported — Ren & Argote's structural/transactive distinction maps to the design. | |
| Permission tiers (3-tier design) | Principle well-supported by Okhuysen & Bechky; specific design is an engineering choice. | Design choices need not be theoretically derived, only defensible. |
| Quantitative trust thresholds | Not supported — Glikson & Woolley give dimensions but not thresholds. | Empirical question, not a literature gap. |

---

## I.6 How to Use Part I

**For the proposal's "Background and Motivation":**
- Open with the Section I.1 paragraph (production relations and constitutive participation).
- Lead with Ren & Argote (2011) and Gupta & Woolley (2021/2023) as central anchors.
- For each design decision, cite the primary anchor from the Section I.2 matrix.

**For the proposal's "Related Work":**
- Use Section I.3 to organize the streams.
- Stream F (TMS + TSM-CI) is the lead stream and should be developed at greatest length.

**For defense / Q&A:**
- Section I.2's "what it does NOT support" column lets you concede gracefully on overclaiming.
- The two Gupta & Woolley cautions (overload; autonomy) are worth pre-empting.

---

## References

Csaszar, F. A., & Steinberger, T. (2022). Organizations as artificial intelligences: The use of artificial intelligence analogies in organization theory. *Academy of Management Annals*, 16(1), 1–37.

Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660.

Gupta, P., Nguyen, T. N., Gonzalez, C., & Woolley, A. W. (2023). Fostering collective intelligence in human–AI collaboration: Laying the groundwork for COHUMAIN. *Topics in Cognitive Science*, 17(2), 189–216.

Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674.

Guzman, A. L., & Lewis, S. C. (2020). Artificial intelligence and communication: A Human–Machine Communication research agenda. *New Media & Society*, 22(1), 70–86.

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100.

Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502.

Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229.

Schoeneborn, D., Kuhn, T. R., & Kärreman, D. (2019). The communicative constitution of organization, organizing, and organizationality. *Organization Studies*, 40(4), 475–496.

---

# Part II — Design Constraints

## II.1 Purpose

The literature underlying WikiGenius doesn't just *support* the design — it also imposes specific constraints. Each constraint has (1) a one-line statement, (2) the source, (3) the WikiGenius design choice it bounds, (4) a concrete test, and (5) what failure looks like.

Use this section during design reviews, when adding new agent behaviors, and as a pre-mortem checklist before user testing.

---

## II.2 Team Agent (Coach + Diagnostic AI)

### C1. Calibrate proactive suggestions — do not over-connect

**Statement.** When the Team Agent proactively surfaces related knowledge, it must supply the right *amount* of information. Surfacing too many connections defeats the purpose.

**Source.** Gupta and Woolley (2021, p. 673): "An important calibration in such systems is to supply the right amount of information, as supplying too many connections could easily lead to overload and defeat the intent of enhanced CI."

**WikiGenius design choice bounded.** The Team Agent's "related knowledge" surfacing behavior; notification volume.

**Concrete test.** For any contribution event, surface at most ≤ 3 connections by default, with an explicit "show more" disclosure. Connections ranked by relevance, not exhaustive. If a member's session shows declining engagement, the surfacing budget should *contract*.

**Failure mode.** The Team Agent floods a contributor with every weakly-related node. Members ignore all suggestions. The transactive memory benefit collapses.

---

### C2. Preserve human autonomy over judgment and responsibility

**Statement.** The Team Agent must not encroach on the contributor's experience of authorship, judgment, or responsibility — even when it could correctly make a decision for them.

**Source.** Gupta and Woolley (2021, p. 674): "Systems that would deprive workers of their autonomy to exercise judgment or experience responsibility for their results can undermine their sense of internal motivation."

**WikiGenius design choice bounded.** Team Agent arbitration scope; the line between "Team Agent decides" vs. "Team Agent suggests + human decides"; permission-tier design.

**Concrete test.** For any Team Agent action, ask: does the human author retain (a) the ability to override, (b) visible attribution, and (c) the felt experience of having made the call? If any answer is no, the action belongs in "suggest, do not execute":
- Edits to others' work: suggest, never silently apply.
- Conflict arbitration: surface the conflict, route decision to a human with appropriate permission.
- Supersession: require explicit human confirmation, with the superseded version inspectable.

**Failure mode.** Team Agent makes "obviously correct" decisions on behalf of members. Members stop feeling like authors. Engagement falls.

---

### C3. Watch for algorithm aversion, not just acceptance

**Statement.** Even well-designed AI decisions are overridden by workers — sometimes to their detriment. The Team Agent's authority is a function of trust, not correctness.

**Source.** Gupta and Woolley (2021, p. 674), citing Glikson and Woolley (2020): "work on algorithm aversion demonstrates the numerous situations in which workers override tools and technologies even when doing so to their detriment."

**WikiGenius design choice bounded.** How aggressively the Team Agent's decisions are presented as default-binding vs. default-overridable.

**Concrete test.** Where Team Agent decisions are reversible, default to one-click reversal. Where irreversible (e.g., supersession), require explicit confirmation. Track override rates — if members consistently override, the agent's behavior needs to change, not the override pathway.

**Failure mode.** Designers harden the agent's authority to reduce override rates. Override rates fall, but engagement falls because members feel coerced.

---

## II.3 User Agent (Assistive AI)

### C4. Preserve attribution under AI-mediated contribution

**Statement.** When the User Agent modifies, augments, or generates content on behalf of a member, the agency question — *who is accountable?* — must have a clear answer.

**Source.** Hancock, Naaman, and Levy (2020, p. 90) frame AI-MC as an agent that "operates on behalf of a communicator by modifying, augmenting, or generating messages" and identify agency, attribution, and trust as the new questions this raises.

**WikiGenius design choice bounded.** How User Agent contributions are recorded in the knowledge graph; provenance visibility.

**Concrete test.** Every node and edit should have a provenance flag: "authored by [human], with User Agent assistance" or "authored by [human], unaided." Other members can see this flag without friction. Permission-tier accountability applies to the *human*, not the User Agent.

**Failure mode.** A member uses the User Agent heavily, producing high volumes of plausible-looking content the human did not formulate. The team relies on it, then discovers errors with no clear answer to "who put this here?"

---

### C5. Do not optimize for goals the member did not ask for

**Statement.** The User Agent should optimize for the user's stated communication goal — not for goals the system can sneak in (engagement, length, brand voice).

**Source.** Hancock et al. (2020, p. 90, Table 1) identify *optimization goal* as a characterizing dimension of AI-MC and flag that AI systems can optimize for goals the communicator did not intend.

**WikiGenius design choice bounded.** What the User Agent is trained or prompted to do when augmenting a member's contribution.

**Concrete test.** Defaults should be conservative — preserve the user's voice and intent unless explicitly asked to change them. The system should not silently "improve" tone, "professionalize" language, or pad short contributions.

**Failure mode.** Members write rough notes; the User Agent inflates them into polished prose; the knowledge graph fills with confidently-stated content nobody actually wrote.

---

## II.4 Trust Surface (How the Team Agent Presents Itself)

### C6. Tangibility — the Team Agent must be present, not hidden

**Statement.** The Team Agent must have a visible, consistent identity in the interface. It cannot operate as ambient infrastructure.

**Source.** Glikson and Woolley (2020, p. 627) identify tangibility as a cognitive-trust dimension; physical or visual presence is shown to increase trust.

**Concrete test.** Every Team Agent action surfaces under an identifiable agent label. Members can navigate to a "what the Team Agent is doing" view. Agent presence is consistent — never "the system" in one place and a named agent in another.

**Failure mode.** Team Agent actions feel like things that "just happen." Members can't form a mental model and develop diffuse mistrust.

---

### C7. Transparency — reasoning must be inspectable on demand

**Statement.** When the Team Agent makes a consequential decision, the reasoning must be available to affected members.

**Source.** Glikson and Woolley (2020): transparency is "critical for developing trust in new technology" (p. 633).

**Concrete test.** For each class of decision, there is a "why this?" view surfacing: the inputs, the rule applied, and alternatives ruled out. One click away — not the default, but available.

**Failure mode.** Members experience agent decisions as opaque. Trust either becomes blind or evaporates.

---

### C8. Reliability — behavior must be consistent across similar cases

**Statement.** The Team Agent must behave the same way in similar circumstances. Inconsistent behavior corrodes trust faster than wrong behavior.

**Source.** Glikson and Woolley (2020): reliability is "exhibiting the same and expected behavior over time" and is "critical to technology trustworthiness."

**Concrete test.** Arbitration rules should be explicit and version-controlled, not implicit in a prompt. Two structurally similar conflicts should produce similar outcomes. Where probabilistic behavior is unavoidable, surface the uncertainty.

**Failure mode.** Members discover the Team Agent freezes a section in one case but allows the same pattern in another. They lose predictability and stop relying on it.

---

### C9. Task characteristics — scope of authority must match user expectations

**Statement.** The Team Agent's authority should not extend beyond what members believe it is qualified to decide.

**Source.** Glikson and Woolley (2020): trust depends on whether the AI is operating within tasks users believe it is suited for.

**Concrete test.** Map every Team Agent action to one of three categories:
- (a) Clearly suitable (deduplication, structural consistency): execute.
- (b) Ambiguously suitable (semantic conflict arbitration): suggest + route.
- (c) Clearly unsuitable (domain judgments): decline + escalate.

Members should see the category for each action class.

**Failure mode.** The agent makes a judgment call in a domain members consider out of its depth. Members generalize the violation and stop trusting it on the actions it *is* qualified for.

---

## II.5 Cross-Cutting Constraints

### C10. Permission tiers must produce accountability, not just access control

**Statement.** Permission tiers are the mechanism by which the system establishes "who is responsible for specific elements of the task."

**Source.** Okhuysen and Bechky (2009, p. 483): accountability "addresses the question of who is responsible for specific elements of the task."

**Concrete test.** For every action, there is a clear answer to "if this goes wrong, who is accountable?" — pointing to a specific human role, not to "the system" or "the Team Agent."

**Failure mode.**Permission tiers exist but accountability is diffused. When a node is wrong, nobody is responsible. The coordination function collapses.

---

### C11. Common understanding is built by the knowledge graph, not assumed

**Statement.** The knowledge graph is the mechanism by which the team holds a shared perspective on its work. Its design must support that function explicitly.

**Source.** Okhuysen and Bechky (2009, pp. 487–488) identify common understanding as an integrating condition of coordination. Ren and Argote (2011, p. 193) treat the TMS structural component as a "retention bin or knowledge repository."

**Concrete test.** A new team member, given access to the knowledge graph, can develop a working understanding of the team's domain, priorities, and recent decisions within one working day without one-on-one onboarding.

**Failure mode.** The graph accumulates content but does not produce shared understanding. New members still need extensive onboarding; old members rely on out-of-band knowledge.

---

### C12. Knowledge decay is a design problem, not just a data problem

**Statement.** A TMS degrades when knowledge becomes stale, expertise shifts, or the team turns over. The system must have explicit decay-handling mechanisms.

**Source.** Ren and Argote (2011, pp. 203–204): "aspects of an individual's transactive memory may become obsolete if members' areas of expertise change... The decay and obsolescence of transactive memories... may be exacerbated in large groups."

**Concrete test.** The knowledge graph distinguishes current from superseded content. The Team Agent surfaces aging content for review. Member-level expertise indicators decay if not refreshed. Member departure triggers a review of authored nodes, not just a permission update.

**Failure mode.** The graph fills with operationally stale content. Members rely on it as current and make decisions based on outdated material.

---

## II.6 Using Part II

**During design reviews.** Walk through each constraint: does the change under review violate any of these? If yes, show why it doesn't apply or how the design accommodates it.

**During build.** When adding autonomous Team Agent behavior, check C1–C3. When adding User Agent transformations, check C4–C5.

**During user testing.** If user testing surfaces something matching a listed failure mode, the corresponding constraint is being violated.

**During defense / paper.** These constraints are pre-emptive answers to reviewer concerns about over-claiming or under-considering autonomy and trust. Citing them shows WikiGenius's design has internalized the warnings the literature provides.

---

## References (Part II)

Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660.

Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674.

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100.

Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502.

Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229.