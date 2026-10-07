# Explore competing designs

Use this mode only when the user explicitly requests independent competing-design exploration or supplies candidate model choices with optional task effort. Keep ordinary Design for a request merely to compare alternatives. A design request remains read-only; exploration does not authorize implementation, preference writes, dependency installation, services, or external actions.

## Establish the comparison

Inspect the relevant implementation and contracts first. Freeze the target revision or workspace snapshot, including relevant local changes, and give all candidates the same source pointers. Record the outcome, hard constraints, and comparison criteria before launching agents. Include the existing design as the baseline, identifying any requirement it already fails.

Choose concrete criteria tied to the task. Examples include acceptance behavior, compatibility, validation and ownership boundaries, failure recovery, consumer experience, maintenance burden, migration scope, and verification cost. Distinguish hard constraints from tradeoffs. Do not invent numerical precision or requirements to favor an approach.

Prepare one neutral brief with the same baseline, criteria, constraints, and evidence requirements for every candidate. Ask for a usage example, data shape and ownership, affected contracts, material tradeoffs, failure behavior, and verification plan. Require structurally different alternatives rather than cosmetic variations. If independent proposals converge, report that convergence and compare the shared approach with the baseline. Do not claim distinct architectural coverage or manufacture a difference merely to fill the comparison. Do not supply the lead's preferred design or another candidate's answer.

## Request independent candidates

Read [active host guidance](../../pancake/references/host-runtime.md) before using preference helpers or delegated settings. On Claude Code, add `--host claude` before every helper subcommand.

When preparing delegates with supported model selection, resolve existing role models using `python3 <installed-setup-directory>/scripts/preferences.py resolve`, with the [setup helper](../../setup/scripts/preferences.py). Resolve its location relative to this installed skill, not the workspace. For an explicitly requested preference location or isolated verification, pass `--config <path>` before `resolve`. Supply host model and effort arguments only when observable. Candidates inherit research model preferences; the judge inherits review model preferences. A read failure leaves those preferences unavailable; report it and preserve the file.

Explicit task-supplied candidate and judge models need no saved preference lookup, even when effort is omitted. When delegation is unavailable, compare directly using current host settings without resolving saved roles. Task choices apply only to this invocation. Resolve omitted or null models through the relevant role, defaults, then observable host model only when supported model selection needs them. Omit effort to inherit from the host unless explicitly requested for this task. Saved effort is inactive; resolved host effort is informational. Do not persist choices or switch the parent conversation. Without supplied candidate choices, request at least two independent candidates using the research model preference. An explicit list with fewer than two entries cannot establish a competing exploration; disclose the gap and use direct Design unless the user supplies the missing choice.

Launch at least two separate read-only candidate agents when delegation is available. Prohibit edits, nested delegation, installations, services, and external actions in their briefs. Queue work within host concurrency limits and await completed proposals. Apply model and effort separately through supported host capabilities. When model diversity is requested, use distinct supported model IDs from actual host metadata when available. Do not invent IDs, silently substitute rejected settings, or treat catalog availability as evidence that delegation applied a choice.

Record requested settings and host-accepted or reported selections. Unknown inheritance remains unknown. Claim model diversity only for distinct actual model IDs of completed candidates. Different efforts on one model and different models from one provider do not establish provider diversity. Unsupported settings, failed agents, or fewer than two completed proposals leave coverage gaps. Retry only when an observed failure supports a bounded retry.

## Judge completed proposals

After candidate outputs stabilize, launch a separate read-only judge that authored none of them. Give it the original neutral brief, frozen target, baseline, comparison criteria, and completed proposals under neutral candidate IDs. Withhold author and model identity, the lead's preference, and other evaluations. Start the judge with a fresh minimal context, without inherited conversation history that reveals those withheld details. Remove identity metadata without changing proposal substance; retain the identity mapping for accurate final reporting. Prohibit edits, nested delegation, installations, services, and external actions.

Ask the judge to inspect decisive claims against source evidence, identify hard-constraint failures, and compare viable proposals with the baseline. Require a recommendation with concrete tradeoffs, inspected locations, uncertainty, and the cheapest useful checks. Agreement and votes are not proof. The baseline may remain preferable if it meets the outcome; a baseline that violates a hard requirement cannot be declared sufficient.

Check the judge's evidence before adopting its recommendation. Resolve consequential disagreements through inspection or authorized experiments, and leave missing evidence explicit. A combined design needs its own coherence check. If the target changed, identify the coverage mismatch and refresh affected inspection before relying on the verdict.

## Report limits

If delegation is unavailable, compare directly and disclose that independent exploration and judging did not run. If fewer than two candidates complete, report an incomplete comparison. If a separate judge cannot complete, the lead may recommend from available evidence while disclosing that independent judging is absent. Multiple passes by the lead are not independent agents.

Report the recommendation, decisive criteria, meaningful rejected alternatives, actual candidate and judge independence, requested versus applied settings when material, and remaining coverage gaps. Keep proposed checks distinct from observed results. Stop at the design unless implementation was also authorized.
