---
name: setup
description: Help choose task-scoped delegate and reviewer settings using the active host. Use for Pancake Stack setup without saving preferences.
---

# Set up a task

Read [active host guidance](../pancake/references/host-runtime.md). Setup is a conversation guide. It runs no bundled scripts and writes no preferences or host settings.

Explain that direct work uses the current conversation settings and delegates inherit the active host's settings by default. No setup is required for inheritance. Accept choices already supplied by the user. Ask only for a missing choice needed for their requested customization; do not turn ordinary setup into a questionnaire about every role or panel.

Use model choices visible in the current host's exposed tool metadata or supplied by the user. If supported choices are unavailable, explain the limit and retain inheritance unless the user specifies an override. Do not query a separate CLI, guess model IDs, or claim that a visible choice was applied. Effort also inherits unless explicitly requested for the task.

For a requested reviewer panel, help phrase the reviewer count and any model or effort choices in the task request. Distinguish Challenge reviewers from consequential implementation reviewers. A nonempty task list requests one reviewer per entry. An empty or absent implementation panel retains the single independent reviewer for consequential changes. Ordinary low-impact work still allows direct review.

Return a concise task instruction the user can use, including supplied choices and any unresolved host limitation. Choices explicitly adopted in the current conversation apply to the specified task. Do not imply they persist across chats. Setup alone does not authorize launching reviewers or implementing the task.

If asked to save defaults or load an older profile, explain that persistent Pancake preferences were removed in 0.20.0. Offer the equivalent task wording. Leave existing files untouched and do not simulate persistence with improvised scripts or configuration edits. See [configuration](../../docs/configuration.md) for the migration boundary.
