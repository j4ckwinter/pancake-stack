---
name: scope
description: Turn a ticket or feature request into an implementation brief grounded in existing code. Use to establish outcomes, acceptance criteria, boundaries, and missing requirements before design or implementation.
---

# Scope the work

Read [core values](../pancake/references/values.md) and applicable repository instructions. Establish what needs building, rather than choosing a detailed architecture or implementing it.

Start with the ticket or request supplied by the user and the latest relevant conversation context. Identify the intended outcome, affected users, explicit acceptance criteria, and constraints. If no useful task can be identified, ask for the ticket summary. Do not invent ticket content, deadlines, or product commitments.

Inspect the relevant implementation, callers, tests, and documentation with focused read-only commands. Use current branch changes when they clarify work already underway, without assuming all workspace changes belong to the ticket. Cite inspected locations that establish current behavior or constrain the work. Distinguish behavior established by code from runtime observations and test expectations.

Resolve observable questions through repository evidence before asking the user. Separate confirmed requirements from proposed acceptance criteria, assumptions, and open decisions. Write criteria as observable outcomes rather than implementation prescriptions. An existing implementation establishes current behavior, not proof that the behavior is desired.

For missing product choices, explain which outcome depends on the decision. Ask only questions that materially change scope or acceptance. Continue independent investigation while a decision is pending, but do not silently settle a required choice. Use labeled assumptions for low-impact details when a useful draft can proceed without an answer.

Define the smallest scope that satisfies the requested outcome. Preserve explicit requirements. List concrete exclusions only when they prevent likely scope creep, and label proposed exclusions that the user has not agreed to. Identify affected interfaces, dependencies, and compatibility needs without turning the brief into a redesign.

Return a concise brief containing the intended outcome, current behavior and relevant code, acceptance criteria, scope boundaries, and material open decisions. Include a small implementation sequence with an observable verification point for each meaningful unit when useful. Keep the sequence provisional where unanswered questions could change it. Distinguish proposed checks from verification already performed. Avoid effort estimates or deadlines without supporting evidence.

Scale the brief to the task. A small change may need a few bullets. For a larger change, use short sections that a colleague can act on without reading the conversation. Indicate whether the brief is ready for design or implementation, or which decision remains necessary.

Return the brief in chat. Do not change files, run application code, create prototypes, retrieve unrelated external records, or update tickets merely to clarify scope. Save a document or proceed to design or implementation only when requested. Scoping does not authorize additional work by itself.
