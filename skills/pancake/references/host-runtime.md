# Active host boundary

Read this reference before applying delegated model or effort choices. Keep the shared workflows and review requirements the same across supported hosts.

## Task choices

Direct work uses the current conversation settings. Delegates inherit the active host's settings by omitting model and effort overrides. Apply an override only when explicitly requested for this task, or for [gathering delegates](#gathering-delegates) under a named economy model, and only when the exposed interface supports it. An omitted or null choice means inheritance, which needs no setup explanation. Do not discover models through a bundled helper or read, create, migrate, or delete saved Pancake preference files.

Identify the active client from its tools or explicit session context, not PATH or inherited environment variables. Use choices visible in the active tool metadata or supplied by the user. If available choices cannot be observed, say so; do not invent model IDs or treat a supplied choice as confirmed support. Setup may help the user express task choices without saving them.

A nonempty task-supplied reviewer list selects one reviewer per entry. An absent or explicitly empty list uses the workflow's default review requirement. Explicit limits on delegation take precedence. Keep unsupported requested entries as coverage gaps instead of silently replacing them.

Without a nonempty list, an explicitly requested reviewer count selects that many independent reviewers with inherited settings unless model diversity was requested.

An explicit request for multi-model review without a nonempty model list authorizes selecting two distinct models from the active host's exposed choices. Honor any requested reviewer count, model constraints, and effort. Announce the selected models before launching. If enough distinct supported choices cannot be established, report the diversity gap and complete the permitted review without inventing or silently substituting models. A request for multiple reviewers alone retains model inheritance.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. If selecting a worker model or effort requires a fresh context, use that supported invocation instead of a full-history fork that cannot accept overrides. Use Claude Code's native model selection when available; do not assume a full model ID is accepted by a tool expecting aliases. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Record requested settings and what the host accepted or reported for each delegate. Report unsupported or rejected selections and observed fallback when material. Unknown inherited settings remain unknown. Do not silently substitute settings or providers. Unsupported or failed entries remain uncovered; retry only when the observed failure supports a bounded retry.

## Gathering delegates

A gathering delegate is read-only and returns located facts for the lead to check. Its work is bulk reading, searching, inventories, fetching pages, and tracing existing behavior to explain it. A delegate that writes or edits a deliverable, runs checks or experiments, investigates a defect or diagnoses a cause, recommends or judges an approach, or reviews a change is not a gathering delegate. Reviewers, candidates and judges of any comparison, and implementation workers follow the task choices above. This section does not request delegation; [parallel work](parallel-work.md) decides whether to delegate.

An economy model is one that the task, or user or repository instructions the host has loaded, names for gathering delegates on the active host. When one is named, launch gathering delegates with it through the supported per-delegate control. Never select a cheaper model on your own judgment. A request for a cheaper model without a name leaves gathering delegates inherited; say that a name is needed. Naming an economy model chooses nothing for any other delegate or for the conversation; their models follow the task choices above, including an explicit choice that names the same model. A task statement about gathering delegates or about all delegates takes precedence over a standing economy model. If the host rejects or cannot apply the economy model, the gathering delegate inherits instead of remaining uncovered; report the request and the fallback.

Give each gathering delegate a bounded question. Prohibit edits, nested delegation, installations, services, and external writes. Require a source location for every claim, the scope searched, and the queries used. Inspect the decisive locations before relying on the result, which describes only the scope it reports. Before a consequential change relies on a complete inventory, confirm completeness directly or with an inherited delegate, and report how. When a result fails inspection or omits required evidence, rerun that slice once with inherited settings instead of retrying the economy model. When an economy model was requested, report each gathering delegate's requested model, its observed model or that the host did not report one, and any rerun.

## Independent review execution

Apply this protocol when Challenge, Check, or implementation calls for independent review. The calling workflow determines when review is required and its default reviewer count; reading this reference does not itself request delegation. An assigned reviewer returns its own findings without launching another panel.

Resolve the panel from the task choices above, then launch one independent read-only reviewer per selected entry through working, permitted host delegation. Otherwise use the calling workflow's default. Queue reviewers within host concurrency limits. Track each selected entry, its returned agent identity, and its completed verdict separately. Verify identity-bearing completion and retain each actual verdict before declaring the panel complete. A generic wait completion, another reviewer's result, a progress message, or a read of a review skill does not establish completion. Interrupted reviewers without verdicts remain uncovered.

Give every reviewer the same neutral objective, target revision or workspace snapshot, relevant source pointers, user requirements, evidence requirements, and applicable permissions and repository instructions. Ask for concrete triggers, consequences, inspected locations, and uncertainty. Prohibit edits, nested delegation, dependency installation, services, and external actions. If the target changes, identify the coverage mismatch and review the affected correction before relying on earlier findings.

## Reviewer context

Create a new reviewer without inherited conversation history. Exclude the lead's suspected findings and other reviewers' conclusions from both the brief and history. Do not reuse an implementation worker or an agent already exposed to those assessments as an independent reviewer.

When the exposed Codex collaboration tool supports `fork_turns`, use `fork_turns="none"` for reviewers. On other hosts, use the available fresh-agent context control; do not invent an argument or assume that a new agent name clears history. Context isolation is separate from model and effort inheritance, which still follow task choices above.

If the host cannot provide a fresh context or its isolation cannot be established, disclose that limit. A review exposed to prior assessments can supply additional findings but does not satisfy independent-review coverage. Complete permitted direct review and report the gap rather than claiming independence or changing global host settings.

## Review coverage

If delegation is unavailable, outside task permissions, or yields no completed independent reviewer, perform permitted direct review and report the concrete independence gap. Multiple passes by one agent are not independent review. Continue with completed evidence when part of a panel fails; unsupported, failed, and incomplete entries remain uncovered.

Claim model diversity only when completed reviewers or design candidates have distinct actual model IDs. Same-model reviewers, including different efforts, provide independent reviews without model diversity. Different models from one provider do not establish provider diversity.

For a panel, report each reviewer's requested model, accepted or observed model, completion status, and supported findings. Keep unknown settings explicit. Inspect each finding against the target, rerun a decisive safe check when available, and deduplicate by failure mechanism. Keep supported lone-reviewer findings. Resolve disagreements with evidence rather than vote counts, and report material unresolved disagreements and missing coverage. A panel request does not authorize fixes or new reproduction files.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. In Cursor, type `/` and select the skill by name from the picker; do not assume Codex or Claude namespaced syntax. All hosts load the same installed workflow tree. Resolve references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Cursor project skills can live in `.cursor/skills/<name>/SKILL.md` or `.agents/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
