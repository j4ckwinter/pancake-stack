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

## Preferences and agents

Read [active host guidance](references/host-runtime.md) before using preference helpers or delegated settings. On Claude Code, add `--host claude` before every helper subcommand.

Work performed directly in the current conversation uses the current host settings. Do not read saved preferences or report unavailable role overrides merely to start a task. This includes explanations, prose edits, direct implementation, and direct review.

When preparing delegates, follow [active host guidance](references/host-runtime.md) for lookup timing and task overrides. Resolve saved role models with `python3 <installed-setup-directory>/scripts/preferences.py resolve`, using the [setup helper](../setup/scripts/preferences.py) relative to this installed skill. The command returns all roles; select implementation for code delegates, review for reviewers, and research for investigators from the output. Missing model preferences inherit from the host. Delegates inherit host effort unless this task explicitly requests an effort. Preserve the file and report read failures.

Challenge and consequential implementation review own panel discovery at their review stage. Planning review requirements does not require reading preferences.

The helper reads preferences; it does not apply them. Apply saved models only through controls exposed by the active host for the delegate. Omit effort unless explicitly requested for this task. Saved effort is inactive; resolved host effort is informational. Do not switch the parent conversation, write global settings, or claim an override was applied from helper output or catalog availability. An unresolved null remains inheritance, not a guessed model or effort.

When preparing a delegate with an explicit preference, distinguish the requested settings from the host's accepted or reported selection. If a setting is unsupported or rejected, report the affected preference and observed fallback once for that role. Selected reviewer panels retain their coverage rules; unsupported entries remain uncovered. Ordinary inheritance needs no setup explanation.

For justified candidate comparisons or independent workstreams, read [parallel work](references/parallel-work.md). Use the current agent by default. Delegate only when an independent review or separable investigation materially helps and host capabilities permit it. Keep writes isolated and review delegated results. Do not add agents simply to satisfy a fixed count or describe same-model reviews as a multi-model panel.

## Finish

For implementation, finish or preserve unfinished work as described in [the implementation sequence](references/implementation.md). For other tasks, inspect the resulting artifact and use checks appropriate to the deliverable. Lead with the outcome, then explain material decisions, verification, and remaining gaps. Complete the delivery actions authorized by the user's request and context. Resolve any genuine uncertainty about the delivery target before acting. Stop when the authorized outcome is complete.
