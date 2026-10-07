# Compare candidates and coordinate work

Use this reference when competing solutions or independent workstreams materially help the requested task and delegation is permitted. Keep a single owner when work is tightly coupled or coordination costs exceed the benefit. This guidance does not require additional agents, providers, or background infrastructure.

## Frame and isolate

State the outcome, constraints, observable completion criteria, and resources available. Choose either a cookoff of alternative solutions to the same problem or partitioned work that covers separate parts. State the selection rule or required coverage before starting. Respect user-specified limits and actual host concurrency, including nested workers. Queue work that exceeds capacity rather than spawning without bounds.

Give each worker a self-contained brief with relevant source pointers, exact target revision or workspace snapshot, exclusive write scope or read-only scope, verification requirements, and expected result. Workers inherit task permissions and may not expand them. Use supported host model choices and existing role preferences only where applicable; do not invent models or claim cloud placement or provider diversity unavailable on the host.

For competing code candidates, use separate worktrees or isolated scratch copies from the same baseline, including task-relevant local changes when required. Do not silently compare a dirty working tree with candidates based only on HEAD. Isolate data directories, ports, and other mutable state as well as files. Disjoint file ownership alone is insufficient when tests share an application instance or database. If isolation cannot be established, keep candidates read-only or work sequentially and disclose the limit.

## Cookoff

Define a small rubric tied to the task before generating candidates. Compare structurally different approaches when the tradeoff warrants it. Give candidates the same objective, constraints, and baseline without seeding a preferred answer. Require an artifact or proposal plus concise rationale and evidence. Do not run competing production edits for a design-only request.

Wait for candidate artifacts to stabilize before judging them. Read each viable result and evaluate correctness, contract fit, maintainability, and task-specific criteria. Run comparable checks when authorized. An independent read-only judge can help when available; disagreement calls for examining evidence, not assuming either reviewer is biased. Do not treat scores or agreement as proof.

Select a coherent base. Incorporate another candidate's idea only when it improves the chosen design without contradicting its assumptions. Record the decisive tradeoffs, accepted ideas, and rejected alternatives briefly. Verify the synthesized result, since passing candidates do not establish that a combination works. Keep a proposal as a proposal unless implementation was requested.

## Partitioned work

Identify prerequisites and assign non-overlapping ownership before starting dependent work. Track the required slices, their owners, results, and unresolved dependencies in the existing plan. For sequential dependent phases, complete and check the prerequisite before handing over its output. The coordinator reviews results and owns integration.

Require each result to identify its target, what was done or inspected, verification performed, and remaining gaps. Deduplicate findings and resolve incompatible assumptions against the source. A failed or missing worker result leaves its slice uncovered. Retry only when the cause is understood and another attempt is useful; otherwise report the gap. Do not mark complete merely because most workers succeeded.

## Finish and recover

Integrate authorized changes deliberately, preserving unrelated work. Use [the implementation sequence](implementation.md) to review and verify the combined artifact. For measurement comparisons, use [measured experiments](experiments.md) so methods and conditions remain comparable.

If scope or dependencies change, update ownership before continuing. Stop obsolete workers through actual host capabilities when necessary, then inspect their outputs before starting replacements. Do not assume interruption discarded their edits. Preserve unfinished work with [handoff](../../handoff/SKILL.md), including completed slices, outstanding results, isolated locations, and the next action.

Report the result, actual review independence, selection rationale or coverage, verification, and gaps. Clean up only owned temporary resources when useful and authorized, preserving evidence and valuable unmerged work. Do not delete worktrees, publish branches, or commit merely to complete an orchestration checklist.

Resolve applicable saved role preferences when preparing a worker with supported model or effort selection, following [Pancake preference guidance](../SKILL.md). Fully specified task choices bypass saved resolution. Direct work uses current host settings without a preference lookup. Reviewer panels retain their own discovery and coverage rules even when selection controls are unavailable.
