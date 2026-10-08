# Implement with rigor

Use this sequence for authorized implementation, including new behavior, fixes, and refactoring. Scale the work to its consequences. A small change can follow the sequence without a separate plan document.

## Ground and choose

For consequential TypeScript data shapes or boundary handling, read [TypeScript guidance](../../design/references/typescript.md).

Establish the requested outcome and observable acceptance criteria before editing. Choose checks based on the behavior being changed, including fresh agent trials for changes to workflow execution; Markdown package validation alone cannot establish agent behavior. Inspect relevant code, callers, tests, and current workspace changes. Preserve unrelated work. Use [scope](../../scope/SKILL.md) when requirements are materially unclear, [how](../../how/SKILL.md) for an execution-flow gap, and the reproduction and diagnosis guidance in [fix](../../fix/SKILL.md) for defects. When using fix, perform its implementation and checks in the corresponding phases below rather than completing a separate fix workflow during grounding. Read only the guidance needed.

For a defect, keep the original command or action and its observed failure available for the final report. For a shared interface, data migration, security boundary, or concurrency change, identify the host's independent-review capability and permitted reviewer scope before editing. This is a capability check only; defer implementation-review panel selection until the implementation is ready for review. Investigation or code delegates and a separately requested pre-implementation Challenge apply their task choices when preparing that work. Carry these facts in the existing plan or conversation; a separate artifact is optional.

Settle consequential interface, ownership, compatibility, or persistence choices before implementation with [design](../../design/SKILL.md). Use [challenge](../../challenge/SKILL.md) when a consequential assumption is disputed or needs adversarial examination. Do not require it for every change. Resolve supported findings within the authorized scope before relying on the affected assumption. Small local changes can use the existing shape directly. Resolve repository facts through inspection; leave required product decisions explicit rather than guessing.

## Plan substantial work

For dependent phases, broad migrations, or material uncertainty, read [substantial-work guidance](substantial-work.md) for completion criteria and checkpoints.

Identify prerequisites and dependencies. Divide the work into the smallest useful units that each end in an observable check. Complete blocking foundations before dependent changes. For substantial work, delegate useful independent investigation or implementation units by default through [parallel work](parallel-work.md), within host capabilities and task permissions. Isolate writes and shared mutable state. Keep small or tightly coupled work direct when coordination would cost more than it helps.

Keep a short plan in the available planning surface or conversation. Record consequential decisions and revise the plan when new evidence changes dependencies. Check each unit before building further on it. Do not require commits, rebases, or additional artifacts merely to follow this sequence.

## Execute efficiently

Reuse existing scripts, queries, and generators before doing repetitive transformations by hand. Add a small task-specific tool when it makes the work materially more reliable or reviewable, with explicit inputs, write scope, and a way to inspect the result. Validate it on a representative unit before applying it broadly, and consider rerun behavior. A few clear edits need no new automation. Keep tooling within authorized scope; do not install a framework or persist a helper merely to satisfy a process rule.

Bound investigation output to the relevant paths and questions. Retain concise findings with artifact pointers, assumptions, verification state, and next actions rather than repeatedly loading whole files or histories. Expand inspection when evidence identifies another affected boundary. Use the existing parallel-work guidance only when delegation improves the task; context size alone is not a reason to invent workers or lose decisive evidence.

Resolve observable repository facts through inspection and make routine reversible implementation choices within the requested scope. Continue independent authorized work while awaiting a required product decision. Ask only for information or authorization that is genuinely missing, after making the dependent choice concrete where possible. Explain material assumptions so the user can steer; do not interpret silence as approval or replace a requested product decision with an untested guess.

## Implement

Before adding a layer or mechanism, inspect the affected path for obsolete branches, duplicated decisions, and pass-through wrappers that can be removed within scope. Confirm callers and relevant contracts before deleting anything; apparent redundancy can preserve compatibility or a boundary requirement. Simplify only when it helps the requested change, not as a repository-wide cleanup prerequisite.

Organize the change around observed usage. Keep local behavior direct, mutable state narrowly owned, and domain decisions in one clear place. Introduce an abstraction when it removes meaningful duplication, hides useful complexity, or protects an invariant. Do not add indirection for hypothetical future callers. Assess reader effort by tracing the actual caller path rather than imposing a fixed number of files or layers.

Make the simplest change that meets the agreed outcome. Add a regression test when it reliably exercises a defect, or reuse an existing check when new infrastructure would not earn its cost.

## Review the affected contracts

Inspect the completed diff using [check](../../check/SKILL.md), including affected callers and contracts. Changes to shared interfaces, serialized payload fields, persisted-data compatibility, security boundaries, or concurrency require the independent review below, even when the diff is small. A change confined to local behavior without those contracts can use direct review. Classify by the affected contract, not line count.

When preparing reviewers, follow [active host guidance](host-runtime.md). Use a task-supplied implementation reviewer list when present. Omitted model and effort choices inherit host settings. An absent or explicitly empty list retains the single independent reviewer for consequential work. Do not read stored preferences or use a Challenge panel for implementation review.

For a nonempty task-supplied implementation panel, launch one independent read-only reviewer per entry through working, permitted host delegation. Otherwise launch the existing single independent reviewer for consequential work. Queue reviewers within host limits. Track each selected entry, its returned agent identity, and its completed verdict separately. Check host status or identity-bearing completion messages for every reviewer and retain its actual verdict before declaring completion. A generic wait completion, another reviewer's result, or a progress message does not establish that reviewer's completion. An interrupted reviewer without a verdict remains uncovered; do not report that the whole panel completed. Give every reviewer the same neutral objective, constraints, target snapshot or actual branch diff, and relevant evidence. Ask each to inspect independently through check and return concrete triggers, consequences, inspected locations, and uncertainty. Do not seed reviews with the lead's suspected findings or another reviewer's verdict. Prohibit edits, nested delegation, dependency installation, services, and external actions. If the target changes, identify the coverage mismatch and review the affected correction before relying on earlier findings.

Apply requested models through supported host selection. Omit effort to inherit from the host unless explicitly requested for this task. Apply explicit task effort separately when supported. Record requested settings and what the host actually accepted or reported for each reviewer. Unknown inherited settings remain unknown. Do not invent IDs or silently substitute settings or providers. Unsupported or failed entries remain uncovered; continue with completed evidence and report the gaps. Retry only when the observed failure supports a bounded retry. If no independent reviewer completes, perform direct review and retain the concrete independence gap. If delegation is unavailable or outside task permissions, review directly and disclose that the panel did not run.

Inspect and deduplicate findings by mechanism rather than vote count. Resolve supported findings within scope before completion and keep material disagreement explicit when evidence cannot settle it. A planned review or a read of the check skill is not a reviewer result. Claim model diversity only when completed reviewers have distinct actual model IDs. Same-model agents, including different efforts, provide independent reviews without model diversity; different models from one provider do not establish provider diversity. Failed or incomplete reviews remain coverage gaps.

## Verify and handle failures

Use [verify](../../verify/SKILL.md) to exercise the requested behavior. Tie the conclusion to the code and state actually checked. A review without findings does not replace verification. For a defect, repeat the original failing scenario under comparable conditions after the correction. Record the before-and-after result. If that scenario cannot be exercised, name the limitation; passing other tests does not establish that the reported defect is resolved. For refactoring, verify that the relevant existing behavior and contracts remain unchanged.

When a check fails, determine whether the failure comes from product behavior, the environment, or the observation method. For a product defect within the authorized implementation scope, diagnose it, make a focused correction, review the correction, and rerun the affected checks. Expand testing only when the correction or failure warrants it. Do not suppress checks, weaken assertions, or add speculative fixes to manufacture a pass.

For an environment or tooling limitation, complete independent checks and report the specific gap. Do not claim success for an unexercised behavior or change unrelated infrastructure without authorization. Stop a failing loop when progress needs unavailable evidence, a required user decision, or an action outside scope. Preserve the current state and explain the concrete next step rather than declaring completion.

## Finish or continue

Before the final reply, check the task's completion facts against the observations collected above. For a defect, include the cause, the original failing action and result, and the corrected result. For a consequential change, include the completed independent-review verdict or the concrete capability or permission limit and direct-review result. If the reviewer is still running, wait for the verdict rather than reporting completion. Keep the evidence brief; a command and its before-and-after output can fit in one sentence.

Report the outcome, material decisions, these review and verification results, and remaining gaps. If work remains unfinished or is explicitly paused, use [handoff](../../handoff/SKILL.md) to preserve a concise continuation note in the conversation. Include completed units, current state, known blockers, and the next action. Save a separate note only when requested. Do not create a handoff for every completed small task.
