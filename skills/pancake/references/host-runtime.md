# Active host boundary

Read this reference before applying delegated model or effort choices. Keep the shared workflows and review requirements the same on both hosts.

## Task choices

Direct work uses the current conversation settings. Delegates inherit the active host's settings by omitting model and effort overrides. Apply an override only when explicitly requested for this task and supported by the exposed interface. An omitted or null choice means inheritance. Do not discover models through a bundled helper or read, create, migrate, or delete saved Pancake preference files.

Identify the active client from its tools or explicit session context, not PATH or inherited environment variables. Use choices visible in the active tool metadata or supplied by the user. If available choices cannot be observed, say so; do not invent model IDs or treat a supplied choice as confirmed support. Setup may help the user express task choices without saving them.

A nonempty task-supplied reviewer list selects one reviewer per entry. An absent or explicitly empty list uses the workflow's default review requirement. Explicit limits on delegation take precedence. Keep unsupported requested entries as coverage gaps instead of silently replacing them.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. If selecting a worker model or effort requires a fresh context, use that supported invocation instead of a full-history fork that cannot accept overrides. Use Claude Code's native model selection when available; do not assume a full model ID is accepted by a tool expecting aliases. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Record requested settings and what the host accepted or reported for each delegate. Unknown inherited settings remain unknown. Do not silently substitute settings or providers. Unsupported or failed entries remain uncovered; retry only when the observed failure supports a bounded retry.

## Independent review execution

Apply this protocol when Challenge or implementation calls for independent review. The calling workflow determines when review is required and its default reviewer count; reading this reference does not itself request delegation.

For a nonempty task-supplied panel, launch one independent read-only reviewer per entry through working, permitted host delegation. Otherwise use the calling workflow's default. Queue reviewers within host concurrency limits. Track each selected entry, its returned agent identity, and its completed verdict separately. Verify identity-bearing completion and retain each actual verdict before declaring the panel complete. A generic wait completion, another reviewer's result, a progress message, or a read of a review skill does not establish completion. Interrupted reviewers without verdicts remain uncovered.

Give every reviewer the same neutral objective, target revision or workspace snapshot, relevant source pointers, user requirements, evidence requirements, and applicable permissions and repository instructions. Ask for concrete triggers, consequences, inspected locations, and uncertainty. Prohibit edits, nested delegation, dependency installation, services, and external actions. If the target changes, identify the coverage mismatch and review the affected correction before relying on earlier findings.

## Reviewer context

Create a new reviewer without inherited conversation history. Exclude the lead's suspected findings and other reviewers' conclusions from both the brief and history. Do not reuse an implementation worker or an agent already exposed to those assessments as an independent reviewer.

When the exposed Codex collaboration tool supports `fork_turns`, use `fork_turns="none"` for reviewers. On other hosts, use the available fresh-agent context control; do not invent an argument or assume that a new agent name clears history. Context isolation is separate from model and effort inheritance, which still follow task choices above.

If the host cannot provide a fresh context or its isolation cannot be established, disclose that limit. A review exposed to prior assessments can supply additional findings but does not satisfy independent-review coverage. Complete permitted direct review and report the gap rather than claiming independence or changing global host settings.

## Review coverage

If delegation is unavailable, outside task permissions, or yields no completed independent reviewer, perform permitted direct review and report the concrete independence gap. Multiple passes by one agent are not independent review. Continue with completed evidence when part of a panel fails; unsupported, failed, and incomplete entries remain uncovered.

Claim model diversity only when completed reviewers have distinct actual model IDs. Same-model reviewers, including different efforts, provide independent reviews without model diversity. Different models from one provider do not establish provider diversity.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. Both load the same installed workflow tree. Resolve references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
