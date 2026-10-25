# Implement with rigor

Use this sequence for authorized implementation, including new behavior, fixes, and refactoring. Keep small changes direct. Read only the guidance needed.

## 1. Establish the outcome and baseline

Define observable acceptance criteria from the request. Inspect relevant code, callers, tests, repository instructions, and workspace changes. Preserve unrelated work. Choose checks that exercise the changed behavior. Workflow changes need fresh agent trials; package validation alone cannot establish agent behavior.

Use [scope](../../scope/SKILL.md) for materially unclear requirements and [how](../../how/SKILL.md) for execution-flow gaps. For defects, use [fix](../../fix/SKILL.md) to reproduce and diagnose, then perform its implementation and checks in the phases below. Retain the original failing action and result.

For refactoring, run an existing focused check before restructuring. Add characterization coverage only when existing checks cannot establish the contract and the task permits it. Report an unavailable baseline.

Before editing, read [change review](change-review.md) for affected-contract classification, review capability, and design preparation.

## 2. Plan the necessary work

For dependent phases, broad migrations, material uncertainty, or sustained work, read [substantial-work guidance](substantial-work.md). It owns unit tracking, completion checks, and phase checkpoints. For substantial work, read [parallel work](parallel-work.md) for delegation and coordination.

Keep the plan in the available planning surface or conversation. Order units by prerequisites and give each an observable completion check. Revise the plan when evidence changes dependencies. Do not create commits, rebases, or separate artifacts merely to represent the sequence.

Resolve observable facts through inspection. Make routine reversible choices within scope and explain material assumptions. Ask only for genuinely missing information or authorization, after making the dependent choice concrete where possible. Continue independent work while awaiting a required decision. Silence is not approval.

## 3. Make the focused change

Inspect the affected path for obsolete branches, duplicated decisions, and pass-through wrappers before adding mechanisms. Confirm callers and contracts before deleting apparent redundancy. Simplify only where it helps the requested change.

Keep domain decisions together and mutable state narrowly owned. Add an abstraction only when it removes meaningful duplication, hides useful complexity, or protects an invariant. Assess reader effort through the caller path, not a fixed file or layer count. Make the simplest change that meets the outcome. Add a reliable regression test or reuse an adequate existing check.

Reuse scripts, queries, and generators for repetitive transformations. Build a task-specific tool only when it improves reliability or reviewability. Define its inputs and write scope, consider reruns, and validate a representative result before broad use. Do not install frameworks or persist helpers merely to satisfy process.

Bound investigation to relevant paths and questions. Keep concise findings, artifact pointers, assumptions, verification state, and next actions. Expand inspection when evidence reveals another affected boundary.

## 4. Review and verify

Apply [change review](change-review.md) to the completed diff, including its independent-review and completion requirements. Use [verify](../../verify/SKILL.md) to exercise the requested behavior on the resulting artifact. A review without findings does not replace verification.

For defects, repeat the original failing scenario under comparable conditions and retain the before-and-after results. For refactoring, repeat the baseline check and verify affected contracts. Passing other tests does not prove an unexercised scenario.

## 5. Resolve failures and finish

Classify failures as product defects, environment limitations, or observation errors. Diagnose an in-scope defect, make a focused correction, review it, and rerun affected checks. Expand testing only when the correction or failure warrants it. Never weaken assertions, suppress checks, or add speculative fixes to manufacture a pass.

For a tooling or environment limit, complete independent checks and report the gap. Stop a failing loop when progress needs unavailable evidence, a required decision, or action outside scope. Do not change unrelated infrastructure or claim success for unexercised behavior.

Check completion against the acceptance criteria. Report the outcome, material decisions, review verdicts, verification, and remaining gaps. For defects, include the cause and original failing action with its before-and-after result.

If work remains unfinished or is explicitly paused, use [handoff](../../handoff/SKILL.md) for a concise continuation note in the conversation. Save a separate note only when requested. Do not create a handoff for completed small tasks.
