# Substantial work

Read this when authorized implementation spans dependent phases, many callers, or material uncertainty. Use the existing implementation sequence for ordinary changes. This reference adds checkpoints to that sequence.

## Frame the outcome

State what must be observably true when the task is complete, which behavior must remain intact, and which actions are authorized. Identify the affected units, prerequisites, consequential unknowns, and available verification. Estimate scope from inspected evidence; label uncertain estimates. Completion means the requested outcome holds on the resulting artifact, not that every planned edit was made.

Capture the relevant starting state before changing it. Prefer existing checks and a focused reproduction. If a new check is needed, ensure it can distinguish the starting behavior from the intended outcome. Do not require a new harness for every task. Record any unavailable baseline as a limitation.

## Choose and execute units

Keep a short phase list in the conversation or available planning surface. For each unit, identify its dependency, expected result, and observable check. Address consequential uncertainty early without skipping blocking foundations. Use the existing design, experiment, and parallel-work guidance only when their conditions apply.

Implement and check each useful unit before relying on it. Separate verified results, observed failures, and inconclusive checks. A unit can pass while the overall outcome remains incomplete. For delegated work, inspect the artifact and evidence before integration; a worker's completion report is not verification.

## Check progress and revise

At meaningful phase boundaries, report completed outcomes, verification evidence, changed assumptions, and the next unit. Keep routine updates brief. Continue authorized work without turning each checkpoint into an approval request.

When evidence changes the plan, explain the cause and revise the remaining units. Diagnose failed checks using the implementation sequence. Repeated attempts without new evidence should trigger examination of the premise or observation method. Preserve useful, correct partial work; discard only task-owned experimental changes that failed their stated criteria.

If progress requires unavailable evidence, a product decision, or work outside authorization, identify the specific dependency and complete independent work where possible. Do not lower completion criteria to manufacture success. On an explicit pause or interruption, preserve a handoff with current artifacts, completed checks, unresolved dependencies, and the next action. Save a separate record only when requested.

## Verify the whole

After integrating the units, check the original completion criteria and affected behavior on the combined artifact. Earlier unit checks do not establish integration correctness. Report what passed, what failed, and what remains unexercised. If required work remains, describe the continuation rather than declaring completion. This guidance does not authorize commits, publishing, or background automation.
