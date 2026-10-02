# Substantial work

Read this when planning or authorized implementation spans dependent phases, many callers, material uncertainty, or a requested sustained run. Use the existing implementation sequence for ordinary changes. This reference adds checkpoints to that sequence.

A request for a plan delivers the plan without starting implementation. Use inspected evidence for proposed units and verification; distinguish planned checks from completed ones. Save a plan only when requested.

## Frame the outcome

State what must be observably true when the task is complete, which behavior must remain intact, and which actions are authorized. Identify the affected units, prerequisites, consequential unknowns, and available verification. Estimate scope from inspected evidence; label uncertain estimates. Completion means the requested outcome holds on the resulting artifact, not that every planned edit was made.

Capture the relevant starting state before changing it. Prefer existing checks and a focused reproduction. If a new check is needed, ensure it can distinguish the starting behavior from the intended outcome. Do not require a new harness for every task. Record any unavailable baseline as a limitation.

## Choose and execute units

Keep a short phase list in the conversation or available planning surface. For each unit, identify its dependency, owner, affected files or shared resources, expected result, and observable check. Address consequential uncertainty early without skipping blocking foundations. Use the existing design, experiment, and parallel-work guidance only when their conditions apply.

Implement and check each useful unit before relying on it. Separate verified results, observed failures, and inconclusive checks. A unit can pass while the overall outcome remains incomplete. For delegated work, inspect the artifact and evidence before integration; a worker's completion report is not verification.

## Check progress and revise

Use [decision-trail guidance](decision-trail.md) when consequential choices or changing assumptions need a recoverable record. Keep it in the conversation unless a separate artifact is requested.

At meaningful phase boundaries, report completed outcomes, verification evidence, changed assumptions, and the next unit. Keep routine updates brief. Continue authorized work without turning each checkpoint into an approval request.

When evidence changes the plan, explain the cause and revise the remaining units. Diagnose failed checks using the implementation sequence. Repeated attempts without new evidence should trigger examination of the premise or observation method. Preserve useful, correct partial work; discard only task-owned experimental changes that failed their stated criteria.

If progress requires unavailable evidence, a product decision, or work outside authorization, identify the specific dependency and complete independent work where possible. Do not lower completion criteria to manufacture success. On an explicit pause or interruption, preserve a handoff with current artifacts, completed checks, unresolved dependencies, and the next action. Save a separate record only when requested.

## Continue across phases

Track each unit as pending, active, verified, or blocked, with its current artifact and relevant evidence. Distinguish code completion from integration and delivery. Record ownership changes and outstanding work before relying on a replacement worker. Use the parallel-work reference when delegation is justified; a single owner needs no orchestration registry.

For dependent branches or PRs, record the actual base and prerequisite revision. Do not assume the default branch or create commits and PRs merely to represent phases. Recheck affected evidence when a prerequisite changes. Use shipping guidance only when delivery is requested.

For a requested sustained run, state a checkable exit condition and applicable limits before continuing. Continue authorized units while useful progress is possible. Reevaluate remaining work against the outcome rather than repeating the same failed action. An autonomy request does not authorize unrelated work, bypass a required decision, or grant merge and deployment permission.

Use host-supported continuation or event observation only when requested and available. Otherwise work within the active session and preserve unfinished state honestly. Do not promise work will continue after the session ends or invent a scheduler. An explicit pause stops further task writes; preserve the current state with a handoff instead of starting another unit.

## Verify the whole

After integrating the units, check the original completion criteria and affected behavior on the combined artifact. Earlier unit checks do not establish integration correctness. Report what passed, what failed, and what remains unexercised. If required work remains, describe the continuation rather than declaring completion. This guidance does not authorize commits, publishing, or background automation.
