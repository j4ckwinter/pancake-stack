---
name: how
description: Explain how existing code works by tracing behavior and citing its implementation. Use for code walkthroughs, execution flow, and ownership questions.
---

# Explain how the code works

Answer the user's question from the implementation. This is an explanation workflow, not authorization to change code.

## Investigate

- Start with the named behavior, symbol, or file. If the scope is broad, state a narrow interpretation and proceed. Ask only when the missing context prevents a useful answer.
- Read the applicable repository instructions. Find the entry point, follow its calls, and identify where inputs become state, output, or an external action. Include failure paths when they affect the question.
- Prefer implementation over comments and documentation when they disagree. Use tests to understand expected behavior, while distinguishing expectations from behavior actually observed.
- Search narrowly and read the relevant callers. Stop when you can explain the requested flow and its ownership. Expand only to resolve a specific gap.
- Keep the investigation read-only. Use inspection commands. Do not execute unfamiliar application code, run setup or installation, change configuration, or start services merely to explain them. If runtime evidence requires side effects, explain what static inspection establishes and what remains unverified.
- Keep a focused trace in the current agent. For a substantial investigation with independent subsystem questions, delegate read-only slices through [parallel work](../pancake/references/parallel-work.md) when permitted and available. Inspect the decisive source locations before synthesizing the explanation. Delegate settings inherit from the host unless the task overrides them; they do not change the current conversation's model.

## Explain

Lead with the answer. Then trace the behavior in execution order, using concrete symbols and values where they help.

Link the key implementation locations with file paths and line numbers. Cite only files you inspected. Connect each reference to the behavior it proves, rather than listing files without explanation.

Distinguish facts established by code, runtime observations, and inferences. Do not turn a plausible explanation into a claimed observation. If something is unresolved, name the missing evidence and its effect on the answer.

Scale the response to the question. A small utility may need one paragraph. A subsystem may need a short flow and the files that own it. Add a diagram only if it clarifies relationships. Avoid mandatory sections and inventories of unrelated files.

If the question assumes behavior the code does not implement, correct the premise with evidence. If the user asks why a design was chosen, explain what the implementation shows and label any inferred motivation. Do not invent historical intent.

End when the question is answered. Mention material limitations or a concrete next investigation only when needed. Do not append a refactor plan or make edits unless requested separately.
