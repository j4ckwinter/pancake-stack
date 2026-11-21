---
name: how
description: Explain how existing code works by tracing behavior and citing its implementation. Use for code walkthroughs, execution flow, and ownership questions.
---

# Explain how the code works

Answer the question from the implementation. Keep the investigation read-only: inspect, and do not run unfamiliar code, setup, or services merely to explain them. If the scope is broad, state a narrow interpretation and proceed.

Start at the named behavior, symbol, or file and the applicable repository instructions. Find the entry point, follow its calls, and note where inputs become state, output, or an external action, including failure paths that matter to the question. Where comments or documentation disagree with the code, the code wins. Tests show expected behavior, not observed behavior. Stop once you can explain the flow and its ownership.

Trace a focused question yourself. For a large investigation with independent subsystem questions, delegate read-only slices through [parallel work](../pancake/references/parallel-work.md) when permitted, with settings from [active host guidance](../pancake/references/host-runtime.md), and inspect the decisive locations before relying on the result.

Lead with the answer, then trace the behavior in execution order with concrete symbols and values. Link the inspected locations that prove each step, with file paths and line numbers. Separate what the code establishes from inference, and name missing evidence. Scale the answer to the question: a utility may need one paragraph, a subsystem a short flow and the files that own it. If the question assumes behavior the code does not have, correct the premise with evidence. For motivation, label inferred intent as inference or use [why](../why/SKILL.md). Do not append a refactor plan or make edits unless requested.
