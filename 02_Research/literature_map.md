# Literature Map: WikiGenius Design × Organizational Communication Theory

**Purpose.** This document maps the design decisions in WikiGenius (a two-tier agent system for AI-native team knowledge management) to established theoretical anchors in organizational communication, coordination, transactive memory, AI–communication studies, and human–AI trust. The aim is twofold: (1) to provide a defensible scholarly foundation for the system's design choices, and (2) to elevate WikiGenius from a product proposal to a contribution that engages substantive open questions in the field.

**Scope.** Eight peer-reviewed articles are drawn on directly: five from *Academy of Management Annals*, one from *Organization Studies*, one from *New Media & Society*, one from *Journal of Computer-Mediated Communication*, and one from *Proceedings of the Human Factors and Ergonomics Society Annual Meeting* (with its 2023 *Topics in Cognitive Science* journal extension noted). Together they cover four scholarly streams: organization × AI, coordination, AI-mediated communication, and the transactive memory / transactive systems literature.

**Conventions.** Direct quotes are kept short (typically under 25 words) and placed in quotation marks with page references in the form (Author, Year, p. X). Most analytic content is original synthesis; quotes anchor the most consequential claims.

---

## 1. Research Significance

The dominant framing of "AI at work" in trade discourse treats AI as a tool that increases individual productivity — better autocomplete, faster drafting, cheaper search. WikiGenius takes a different position: when AI agents are introduced into the team's knowledge layer, they do not merely amplify existing roles. They participate in the **constitution** of the team itself — who knows what, who is accountable for what, what counts as the team's shared "truth", and how disagreements are resolved.

This framing is not rhetorical. It connects WikiGenius directly to five converging streams in the literature:

- **The CCO (Communicative Constitution of Organization) perspective** argues that organizations are produced *in* communication rather than serving as containers within which communication happens. Schoeneborn, Kuhn, and Kärreman (2019) summarize this reversal as the proposition that "*organization happens in communication*" (p. 476, citing Cooren, Bartels, & Martine, 2017). They further note that the participants in such communication need not all be human — "an array of participants — human as well as nonhuman — engage" in the practices that constitute organizational meaning (Schoeneborn et al., 2019, p. 476). WikiGenius's Team Agent is, in this sense, not infrastructure for the organization but a *constitutive actor* in it.

- **The transactive memory systems (TMS) literature** provides the canonical account of how teams encode "who knows what" as a collective resource. Ren and Argote (2011) define a TMS as "a shared system that people in relationships develop for encoding, storing, and retrieving information about different substantive domains" (p. 191), with three transactive processes — directory updating, information allocation, and retrieval coordination — operating over it. They close their review with an explicit call: Web 2.0 technologies such as wikis "have the potential to automatically populate directories of who knows what" (p. 218), but "[w]hether the opportunities are realized depends on how the tools are used, a topic on which additional research is needed" (p. 219). WikiGenius is, structurally, an answer to that open call.

- **The transactive systems model of collective intelligence (TSM-CI)** extends TMS into the human–AI domain. Gupta and Woolley (2021), elaborated by Gupta, Nguyen, Gonzalez, and Woolley (2023), articulate three systems — transactive memory, transactive attention, and transactive reasoning — and identify three corresponding roles for AI: *Assistive AI* (augmenting individual capability), *Coach AI* (nudging collaboration behaviours), and *Diagnostic AI* (monitoring collective process). WikiGenius's User Agent and Team Agent map directly onto this typology — a point developed in Section 4.

- **The AI-Mediated Communication (AI-MC) framework** defines a new mode of interpersonal communication in which "*an intelligent agent operates on behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication goals*" (Hancock, Naaman, & Levy, 2020, p. 89). WikiGenius's User Agent is a textbook instance of AI-MC operating at organizational scale, raising the agency and attribution questions Hancock et al. flag as central.

- **The coordination literature** identifies three integrating conditions — accountability, predictability, and common understanding — through which interdependent work becomes coherent (Okhuysen & Bechky, 2009). WikiGenius's permission tiers, conflict arbitration protocol, and knowledge-graph-as-shared-truth map cleanly onto these three conditions, allowing the system to be analyzed as a *computational instantiation of coordination mechanisms* rather than as a chat product.

- **Trust in AI** is what determines whether such mechanisms are accepted by their human counterparts. Glikson and Woolley (2020) distinguish cognitive trust — driven by "AI's tangibility, transparency, reliability, and immediacy behaviors" (p. 627) — from emotional trust, which additionally depends on anthropomorphism.

The contribution WikiGenius can claim, then, is not "another AI knowledge tool" but a working instance of how *production relations inside a team are reshaped when communicative AI becomes a co-constitutive participant in the team's knowledge work*. Each of the design decisions documented below is a partial answer to questions these literatures have explicitly left open — most directly, the organizational-level TMS question Ren and Argote raised in 2011 and the human–AI extension Gupta and Woolley have been developing since 2021.

---

## 2. Design ↔ Theory Cross-Check Matrix

The table below allows quick verification that each design decision has a defensible theoretical anchor, and conversely that each cited paper is being used for a claim the paper actually supports.

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

**Cross-check logic:** every primary anchor in the right column appears in Section 4 with a verbatim short quote and a page reference. Every "what it does NOT support" claim has been added to prevent overclaiming when this map is referenced in the proposal or paper.

---

## 3. Anchor Stream Overview

Rather than treating each paper in isolation, it is useful to group them into the streams they belong to and clarify how the streams differ.

**Stream A — Organization theory × AI (Csaszar & Steinberger, 2022).** Reads "the organization itself as a kind of AI", arguing that the OT canon has long borrowed from AI ideas — search, representation, aggregation — without acknowledging it. Useful for framing WikiGenius's *system-level* design as itself an information-processing architecture.

**Stream B — Communicative Constitution of Organization (Schoeneborn, Kuhn, & Kärreman, 2019).** A perspective paper synthesizing a decade of CCO work in *Organization Studies*. Crucial for the move that lets WikiGenius's Team Agent be theorized as a participant in organizational constitution rather than as a tool external to it.

**Stream C — Coordination (Okhuysen & Bechky, 2009).** The canonical *Annals* review of how interdependent work becomes coherent. Provides the three integrating conditions used as a checklist against which WikiGenius's coordination affordances are evaluated.

**Stream D — AI-mediated and human–machine communication (Hancock et al., 2020; Guzman & Lewis, 2020).** Two complementary research agendas. Hancock et al. focus on the AI-MC construct narrowly (an agent modifying messages between humans); Guzman and Lewis open the wider HMC question of machines as communicative subjects. Together they cover the *individual interaction layer* of WikiGenius.

**Stream E — Trust in AI (Glikson & Woolley, 2020).** The *Annals* synthesis of empirical work on human trust in AI across robotic, virtual, and embedded forms. Provides the dimensions WikiGenius must design against for the Team Agent's decisions to be accepted.

**Stream F — Transactive memory systems and the TSM-CI extension to AI (Ren & Argote, 2011; Gupta & Woolley, 2021; Gupta, Nguyen, Gonzalez, & Woolley, 2023).** The most directly relevant stream for WikiGenius. Ren and Argote provide the canonical *Annals* integrative framework for TMS at the team level and call for organizational-level extensions via Web 2.0 tools. Gupta and Woolley's TSM-CI builds out the human side into a three-system architecture (memory, attention, reasoning), and the 2023 *Topics in Cognitive Science* extension applies that architecture to human–AI collaboration explicitly. WikiGenius can be positioned as a working implementation of the agenda these papers articulate.

---

## 4. Anchor Cards

Each card contains: citation, the paper's core claim, the most relevant quoted passages, and an explicit mapping back to WikiGenius design decisions.

### Card A — Csaszar & Steinberger (2022)

**Citation.** Csaszar, F. A., & Steinberger, T. (2022). Organizations as artificial intelligences: The use of artificial intelligence analogies in organization theory. *Academy of Management Annals*, 16(1), 1–37.

**Core claim.** Over 100 organization-theory works depend on AI ideas, and these ideas can be grouped into "10 AI approaches that speak to three fundamental processes in organizations: search, representation, and aggregation" (p. 1). The paper argues that the popular framing of AI as merely lowering the "cost of making predictions" misses its effect on "the type of knowledge the organization can represent and on the organization's search and aggregation processes" (p. 2).

**Why it matters for WikiGenius.** WikiGenius is not a prediction tool — it is a *representation and aggregation* system. Csaszar and Steinberger's three-process scheme gives a defensible vocabulary for what the Team Agent does at the system level: it maintains the team's representation of its own knowledge, and it aggregates new contributions into that representation under conflict.

**Maps to design decisions.** D1, D2, D7.

### Card B — Glikson & Woolley (2020)

**Citation.** Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660.

**Core claim.** The review synthesizes empirical studies on trust in AI and proposes a framework distinguishing cognitive trust — shaped by "AI's tangibility, transparency, reliability, and immediacy behaviors" (p. 627) — from emotional trust, additionally shaped by anthropomorphism. AI representation (robotic, virtual, embedded) and level of machine intelligence are identified as key antecedents.

**Why it matters for WikiGenius.** WikiGenius's Team Agent makes consequential decisions — supersession of prior knowledge, conflict arbitration, freezing of sections. Whether members accept these decisions is not a function of the agent's correctness alone; it is a function of how trust is *designed*. Glikson and Woolley's five cognitive-trust dimensions provide a direct checklist:

- **Tangibility** — the agent's presence must be visible (the system surfaces an explicit Team Agent identity in the UI).
- **Transparency** — its reasoning for arbitration outcomes must be inspectable.
- **Reliability** — its behaviour must be consistent over time and across similar cases.
- **Task characteristics** — its scope of authority must match what users believe it is qualified to decide.
- **Immediacy behaviors** — its responsiveness and acknowledgement of user input matter.

**Maps to design decisions.** D8 primarily; also D4 (Team Agent as arbiter), where trust-design constraints determine whether the arbitration is socially viable.

### Card C — Guzman & Lewis (2020)

**Citation.** Guzman, A. L., & Lewis, S. C. (2020). Artificial intelligence and communication: A Human–Machine Communication research agenda. *New Media & Society*, 22(1), 70–86.

**Core claim.** AI does not "fit neatly into paradigms of communication theory that have long focused on human–human communication" (p. 70). The Human–Machine Communication (HMC) approach treats AI as a *communicative subject* — not a mere channel — and the paper articulates a research agenda along three dimensions: functional, relational, and metaphysical. A central distinction: HMC focuses on "people's interactions with technologies designed as communicative subjects, instead of mere interactive objects" (p. 71).

**Why it matters for WikiGenius.** The Team Agent is not Slack — it is not a channel users push messages through. It is an entity users *talk to* and that talks back, makes judgments, and intervenes. Treating it as an "interactive object" understates what it does. Guzman and Lewis's framework licenses the move to theorize the Team Agent as a communicative subject, with all the agency-attribution and identity questions that move entails.

**Maps to design decisions.** D3, D4.

### Card D — Hancock, Naaman, & Levy (2020)

**Citation.** Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100.

**Core claim.** The paper defines AI-Mediated Communication (AI-MC) as "interpersonal communication in which an intelligent agent operates on behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication goals" (p. 89). It proposes three characterizing dimensions — *magnitude*, *media type*, and *optimization goal* (p. 90, Table 1) — and identifies new ethical questions around agency, attribution, and trust that AI-MC introduces beyond traditional CMC.

**Why it matters for WikiGenius.** WikiGenius's User Agent is, by Hancock et al.'s definition, an AI-MC system at organizational scale: it modifies and augments what a member contributes before it lands in the team's knowledge layer. This brings with it the agency question the authors flag — *who* is accountable for a contribution that has been agent-modified? WikiGenius's answer (the human author remains accountable, with permission tier determining authority) is a defensible position in the AI-MC debate, not a settled fact.

**Maps to design decisions.** D1, D3.

### Card E — Okhuysen & Bechky (2009)

**Citation.** Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502.

**Core claim.** Coordination is "the process of interaction that integrates a collective set of interdependent tasks" (p. 463). The review's key contribution is identifying three *integrating conditions* — accountability, predictability, and common understanding — that coordination mechanisms (plans, rules, objects, roles, routines, proximity) accomplish in different combinations (p. 483).

- **Accountability** "addresses the question of who is responsible for specific elements of the task" (p. 483).
- **Predictability** "enables interdependent parties to anticipate subsequent task related activity by knowing what the elements of the task are and when they happen" (p. 486).
- **Common understanding** provides a shared perspective on how the work fits together (paraphrased from p. 487).

**Why it matters for WikiGenius.** This is the framework against which WikiGenius's coordination affordances are evaluated. The mapping is direct:

- *Accountability* ↔ permission tiers + author attribution on knowledge nodes (D5).
- *Predictability* ↔ async notifications + frozen-section signals (D6).
- *Common understanding* ↔ the knowledge graph itself, plus the Team Agent's consistency enforcement (D2, D6).

WikiGenius can therefore be described not as a knowledge tool but as a system that *jointly produces all three integrating conditions* through a single computational substrate.

**Maps to design decisions.** D5, D6 (primary); D2 (common understanding).

### Card F — Schoeneborn, Kuhn, & Kärreman (2019)

**Citation.** Schoeneborn, D., Kuhn, T. R., & Kärreman, D. (2019). The communicative constitution of organization, organizing, and organizationality. *Organization Studies*, 40(4), 475–496.

**Core claim.** The CCO perspective "engineers a major reversal" by asking "how organization happens in communication" (p. 476, quoting Cooren et al., 2017, p. 513) rather than treating communication as something that happens inside pre-existing organizations. Crucially for AI-mediated systems, CCO holds that the participants in constitutive communication can include nonhuman actors: meaning resides "in the practices in which an array of participants — human as well as nonhuman — engage" (p. 476). The paper introduces three theoretical orientations — communication constituting organization (noun), organizing (verb), and organizationality (adjective/attribute).

**Why it matters for WikiGenius.** This is the most ambitious anchor and gives WikiGenius its strongest theoretical claim. If the Team Agent participates in the communicative practices that constitute the team's knowledge truth, then by the CCO reading it is not infrastructure — it is part of how the team comes into being as an organization. Two implications:

1. The Team Agent's design decisions are *not* "engineering choices" in a neutral sense; they are constitutive choices about what kind of organization is being produced.
2. WikiGenius can be theorized using the *organizationality* construct: teams using WikiGenius may not be more or less organized in a binary sense, but exhibit different *degrees* of organizationality depending on how the agents are configured.

**Maps to design decisions.** D2, D4, D5.

### Card G — Ren & Argote (2011)

**Citation.** Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229.

**Core claim.** Reviewing 76 papers, the authors provide the canonical integrative framework for TMS. A TMS is "a shared system that people in relationships develop for encoding, storing, and retrieving information about different substantive domains" (p. 191). It has two components: a *structural* component (the directory of who knows what) and three *transactive processes* — directory updating, information allocation, and retrieval coordination (p. 192) — which together govern how the system operates. Liang, Moreland, and Argote's (1995) three behavioral indicators — memory differentiation, task credibility, and task coordination — became the dominant measurement frame (p. 192). The review further characterizes a TMS as "a retention bin or knowledge repository... for group or organizational memory" that "stores knowledge of who knows what, which can influence the future performance of the group or organization" (p. 193).

The paper closes with a section on organizational-level TMS that is particularly relevant to WikiGenius. Ren and Argote note that "the communication capabilities afforded by Web 2.0 technologies such as wikis, blogs, and online social networks have the potential to automatically populate directories of who knows what while members edit their personal profiles or post documents about their work activities" (p. 218). They add: "Whether the opportunities are realized depends on how the tools are used, a topic on which additional research is needed" (p. 219).

**Why it matters for WikiGenius.** This is the most direct intellectual ancestor of WikiGenius in the management literature. Three reasons:

1. **Structural alignment.** WikiGenius's knowledge graph is, in TMS terms, the structural component — the directory of who knows what (plus, in WikiGenius's extension, what they know). The User Agent + Team Agent system operationalises the three transactive processes (updating, allocation, retrieval) computationally.
2. **Direct fulfillment of an open call.** Ren and Argote explicitly identify Web 2.0 / wiki-class tools as the means by which organizational-level TMS might be realized — and explicitly note that this remains under-researched. WikiGenius can claim to be a working answer to that call, rather than a generic productivity product.
3. **A vocabulary for measurement.** The three behavioral indicators (specialization, credibility, coordination) provide a research-grade evaluation frame for whether WikiGenius actually produces a stronger team-level TMS than baseline knowledge tools — an empirically falsifiable claim.

**Maps to design decisions.** D2 (knowledge graph as the TMS structural component); D7 (the structural/transactive distinction supports the supersession-with-history design); D1 (the three transactive processes correspond to the User Agent / Team Agent division of labor).

### Card H — Gupta & Woolley (2021), with extension Gupta, Nguyen, Gonzalez, & Woolley (2023)

**Citation.** Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674. Extended in Gupta, P., Nguyen, T. N., Gonzalez, C., & Woolley, A. W. (2023). Fostering collective intelligence in human–AI collaboration: Laying the groundwork for COHUMAIN. *Topics in Cognitive Science*, 17(2), 189–216.

**Core claim.** The Transactive Systems Model of Collective Intelligence (TSM-CI) extends TMS into a three-system architecture covering memory, attention, and reasoning. The framework "articulates the inter-member processes underlying the emergence of collective memory, attention, and reasoning, which are fundamental to intelligence in any system" (Gupta & Woolley, 2021, p. 670). The three systems are:

- **Transactive Memory System (TMS)** — who knows what; updating, allocation, retrieval of *knowledge*.
- **Transactive Attention System (TAS)** — who is focused on what; updating, allocation, retrieval of *attention*. Effective TAS produces "burstiness" — alternating independent and synchronous work (p. 672).
- **Transactive Reasoning System (TRS)** — alignment of individual and collective goals; "members maximize joint rewards via negotiation and alignment around these goals and priorities" (p. 672).

Crucially, the paper proposes three roles for AI in supporting these systems (p. 672, Fig. 2):

- **Assistive AI** — "augments individuals' production capabilities".
- **Coach AI** — "predicts and nudges coordination behaviors". The paper explicitly notes that "some new tools enhance [transactive memory] by sensing the content of one member's work and proactively alerting them to related information team members might have" (p. 673).
- **Diagnostic AI** — "monitors collective effort, strategy, and skill use".

The 2023 *Topics in Cognitive Science* extension generalizes this into the COHUMAIN agenda (Collective Human–Machine Intelligence), treating AI agents as full participants in the three transactive systems rather than as adjuncts to them.

**Why it matters for WikiGenius.** This is the closest existing framework to what WikiGenius is doing. The mapping is unusually clean:

- The **User Agent** is Assistive AI in TSM-CI terms — augmenting an individual's contribution capability.
- The **Team Agent** combines **Coach AI** (proactively connecting members' work to relevant existing knowledge — exactly the behavior Gupta & Woolley describe on p. 673) and **Diagnostic AI** (monitoring consistency, surfacing conflicts).
- The **knowledge graph** is the TMS directory; the **conflict-arbitration protocol** is part of the TRS (alignment of goals around what the team's truth should be); the **async notification system** plus **frozen sections** are TAS mechanisms.

Two cautions the framework imposes on WikiGenius:

1. **Calibration of information surfacing.** Gupta and Woolley warn that for Coach-AI-style proactive alerting, "supplying too many connections could easily lead to overload and defeat the intent of enhanced CI" (p. 673). This is a direct design constraint on how aggressively the Team Agent should push related-knowledge suggestions.
2. **Autonomy preservation.** "Systems that would deprive workers of their autonomy to exercise judgment or experience responsibility for their results can undermine their sense of internal motivation" (p. 674). This bounds how much Team Agent arbitration is acceptable before users disengage — a permission-design constraint.

**Maps to design decisions.** D1 (the User Agent / Team Agent split mirrors Assistive vs. Coach+Diagnostic AI); D4 (Team Agent as Coach + Diagnostic AI); D9 (TAS framework directly supports the async/multi-agent coordination layer); also imposes design constraints on D4 and D6.

---

## 5. Reverse Check — Are Any Design Decisions Unsupported?

With the eight papers now integrated, the previous gaps have largely closed. The remaining areas where additional reading would strengthen the proposal are narrower than before:

| Design feature | Status | Notes |
|---|---|---|
| Two-tier agent system | Well-supported — Gupta & Woolley's TSM-CI provides the architectural framework; Hancock and Csaszar each support one tier. | The Gupta et al. (2023) *Topics in Cognitive Science* paper extends this further into the COHUMAIN agenda and is worth citing alongside the 2021 piece for the human–AI angle specifically. |
| Knowledge graph as truth | Well-supported — Ren & Argote (TMS as repository), Csaszar (representation), Schoeneborn (authoritative text) triangulate the claim. | No major gap. |
| Truth-lossless compression / supersession | Adequately supported — Ren & Argote's distinction between the structural component and transactive processes maps to the supersession-with-history design. | Empirical work on knowledge obsolescence and decay in TMS (Ren & Argote, 2011, pp. 203–204) is worth invoking if the proposal discusses memory decay explicitly. |
| Permission tiers specifically as a 3-tier design | The *principle* (accountability) is well-supported by Okhuysen & Bechky; the *specific design* is an engineering choice. | This is acceptable — design choices need not be theoretically derived, only theoretically defensible. |
| Quantitative trust thresholds | Not supported — Glikson & Woolley give the dimensions but not the thresholds. | Empirical question, not a literature gap. |

The earlier note that Argote & Ingram (2000), Murray, Rhymer, & Sirmon (2021), and Foss et al. (2023) might be needed is largely superseded by the addition of Ren & Argote (2011) and the two Gupta & Woolley papers, which together cover knowledge-as-organizational-resource, AI in management, and the knowledge-trajectories question.

---

## 6. How to Use This Document

For the proposal's "Background and Motivation" section:
- Open with the Section 1 paragraph (production relations and constitutive participation).
- Lead with Ren & Argote (2011) and Gupta & Woolley (2021/2023) as the central anchors — these are the most directly applicable and the open-call structure of Ren & Argote (2011, p. 219) gives WikiGenius its sharpest framing line.
- For each design decision, cite the primary anchor identified in the Section 2 matrix.
- Reserve direct quotes for places where the original phrasing is doing real work — the AI-MC definition, the CCO reversal, the three integrating conditions, the TMS definition, and the TSM-CI three-role typology. One short quote per anchor is sufficient.

For the proposal's "Related Work":
- Use Section 3 to organize the streams.
- Use Section 4 cards for the substantive paragraph on each paper.
- Stream F (TMS + TSM-CI) is now the lead stream and should be developed at greatest length.

For the defense / Q&A:
- Section 2's "what it does NOT support" column is the most important — it lets you concede gracefully where a reviewer pushes on overclaiming, while still defending the core mapping.
- The two Gupta & Woolley papers contain two explicit design *cautions* (overload of suggestions; autonomy preservation) that are worth pre-empting in the defense — show that WikiGenius's design takes them seriously rather than waiting for the reviewer to raise them.

---

## References

Csaszar, F. A., & Steinberger, T. (2022). Organizations as artificial intelligences: The use of artificial intelligence analogies in organization theory. *Academy of Management Annals*, 16(1), 1–37. https://doi.org/10.5465/annals.2020.0192

Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660. https://doi.org/10.5465/annals.2018.0057

Gupta, P., Nguyen, T. N., Gonzalez, C., & Woolley, A. W. (2023). Fostering collective intelligence in human–AI collaboration: Laying the groundwork for COHUMAIN. *Topics in Cognitive Science*, 17(2), 189–216. https://doi.org/10.1111/tops.12679

Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674. https://doi.org/10.1177/1071181321651354c

Guzman, A. L., & Lewis, S. C. (2020). Artificial intelligence and communication: A Human–Machine Communication research agenda. *New Media & Society*, 22(1), 70–86. https://doi.org/10.1177/1461444819858691

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100. https://doi.org/10.1093/jcmc/zmz022

Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502. https://doi.org/10.1080/19416520903047533

Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229. https://doi.org/10.1080/19416520.2011.590300

Schoeneborn, D., Kuhn, T. R., & Kärreman, D. (2019). The communicative constitution of organization, organizing, and organizationality. *Organization Studies*, 40(4), 475–496. https://doi.org/10.1177/0170840618782284
