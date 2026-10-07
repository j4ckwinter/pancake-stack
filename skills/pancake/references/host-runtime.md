# Active host boundary

Read this reference before applying delegated model or effort choices. Keep the shared workflows and review requirements the same on both hosts.

## Task choices

Direct work uses the current conversation settings. Delegates inherit the active host's settings by omitting model and effort overrides. Apply an override only when explicitly requested for this task and supported by the exposed interface. An omitted or null choice means inheritance. Do not discover models through a bundled helper or read, create, migrate, or delete saved Pancake preference files.

Identify the active client from its tools or explicit session context, not PATH or inherited environment variables. Use choices visible in the active tool metadata or supplied by the user. If available choices cannot be observed, say so; do not invent model IDs or treat a supplied choice as confirmed support. Setup may help the user express task choices without saving them.

A nonempty task-supplied reviewer list selects one reviewer per entry. An absent or explicitly empty list uses the workflow's default review requirement. Explicit limits on delegation take precedence. Keep unsupported requested entries as coverage gaps instead of silently replacing them.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. If selecting a worker model or effort requires a fresh context, use that supported invocation instead of a full-history fork that cannot accept overrides. Use Claude Code's native model selection when available; do not assume a full model ID is accepted by a tool expecting aliases. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Distinguish requested settings from what the host accepted or reported. Unknown inherited settings remain unknown. Unsupported or failed panel entries remain uncovered. Keep one reviewer per selected entry, completed per-reviewer verdicts, and bounded concurrency. Direct sequential passes do not establish independent review.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. Both load the same installed workflow tree. Resolve references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
