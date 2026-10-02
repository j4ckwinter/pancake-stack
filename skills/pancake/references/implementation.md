# Implement with rigor

Use this sequence for authorized implementation, including new behavior, fixes, and refactoring. Scale the work to its consequences. A small change can follow the sequence without a separate plan document.

## Ground and choose

Establish the requested outcome and observable acceptance criteria. Inspect relevant code, callers, tests, and current workspace changes. Preserve unrelated work. Use [scope](../../scope/SKILL.md) when requirements are materially unclear, [how](../../how/SKILL.md) for an execution-flow gap, and the reproduction and diagnosis guidance in [fix](../../fix/SKILL.md) for defects. When using fix, perform its implementation and checks in the corresponding phases below rather than completing a separate fix workflow during grounding. Read only the guidance needed.

Settle consequential interface, ownership, compatibility, or persistence choices before implementation with [design](../../design/SKILL.md). Use [challenge](../../challenge/SKILL.md) when a consequential assumption is disputed or needs adversarial examination. Do not require it for every change. Resolve supported findings within the authorized scope before relying on the affected assumption. Small local changes can use the existing shape directly. Resolve repository facts through inspection; leave required product decisions explicit rather than guessing.

## Plan substantial work

Identify prerequisites and dependencies. Divide the work into the smallest useful units that each end in an observable check. Complete blocking foundations before dependent changes. Parallelize only separable work when delegation is useful and permitted; isolate writes and account for shared mutable state. A single owner is appropriate when coordination would cost more than it helps.

Keep a short plan in the available planning surface or conversation. Record consequential decisions and revise the plan when new evidence changes dependencies. Check each unit before building further on it. Do not require commits, rebases, or additional artifacts merely to follow this sequence.

## Implement and review

Make the simplest change that meets the agreed outcome. Add a regression test when it reliably exercises a defect, or reuse an existing check when new infrastructure would not earn its cost.

Inspect the completed diff using [check](../../check/SKILL.md), including affected callers and contracts. For a small, low-impact change, the implementing agent can perform a direct review. For consequential changes, such as shared APIs, data migrations, security boundaries, or concurrency, seek an independent reviewer when host capabilities and task permissions allow. Give the reviewer the objective, constraints, actual diff, and relevant evidence, with a read-only scope. Judge each finding against the implementation before acting. State when independent review was unavailable and perform the review directly. Do not imply that self-review is independent or that same-model agents provide model diversity.

## Verify and handle failures

Use [verify](../../verify/SKILL.md) to exercise the requested behavior. Tie the conclusion to the code and state actually checked. A review without findings does not replace verification. For a defect, repeat the original failing scenario under comparable conditions after the correction. Record the before-and-after result. If that scenario cannot be exercised, name the limitation; passing other tests does not establish that the reported defect is resolved. For refactoring, verify that the relevant existing behavior and contracts remain unchanged.

When a check fails, determine whether the failure comes from product behavior, the environment, or the observation method. For a product defect within the authorized implementation scope, diagnose it, make a focused correction, review the correction, and rerun the affected checks. Expand testing only when the correction or failure warrants it. Do not suppress checks, weaken assertions, or add speculative fixes to manufacture a pass.

For an environment or tooling limitation, complete independent checks and report the specific gap. Do not claim success for an unexercised behavior or change unrelated infrastructure without authorization. Stop a failing loop when progress needs unavailable evidence, a required user decision, or an action outside scope. Preserve the current state and explain the concrete next step rather than declaring completion.

## Finish or continue

Report the outcome, material decisions, review performed, verification results, and remaining gaps. If work remains unfinished or is explicitly paused, use [handoff](../../handoff/SKILL.md) to preserve a concise continuation note in the conversation. Include completed units, current state, known blockers, and the next action. Save a separate note only when requested. Do not create a handoff for every completed small task.
