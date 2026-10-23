# Implement with rigor

Use this sequence for authorized implementation, including new behavior, fixes, and refactoring. Scale the work to its consequences. A small change can follow the sequence without a separate plan document.

## Ground and choose

Establish the requested outcome and observable acceptance criteria before editing. Choose checks based on the behavior being changed, including fresh agent trials for changes to workflow execution; Markdown package validation alone cannot establish agent behavior. Inspect relevant code, callers, tests, and current workspace changes. Preserve unrelated work. Use [scope](../../scope/SKILL.md) when requirements are materially unclear, [how](../../how/SKILL.md) for an execution-flow gap, and the reproduction and diagnosis guidance in [fix](../../fix/SKILL.md) for defects. When using fix, perform its implementation and checks in the corresponding phases below rather than completing a separate fix workflow during grounding. Read only the guidance needed.

For a defect, keep the original command or action and its observed failure available for the final report. Before consequential edits, read [change review](change-review.md) for affected-contract classification, review capability, and design preparation.

For refactoring, capture the affected behavior with an existing focused check before restructuring, then repeat it afterward. Add characterization coverage only when existing checks cannot establish the contract and the task permits it. Report an unavailable baseline.

## Plan substantial work

For dependent phases, broad migrations, or material uncertainty, read [substantial-work guidance](substantial-work.md) for completion criteria and checkpoints.

Keep a short plan in the available planning surface or conversation. Order dependent units by their prerequisites and give each an observable completion check. For work spanning phases, use the unit tracking and checkpoints in substantial-work guidance. Record consequential decisions and revise the plan when evidence changes dependencies. Do not require commits, rebases, or additional artifacts merely to represent the sequence.

For substantial work, read [parallel work](parallel-work.md) during planning for delegation defaults and coordination.

## Execute efficiently

Reuse existing scripts, queries, and generators before doing repetitive transformations by hand. Add a small task-specific tool when it makes the work materially more reliable or reviewable, with explicit inputs, write scope, and a way to inspect the result. Validate it on a representative unit before applying it broadly, and consider rerun behavior. A few clear edits need no new automation. Keep tooling within authorized scope; do not install a framework or persist a helper merely to satisfy a process rule.

Bound investigation output to the relevant paths and questions. Retain concise findings with artifact pointers, assumptions, verification state, and next actions rather than repeatedly loading whole files or histories. Expand inspection when evidence identifies another affected boundary.

Resolve observable repository facts through inspection and make routine reversible implementation choices within the requested scope. Continue independent authorized work while awaiting a required product decision. Ask only for information or authorization that is genuinely missing, after making the dependent choice concrete where possible. Explain material assumptions so the user can steer; do not interpret silence as approval or replace a requested product decision with an untested guess.

## Implement

Before adding a layer or mechanism, inspect the affected path for obsolete branches, duplicated decisions, and pass-through wrappers that can be removed within scope. Confirm callers and relevant contracts before deleting anything; apparent redundancy can preserve compatibility or a boundary requirement. Simplify only when it helps the requested change, not as a repository-wide cleanup prerequisite.

Organize the change around observed usage. Keep local behavior direct, mutable state narrowly owned, and domain decisions in one clear place. Introduce an abstraction when it removes meaningful duplication, hides useful complexity, or protects an invariant. Do not add indirection for hypothetical future callers. Assess reader effort by tracing the actual caller path rather than imposing a fixed number of files or layers.

Make the simplest change that meets the agreed outcome. Add a regression test when it reliably exercises a defect, or reuse an existing check when new infrastructure would not earn its cost.

## Review the affected contracts

Apply [change review](change-review.md) to the completed diff, including its independent-review and completion requirements.

## Verify and handle failures

Use [verify](../../verify/SKILL.md) to exercise the requested behavior. Tie the conclusion to the code and state actually checked. A review without findings does not replace verification. For a defect, repeat the original failing scenario under comparable conditions after the correction. Record the before-and-after result. If that scenario cannot be exercised, name the limitation; passing other tests does not establish that the reported defect is resolved. For refactoring, verify that the relevant existing behavior and contracts remain unchanged.

When a check fails, determine whether the failure comes from product behavior, the environment, or the observation method. For a product defect within the authorized implementation scope, diagnose it, make a focused correction, review the correction, and rerun the affected checks. Expand testing only when the correction or failure warrants it. Do not suppress checks, weaken assertions, or add speculative fixes to manufacture a pass.

For an environment or tooling limitation, complete independent checks and report the specific gap. Do not claim success for an unexercised behavior or change unrelated infrastructure without authorization. Stop a failing loop when progress needs unavailable evidence, a required user decision, or an action outside scope. Preserve the current state and explain the concrete next step rather than declaring completion.

## Finish or continue

Before the final reply, check the task's completion facts against the observations collected above. For a defect, include the cause, the original failing action and result, and the corrected result. Keep the evidence brief; a command and its before-and-after output can fit in one sentence.

Report the outcome, material decisions, these review and verification results, and remaining gaps. If work remains unfinished or is explicitly paused, use [handoff](../../handoff/SKILL.md) to preserve a concise continuation note in the conversation. Include completed units, current state, known blockers, and the next action. Save a separate note only when requested. Do not create a handoff for every completed small task.
