# Design Constraints from the Literature

**Purpose.** The literature underlying WikiGenius (see `literature_map.md`) doesn't just *support* the design — it also imposes specific constraints on it. This document extracts those constraints as a separate, scannable reference. Each constraint has (1) a one-line statement, (2) the source it comes from, (3) the WikiGenius design choice it bounds, (4) a concrete test for whether the system is respecting it, and (5) what failure looks like.

Use this document during design reviews, when adding new agent behaviors, and as a pre-mortem checklist before user testing. Constraints are grouped by the system component they primarily affect.

---

## Team Agent (Coach + Diagnostic AI)

### C1. Calibrate proactive suggestions — do not over-connect

**Statement.** When the Team Agent proactively surfaces related knowledge in response to a member's contribution, it must supply the right *amount* of information. Surfacing too many connections defeats the purpose.

**Source.** Gupta and Woolley (2021, p. 673): "An important calibration in such systems is to supply the right amount of information, as supplying too many connections could easily lead to overload and defeat the intent of enhanced CI."

**WikiGenius design choice bounded.** The Team Agent's "related knowledge" surfacing behavior when a member edits, asks, or contributes. Also bounds the Team Agent's notification volume.

**Concrete test.** For any contribution event, the Team Agent should surface at most a small bounded number of connections (suggested: ≤ 3 by default, with explicit "show more" disclosure). Connections should be ranked by relevance, not exhaustively listed. If a member's session shows declining engagement (reduced clicks on suggestions, dismissals) the surfacing budget should *contract*, not expand.

**Failure mode.** The Team Agent floods a contributor with every weakly-related node in the graph. Members start ignoring all suggestions, including the high-value ones. The transactive memory benefit collapses because surfacing becomes noise.

---

### C2. Preserve human autonomy over judgment and responsibility

**Statement.** The Team Agent must not encroach on the contributor's experience of authorship, judgment, or responsibility for their work — even when it could correctly make a decision for them.

**Source.** Gupta and Woolley (2021, p. 674): "Systems that would deprive workers of their autonomy to exercise judgment or experience responsibility for their results can undermine their sense of internal motivation."

**WikiGenius design choice bounded.** Team Agent arbitration scope; the line between "Team Agent decides" and "Team Agent suggests + human decides"; permission-tier design.

**Concrete test.** For any class of action the Team Agent can take, ask: does the human author retain (a) the ability to override, (b) visible attribution, and (c) the felt experience of having made the call? If the answer to any is no, the action belongs in the "suggest, do not execute" category. Specifically:
- Edits to others' work: suggest, never silently apply.
- Conflict arbitration: surface the conflict, frame the options, but route the actual decision to a human with appropriate permission.
- Supersession of prior content: require explicit human confirmation, with the superseded version inspectable.

**Failure mode.** Team Agent makes "obviously correct" decisions on behalf of members. Members stop feeling like authors of the team's knowledge — they become reviewers of an agent's output. Engagement falls; quality of contributions falls because the felt stake is gone.

---

### C3. Watch for algorithm aversion, not just acceptance

**Statement.** Even well-designed AI decisions are overridden by workers — sometimes to their detriment. The Team Agent's authority is not a function of its correctness; it is a function of the trust members place in it.

**Source.** Gupta and Woolley (2021, p. 674), citing Glikson and Woolley (2020): "work on algorithm aversion demonstrates the numerous situations in which workers override tools and technologies even when doing so to their detriment."

**WikiGenius design choice bounded.** How aggressively the Team Agent's decisions are presented as default-binding vs. default-overridable.

**Concrete test.** Where Team Agent decisions are reversible, default to making them reversible without friction (one click). Where they are not reversible (e.g., supersession), require explicit confirmation. Track override rates as a primary metric — if members consistently override the Team Agent's arbitration, the agent's behavior, not the override pathway, is what needs to change.

**Failure mode.** Designers harden the agent's authority to reduce override rates. Override rates fall, but engagement also falls because members feel coerced. The system loses the human contributions that gave it value in the first place.

---

## User Agent (Assistive AI)

### C4. Preserve attribution under AI-mediated contribution

**Statement.** When the User Agent modifies, augments, or generates content on behalf of a member, the agency question — *who is accountable for this contribution?* — must have a clear answer.

**Source.** Hancock, Naaman, and Levy (2020, p. 90) frame AI-MC as an agent that "operates on behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication goals" and identify agency, attribution, and trust as the new questions this raises (p. 89).

**WikiGenius design choice bounded.** How User Agent contributions are recorded in the knowledge graph; what is shown to other team members about the provenance of a node or edit.

**Concrete test.** Every node and edit in the knowledge graph should have a recorded "authored by [human], with User Agent assistance" or "authored by [human], unaided" provenance flag. Other members reading the content should be able to see this flag without friction. Permission-tier accountability rules should apply to the *human*, not the User Agent.

**Failure mode.** A member uses the User Agent heavily, producing high volumes of plausible-looking content the human did not actually formulate. The team relies on it, then discovers errors with no clear answer to "who put this here and who can fix it?"

---

### C5. Do not optimize for goals the member did not ask for

**Statement.** The User Agent should optimize messages for the user's stated communication goal (clarity, completeness, fit to the knowledge graph) — not for goals the system can sneak in (engagement, length, brand voice).

**Source.** Hancock et al. (2020, p. 90, Table 1) identify *optimization goal* as one of the three characterizing dimensions of AI-MC, and flag that AI systems can optimize for goals (appearing trustworthy, persuasive, etc.) that the communicator did not intend.

**WikiGenius design choice bounded.** What the User Agent is trained or prompted to do when augmenting a member's contribution.

**Concrete test.** For every transformation the User Agent applies (rewrite, expand, summarise, restructure), ask: did the user ask for this? Defaults should be conservative — preserve the user's voice and intent unless explicitly asked to change them. The system should not silently "improve" tone, "professionalize" language, or pad short contributions to look more substantial.

**Failure mode.** Members write rough notes; the User Agent inflates them into polished prose; the team's knowledge graph fills with confidently-stated content that nobody actually wrote and nobody is sure is correct.

---

## Trust Surface (How the Team Agent Presents Itself)

The cognitive-trust dimensions identified in Glikson and Woolley (2020) function as a checklist for how the Team Agent earns the right to make decisions members will accept. Each is a constraint on UI and behavior.

### C6. Tangibility — the Team Agent must be present, not hidden

**Statement.** The Team Agent must have a visible, consistent identity in the interface. It cannot operate as ambient infrastructure.

**Source.** Glikson and Woolley (2020, p. 627) identify tangibility as one of five cognitive-trust dimensions; physical or visual presence is shown to increase trust across studies.

**Concrete test.** Every Team Agent action surfaces under an identifiable agent label, not anonymously. Members can navigate to a "what the Team Agent is doing" view at any time. Agent presence is consistent across the product — never represented as "the system" in one place and as a named agent in another.

**Failure mode.** Team Agent actions feel like things that "just happen". Members can't tell what is automated vs. human, can't form a mental model of the agent, and develop diffuse mistrust of the whole product.

---

### C7. Transparency — reasoning must be inspectable on demand

**Statement.** When the Team Agent makes a consequential decision, the reasoning behind it must be available to the affected members.

**Source.** Glikson and Woolley (2020): transparency is the extent to which "the underlying operating rules and inner logics of the technology are apparent to the users and is considered to be critical for developing trust in new technology" (p. 633, in the cognitive trust section).

**Concrete test.** For each class of decision the Team Agent makes (conflict arbitration, supersession, freezing a section), there is a "why this?" view that surfaces: the inputs the agent considered, the rule it applied, and the alternatives it ruled out. This view does not need to be the default — it needs to be one click away.

**Failure mode.** Members experience agent decisions as opaque. Trust either becomes blind (dangerous when wrong) or evaporates (no acceptance of correct decisions).

---

### C8. Reliability — behavior must be consistent across similar cases

**Statement.** The Team Agent must behave the same way in similar circumstances. Inconsistent behavior corrodes trust faster than wrong behavior does.

**Source.** Glikson and Woolley (2020) define reliability as "exhibiting the same and expected behavior over time" and note it is "critical to technology trustworthiness" (cognitive trust section). They also note reliability is harder to assess for AI because of nondeterministic behavior.

**Concrete test.** The Team Agent's arbitration rules should be explicit and version-controlled, not implicit in a prompt that changes session-to-session. Two structurally similar conflicts should produce structurally similar outcomes. Where probabilistic behavior is unavoidable, surface the uncertainty rather than hiding it.

**Failure mode.** Members discover that the Team Agent freezes a section in one case but allows the same edit pattern in another. They lose the ability to predict the agent's behavior and stop relying on it for coordination.

---

### C9. Task characteristics — scope of authority must match user expectations

**Statement.** The Team Agent's authority should not extend beyond what members believe it is qualified to decide.

**Source.** Glikson and Woolley (2020) identify task characteristics as a cognitive trust dimension — trust depends on whether the AI is operating within tasks users believe it is suited for.

**Concrete test.** Map every Team Agent action to one of three categories: (a) clearly suitable (deduplication, structural consistency checks), (b) ambiguously suitable (semantic conflict arbitration), (c) clearly unsuitable (judgments requiring domain context the agent lacks). Default behavior should match category: (a) execute, (b) suggest + route, (c) decline + escalate. Members should be able to see the category for each action class.

**Failure mode.** The agent makes a judgment call in a domain members consider out of its depth. Even if the call is correct, members generalize the violation and stop trusting it on the actions it *is* qualified for.

---

## Cross-Cutting

### C10. Permission tiers must produce accountability, not just access control

**Statement.** Permission tiers (Admin / Project Owner / Member) are not just about restricting actions. They are the mechanism by which the system establishes "who is responsible for specific elements of the task" — which is the core integrating condition for coordination.

**Source.** Okhuysen and Bechky (2009, p. 483): accountability "addresses the question of who is responsible for specific elements of the task. By creating accountability, organization members make clear where the responsibilities of interdependent parties lie."

**Concrete test.** For every action the system supports, there is a clear answer to "if this goes wrong, who is accountable?" — and that answer points to a specific human role, not to "the system" or "the Team Agent". The permission tier shapes who *can* act, but the accountability rule shapes who *is responsible* for the action's consequences.

**Failure mode.** Permission tiers exist but accountability is diffused into the system. When a knowledge node turns out to be wrong, nobody is responsible — the Member who wrote it points to the User Agent, the Team Agent points to its rules, the Owner points to having delegated. The coordination function collapses.

---

### C11. Common understanding is built by the knowledge graph, not assumed

**Statement.** The knowledge graph is not just a storage layer. It is the mechanism by which the team holds a shared perspective on its work. Its design must support that function explicitly.

**Source.** Okhuysen and Bechky (2009, pp. 487–488) identify common understanding as one of the three integrating conditions of coordination, accomplished through shared perspectives on the whole of the work. Ren and Argote (2011, p. 193) treat the structural component of a TMS as "a retention bin or knowledge repository... for group or organizational memory."

**Concrete test.** A new team member, given access to the knowledge graph, can develop a working understanding of the team's domain, current priorities, and recent decisions within a bounded time (e.g., one working day) without one-on-one onboarding. If they cannot, the graph is functioning as storage but not as common understanding.

**Failure mode.** The graph accumulates content but does not produce shared understanding. New members still need extensive one-on-one onboarding; old members rely on out-of-band knowledge to interpret what the graph says.

---

### C12. Knowledge decay is a design problem, not just a data problem

**Statement.** A TMS — including a computational one — degrades when knowledge becomes stale, when members' expertise shifts, or when the team turns over. The system must have explicit mechanisms for handling decay, not just for accumulation.

**Source.** Ren and Argote (2011, pp. 203–204) identify forgetting and decay as an under-researched aspect of TMS: "aspects of an individual's transactive memory may become obsolete if members' areas of expertise change... The decay and obsolescence of transactive memories are less of a concern in small and collocated groups where members interact frequently, but may be exacerbated in large groups."

**Concrete test.** The knowledge graph distinguishes current from superseded content (this is the "truth-lossless compression" design). The Team Agent surfaces aging content that has not been validated for review. Member-level expertise indicators decay if not refreshed. Departure of a member triggers a review of the nodes they authored, not just a permission update.

**Failure mode.** The graph fills with content that is technically retained but operationally stale. Members rely on it as current, make decisions based on outdated material, and the system's value as common understanding inverts into a liability.

---

## Using This Document

**During design reviews.** Walk through each constraint and ask: does the change under review violate any of these? If yes, the change needs explicit treatment of the constraint — either showing why it doesn't apply here, or describing how the design accommodates it.

**During build.** When adding any Team Agent behavior that is *more* autonomous than the current baseline (executes rather than suggests, decides rather than escalates), check C1–C3 explicitly. When adding any User Agent transformation, check C4–C5.

**During user testing.** The "failure mode" descriptions are designed to be observable. If user-testing surfaces something that looks like a listed failure mode, the corresponding constraint is being violated.

**During the defense/paper.** The constraints in this document are pre-emptive answers to reviewer concerns about over-claiming, over-automating, or under-considering autonomy and trust. Citing them shows that WikiGenius's design has internalized the warnings the literature provides.

---

## References

Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627–660. https://doi.org/10.5465/annals.2018.0057

Gupta, P., & Woolley, A. W. (2021). Articulating the role of artificial intelligence in collective intelligence: A transactive systems framework. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 65(1), 670–674. https://doi.org/10.1177/1071181321651354c

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100. https://doi.org/10.1093/jcmc/zmz022

Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *The Academy of Management Annals*, 3(1), 463–502. https://doi.org/10.1080/19416520903047533

Ren, Y., & Argote, L. (2011). Transactive memory systems 1985–2010: An integrative framework of key dimensions, antecedents, and consequences. *The Academy of Management Annals*, 5(1), 189–229. https://doi.org/10.1080/19416520.2011.590300
