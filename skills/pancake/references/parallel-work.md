# Compare candidates and coordinate work

Use this reference for substantial work with independent investigation or implementation slices, or for justified competing solutions. When delegation is permitted and available, assign useful independent slices to agents by default. Keep small or tightly coupled work direct when coordination would cost more than it saves. A slice is independent when an agent can finish it from available inputs while the lead works elsewhere. No fixed agent count, provider mix, or background infrastructure is required.

Split an investigation by question or subsystem. Delegate implementation as bounded changes with exclusive ownership, and keep dependent work sequential until its prerequisite is ready. A read-only slice that only returns located facts for the lead to check is gathering work; [host guidance](host-runtime.md#gathering-delegates) owns its settings. Do not turn an ordinary investigation into competing designs or a reviewer panel unless that workflow applies.

## Brief and isolate

Open each brief with the goal. Then give the assignment, relevant source pointers, the exact revision or workspace snapshot, the write scope or read-only scope, the checks to run, and the result expected back. Point to files instead of pasting them. Workers inherit task permissions and may not expand them.

Each brief carries these rules even when it does not repeat them:

- The checks in the brief are the whole bar. Add no extra gate, review round, or sign-off.
- Report what was done or inspected, the checks that ran and their results, and remaining gaps. A check not run is reported as not run.
- Do not ask the user a question. Make a reversible choice within scope and say why; stop for anything outside scope or needing authorization.
- A brief for a further agent opens with the goal and carries these rules on.

Isolate data directories, ports, and other mutable state as well as files; disjoint files are not enough when tests share an instance or database. Run competing code candidates in separate worktrees or scratch copies from the same baseline, including task-relevant local changes. If isolation cannot be established, keep workers read-only or sequential and say so.

Respect user limits and actual host concurrency, and queue work beyond it. Use the host's delegation tool after briefly stating the assignments and the lead's own work. Confirm launches before saying agents started. Continue independent work while they run, and report results, failures, or changed assignments without narrating polling. If delegation is unavailable or prohibited, work directly and note the limit when it matters.

## Cookoff

Design exploration selected by [Design](../../design/SKILL.md#compare-approaches), requested explicitly, or selected through task-supplied candidates follows [competing designs](../../design/references/competing-designs.md), which owns candidate isolation and the separate judge. For other comparisons, state a small rubric before generating candidates, give every candidate the same objective, constraints, and baseline without a preferred answer, and require an artifact or proposal with its evidence. Do not run competing production edits for a design-only request.

Judge stable results by correctness, contract fit, maintainability, and the rubric, running comparable checks when authorized. Scores and agreement are not proof. Pick a coherent base, take another candidate's idea only when it fits that base, and verify the combined result.

## Partitioned work

Track owners, returned artifacts, and uncovered work in the plan. Inspect each result before integrating it, resolve conflicting assumptions against the source, and verify the combined result. A failed or missing result leaves its slice uncovered; most workers succeeding is not completion.

## Finish and recover

Give a retry, fix round, or follow-up to a fresh agent with the original brief, later directions, and the prior report. Resume an existing agent only when the work needs state that lives in it, such as its uncommitted changes or a running process. Retry only when the cause is understood.

If scope or dependencies change, update ownership before continuing. Stop obsolete workers through actual host controls and inspect their output before replacing them; interruption does not discard edits. Preserve unfinished work with [handoff](../../handoff/SKILL.md).

Integrate authorized changes without disturbing unrelated work, then review and verify the combined artifact through [the implementation sequence](implementation.md). Measurement comparisons use [measured experiments](experiments.md). Report the result, actual review independence, selection rationale or coverage, verification, and gaps. Clean up only owned temporary resources; do not delete worktrees, publish branches, or commit to finish an orchestration checklist.

Before applying delegated model or effort choices, read [active host guidance](host-runtime.md). Independent implementation review follows [change review](change-review.md); an implementation worker cannot replace its independent reviewer.
