---
name: design
description: Propose a software design grounded in existing code and constraints. Use for architecture decisions, interface planning, or comparing implementation approaches before coding.
---

# Design a change

Read [core values](../pancake/references/values.md) and applicable repository instructions. Establish the requested outcome, constraints, and what is outside scope from the user's request and available context. Ask only when a missing product decision materially changes the design.

Inspect the relevant implementation, callers, tests, and documented contracts. Identify who owns the data and behavior, and which boundaries the change crosses. Cite inspected locations that constrain the proposal. For greenfield work, state assumptions rather than inventing an existing architecture. Distinguish documented rationale from inferred intent.

Start with an example of how a caller or user would use the proposed change. Derive the necessary data shapes, interfaces, and ownership from that example. Describe state transitions, failure handling, or persistence only when relevant. Keep sketches in the response unless the user requests a written artifact. Do not add stub files or change code merely to present a design.

Compare alternatives when the choice has meaningful consequences. Include extending the existing design when viable. Explain the concrete tradeoff that decides the recommendation, such as compatibility, maintenance, performance, or operational cost. A small local change may need only a short recommendation. A consequential architectural choice benefits from structurally different alternatives. Do not require a fixed number of designs, agents, or providers.

If an uncertain behavior decides the design, seek narrow evidence from existing checks or inspection. Label estimates and untested assumptions. A prototype that writes files, starts services, or changes configuration requires authorization appropriate to those actions; a design request alone remains read-only.

Recommend the simplest sufficient approach. Identify affected contracts, migration needs, and material risks. Describe a focused verification plan tied to the intended outcome, distinguishing proposed checks from checks already performed. For larger work, outline an implementation sequence that can be verified incrementally.

Lead with the recommendation. Include the usage sketch, decisive tradeoffs, and verification plan only to the depth the task needs. Leave unresolved decisions explicit. Stop at the proposal unless implementation was also requested. If authorized implementation reveals a faulty assumption, revise the design rather than preserving it through repeated workarounds.
