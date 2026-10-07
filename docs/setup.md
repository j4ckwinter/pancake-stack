# Set up a task

No setup is required to inherit the active host's settings. Invoke `$pancake-stack:setup` in Codex or `/pancake-stack:setup` in Claude Code when you want help expressing delegate or reviewer choices for a task.

Setup uses choices visible in the active host or supplied by you. It does not launch a model-discovery process, save preferences, change the current model, or start reviewers. When supported choices are unknown, it explains the limitation instead of inventing model IDs.

For example:

> $pancake-stack:setup Help me phrase an implementation task with two independent reviewers. Both should inherit the active host's model and effort.

Use the resulting wording in your task request. You can also supply choices directly to Pancake, Challenge, or Design. Choices explicitly adopted in the current conversation apply to the named task. Repeat them in a new chat when needed.

See [task settings](configuration.md) for panel defaults, unsupported choices, and migration from saved preferences. See [verification](verification.md) for external checks and historical evidence limits.
