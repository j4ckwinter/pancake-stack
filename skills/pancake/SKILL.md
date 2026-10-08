---
name: pancake
description: Apply proportionate rigor to a software task. Use when the user invokes pancake or explicitly requests a rigorous investigation, implementation, or review.
---

# Work with rigor

Read [core values](references/values.md), [sift](../sift/SKILL.md), and applicable repository instructions. Apply sift while drafting progress updates, explanations, authorized written artifacts, and final replies. Keep the requested outcome and scope explicit. For substantial work, maintain a short plan whose steps end in observable checks. Handle small tasks directly.

## Choose the work

- For explicitly requested comment cleanup, read [comment-cleanup guidance](references/comment-cleanup.md). A cleanup audit remains read-only unless edits are requested.
- For requested worktree inventory or cleanup, read [worktree-cleanup guidance](references/worktree-cleanup.md). Inventory remains read-only.
- For catching up on a project or recovering prior decisions and unfinished work, read [recap](../recap/SKILL.md). Historical recovery stays scoped to the requested project and topic.
- For requested task pickup or an explicit pause, read [handoff](../handoff/SKILL.md) and its continuation guidance.
- For requested commits, merges, releases, publication, deployment, or delivery preparation, read [shipping guidance](references/shipping.md).
- For requested PR status, feedback triage, or merge-readiness work, read [PR-maintenance guidance](references/pr-maintenance.md). A status request remains read-only.
- For matching an interface or preserving appearance during a migration, read [visual-parity guidance](references/visual-parity.md).
- For runtime symptoms or captured profiling artifacts, read [forensics guidance](references/forensics.md). Keep a diagnosis separate from repair unless both are requested.
- For performance experiments, prototypes that settle observable questions, or skill evaluations, read [measured experiments](references/experiments.md). Use it only when the requested work authorizes the experiment.
- For requested retrospectives and durable lessons, read [reflect](../reflect/SKILL.md). Do not run it automatically after every task.
- For ticket clarification and implementation briefs, read [scope](../scope/SKILL.md).
- For guided learning or understanding a concept at the reader's pace, read [teach](../teach/SKILL.md).
- For execution-flow explanations, read [how](../how/SKILL.md).
- For historical rationale and design motivation, read [why](../why/SKILL.md).
- For proving requested behavior, read [verify](../verify/SKILL.md).
- For adversarial review of contested decisions or consequential assumptions, read [challenge](../challenge/SKILL.md). Challenge consumes its optional reviewer panel and delegates one reviewer per selected entry when supported.
- For change reviews, read [check](../check/SKILL.md).
- For explicitly requested structural or code-quality reviews, read [structural-quality guidance](../design/references/structural-quality.md). Review remains read-only unless edits are requested.
- For design proposals and consequential architecture choices, read [design](../design/SKILL.md).
- For explicitly requested test-first development or regression tests, read [tdd](../tdd/SKILL.md). Keep the failing-test step before production changes.
- For authorized implementation, read [the implementation sequence](references/implementation.md). It covers grounding, design choices, implementation, proportional review, verification, and failure handling.

Read only the workflow needed for the task. Do not run every workflow in sequence. A scope brief, review, explanation, or design proposal remains read-only unless edits are requested.

## Agents and task choices

Direct work uses the current conversation settings. Delegates inherit the active host's model and effort unless the user supplies explicit choices for this task. Do not read or write stored Pancake preferences, run model-discovery helpers, or change global host settings.

Before applying delegated settings, read [active host guidance](references/host-runtime.md). Use only the controls exposed by the active host. An explicit task choice is a request, not proof of application. Report unsupported or rejected selections and observed fallback when material. Selected reviewer panels retain their coverage rules; unsupported entries remain uncovered. Ordinary inheritance needs no setup explanation.

Challenge and consequential implementation review select their task-supplied panels at review time. Without a supplied panel, follow each workflow's default review requirement. Setup can help phrase choices for the current task; it does not persist them.

For substantial work, read [parallel work](references/parallel-work.md) during planning and launch useful independent assignments early when host capabilities and task permissions permit it. Split investigations or implementation into bounded assignments while the lead advances another part. Keep small tasks and tightly coupled work in the current agent. Do not add agents simply to satisfy a fixed count. Existing independent-review requirements still apply; an implementation worker does not replace its independent reviewer.

Make delegation visible with a brief update naming each agent's assignment and what the lead will handle. Launch through the host's actual delegation tool, and report an agent as started only after the tool confirms it. Summarize completed findings and material gaps as results arrive. Do not promise a particular host UI indicator or describe same-model reviews as a multi-model panel.

## Finish

For implementation, finish or preserve unfinished work as described in [the implementation sequence](references/implementation.md). For other tasks, inspect the resulting artifact and use checks appropriate to the deliverable. Lead with the outcome, then explain material decisions, verification, and remaining gaps. Complete the delivery actions authorized by the user's request and context. Resolve any genuine uncertainty about the delivery target before acting. Stop when the authorized outcome is complete.
