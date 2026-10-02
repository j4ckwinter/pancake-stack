---
name: pancake
description: Apply proportionate rigor to a software task. Use when the user invokes pancake or explicitly requests a rigorous investigation, implementation, or review.
---

# Work with rigor

Read [core values](references/values.md), [sift](../sift/SKILL.md), and applicable repository instructions. Apply sift while drafting progress updates, explanations, authorized written artifacts, and final replies. Keep the requested outcome and scope explicit. For substantial work, maintain a short plan whose steps end in observable checks. Handle small tasks directly.

## Choose the work

- For runtime symptoms or captured profiling artifacts, read [forensics guidance](references/forensics.md). Keep a diagnosis separate from repair unless both are requested.
- For performance experiments, prototypes that settle observable questions, or skill evaluations, read [measured experiments](references/experiments.md). Use it only when the requested work authorizes the experiment.
- For requested retrospectives and durable lessons, read [reflect](../reflect/SKILL.md). Do not run it automatically after every task.
- For ticket clarification and implementation briefs, read [scope](../scope/SKILL.md).
- For execution-flow explanations, read [how](../how/SKILL.md).
- For historical rationale and design motivation, read [why](../why/SKILL.md).
- For proving requested behavior, read [verify](../verify/SKILL.md).
- For adversarial review of contested decisions or consequential assumptions, read [challenge](../challenge/SKILL.md).
- For change reviews, read [check](../check/SKILL.md).
- For design proposals and consequential architecture choices, read [design](../design/SKILL.md).
- For authorized implementation, read [the implementation sequence](references/implementation.md). It covers grounding, design choices, implementation, proportional review, verification, and failure handling.

Read only the workflow needed for the task. Do not run every workflow in sequence. A scope brief, review, explanation, or design proposal remains read-only unless edits are requested.

## Preferences and agents

Read saved preferences with `python3 <installed-setup-directory>/scripts/preferences.py resolve`, using the [setup helper](../setup/scripts/preferences.py). Resolve paths relative to this installed skill, not the user's workspace. Supply host model and effort arguments only when those values are observable. Missing preferences inherit from the host. If reading fails, report the limitation and preserve the file.

Use implementation preferences for writing code, review preferences for reviewing, and research preferences for investigation. Apply a supported model and reasoning effort only when the host exposes a capability to select them for the intended work. The helper reads preferences; it does not apply them. Do not switch the parent conversation, write global settings, or claim an override was applied when it was not. If an explicit preference cannot be applied, state that briefly and use the current host settings. An unresolved null remains inheritance, not a guessed model or effort.

When starting work with an explicit preference, distinguish the resolved request from what the host actually selected. Report model and effort separately when one applies and the other does not. Claim application only from the host's supported invocation or reported selection, not from helper output or catalog availability. If selection is rejected, report the affected preference and the observed fallback; do not silently substitute a different model. Give this notice once for the affected role unless the selection changes. Ordinary inheritance needs no repeated setup explanation.

For justified candidate comparisons or independent workstreams, read [parallel work](references/parallel-work.md). Use the current agent by default. Delegate only when an independent review or separable investigation materially helps and host capabilities permit it. Keep writes isolated and review delegated results. Do not add agents simply to satisfy a fixed count or describe same-model reviews as a multi-model panel.

## Finish

For implementation, finish or preserve unfinished work as described in [the implementation sequence](references/implementation.md). For other tasks, inspect the resulting artifact and use checks appropriate to the deliverable. Lead with the outcome, then explain material decisions, verification, and remaining gaps. Stop when the authorized outcome is complete. Do not commit, publish, or install the plugin unless requested.
