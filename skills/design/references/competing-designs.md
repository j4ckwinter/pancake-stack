# Explore competing designs

Use this mode when [Design](../SKILL.md#compare-approaches) selects independent exploration for an unresolved consequential choice, or when the user requests it or supplies candidate model choices. Respect explicit delegation limits and keep settled or small choices direct unless independent exploration was requested.

## Establish the comparison

Inspect the relevant implementation and contracts first. Freeze the target revision or workspace snapshot, including relevant local changes, and give all candidates the same source pointers. Record the outcome, hard constraints, and comparison criteria before launching agents. Include the existing design as the baseline, identifying any requirement it already fails.

Choose concrete criteria tied to the task. Examples include acceptance behavior, compatibility, validation and ownership boundaries, failure recovery, consumer experience, maintenance burden, migration scope, and verification cost. Distinguish hard constraints from tradeoffs. Do not invent numerical precision or requirements to favor an approach.

Prepare one neutral brief with the same baseline, criteria, constraints, and evidence requirements for every candidate. Ask for a usage example, data shape and ownership, affected contracts, material tradeoffs, failure behavior, and verification plan. Require structurally different alternatives rather than cosmetic variations. If independent proposals converge, report that convergence and compare the shared approach with the baseline. Do not claim distinct architectural coverage or manufacture a difference merely to fill the comparison. Do not supply the lead's preferred design or another candidate's answer.

## Request independent candidates

Read [active host guidance](../../pancake/references/host-runtime.md) before applying delegated settings. It owns inheritance, model and effort choices, recorded settings, and diversity claims for candidates and the judge. When model diversity is requested, select distinct models and report any diversity gap as that guidance describes for multi-model review.

Without supplied candidate choices, request at least two independent candidates with inherited settings unless model diversity was requested. An explicit list with fewer than two entries cannot establish a competing exploration; disclose the gap and use direct Design unless the user supplies the missing choice.

Launch at least two separate read-only candidate agents when delegation is available. Prohibit edits, nested delegation, installations, services, and external actions in their briefs. Queue work within host concurrency limits and await completed proposals. Unsupported settings, failed agents, or fewer than two completed proposals leave coverage gaps.

Apply the [reviewer context isolation rules](../../pancake/references/host-runtime.md#reviewer-context) to every candidate as well as the judge. A neutral brief does not remove preferences or earlier proposals from inherited history. When fresh context is unavailable or cannot be established, report the independence gap instead of counting the affected proposal as independent exploration.

## Judge completed proposals

After candidate outputs stabilize, launch a separate read-only judge that authored none of them. Give it the original neutral brief, frozen target, baseline, comparison criteria, and completed proposals under neutral candidate IDs. Withhold author and model identity, the lead's preference, and other evaluations. Start the judge with a fresh minimal context, without inherited conversation history that reveals those withheld details. Remove identity metadata without changing proposal substance; retain the identity mapping for accurate final reporting. Prohibit edits, nested delegation, installations, services, and external actions.

Ask the judge to inspect decisive claims against source evidence, identify hard-constraint failures, and compare viable proposals with the baseline. Require a recommendation with concrete tradeoffs, inspected locations, uncertainty, and the cheapest useful checks. Agreement and votes are not proof. The baseline may remain preferable if it meets the outcome; a baseline that violates a hard requirement cannot be declared sufficient.

Check the judge's evidence before adopting its recommendation. Resolve consequential disagreements through inspection or authorized experiments, and leave missing evidence explicit. A combined design needs its own coherence check. If the target changed, identify the coverage mismatch and refresh affected inspection before relying on the verdict.

## Report limits

If delegation is unavailable, compare directly and disclose that independent exploration and judging did not run. If fewer than two candidates complete, report an incomplete comparison. If a separate judge cannot complete, the lead may recommend from available evidence while disclosing that independent judging is absent. Multiple passes by the lead are not independent agents.

Report the recommendation, decisive criteria, meaningful rejected alternatives, actual candidate and judge independence, requested versus applied settings when material, and remaining coverage gaps.
