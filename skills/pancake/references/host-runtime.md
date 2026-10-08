# Active host boundary

Read this reference before applying delegated model or effort choices. Keep the shared workflows and review requirements the same on both hosts.

## Task choices

Direct work uses the current conversation settings. Delegates inherit the active host's settings by omitting model and effort overrides. Apply an override only when explicitly requested for this task and supported by the exposed interface. An omitted or null choice means inheritance. Do not discover models through a bundled helper or read, create, migrate, or delete saved Pancake preference files.

Identify the active client from its tools or explicit session context, not PATH or inherited environment variables. Use choices visible in the active tool metadata or supplied by the user. If available choices cannot be observed, say so; do not invent model IDs or treat a supplied choice as confirmed support. Setup may help the user express task choices without saving them.

A nonempty task-supplied reviewer list selects one reviewer per entry. An absent or explicitly empty list uses the workflow's default review requirement. Explicit limits on delegation take precedence. Keep unsupported requested entries as coverage gaps instead of silently replacing them.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. If selecting a worker model or effort requires a fresh context, use that supported invocation instead of a full-history fork that cannot accept overrides. Use Claude Code's native model selection when available; do not assume a full model ID is accepted by a tool expecting aliases. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Distinguish requested settings from what the host accepted or reported. Unknown inherited settings remain unknown. Unsupported or failed panel entries remain uncovered. Keep one reviewer per selected entry, completed per-reviewer verdicts, and bounded concurrency. Direct sequential passes do not establish independent review.

## Reviewer context

For Challenge and implementation review, create a new reviewer with only the neutral task brief, target revision or workspace snapshot, relevant source pointers, user requirements, and applicable permissions and repository instructions. Exclude the lead's suspected findings and other reviewers' conclusions from both the brief and inherited history. Do not reuse an implementation worker or an agent already exposed to those assessments as an independent reviewer.

When the exposed Codex collaboration tool supports `fork_turns`, use `fork_turns="none"` for reviewers. On other hosts, use the available fresh-agent context control; do not invent an argument or assume that a new agent name clears history. Context isolation is separate from model and effort inheritance, which still follow task choices above.

If the host cannot provide a fresh context or its isolation cannot be established, disclose that limit. A review exposed to prior assessments can supply additional findings but does not satisfy independent-review coverage. Complete permitted direct review and report the gap rather than claiming independence or changing global host settings.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. Both load the same installed workflow tree. Resolve references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
