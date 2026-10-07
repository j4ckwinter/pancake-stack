---
name: challenge
description: Challenge assumptions in a software design or consequential code change with evidence-based adversarial review. Use for blind spots, contested decisions, or requests to stress-test an approach. Use check for routine diff review.
---

# Challenge the approach

Read [core values](../pancake/references/values.md), [sift](../sift/SKILL.md), and applicable repository instructions. Return a verdict without applying changes unless repair or implementation was separately requested.

## Establish the target

Use the supplied proposal, files, diff, or branch range. For recent local work, inspect staged and unstaged changes and relevant untracked files. For a branch comparison, establish the intended base from available evidence instead of assuming main. If the target cannot be inferred, ask what to challenge. Do not mistake a clean workspace for an absence of committed changes.

State the intended outcome, constraints, and consequential assumptions briefly. Inspect enough implementation and callers to distinguish existing safeguards from proposed ones. A design can be challenged before code exists; label assumptions and proposed contracts accordingly. Do not invent missing requirements to make an approach fail.

## Seek counterexamples

Choose the review questions that matter to this target. Look for a concrete input, state, ordering, failure, or consumer that would invalidate the approach. Consider contract compatibility, data ownership, failure recovery, concurrency, security boundaries, and unnecessary complexity where relevant. Prefer a discriminating counterexample to a generic warning.

Read surrounding code and tests to check whether each suspected issue is already handled. Use focused, safe checks when they can settle a question. Do not modify files, install dependencies, run live external writes, or start services merely to challenge a proposal. When runtime evidence is unavailable, state what static evidence supports and what remains unproved.

## Independent perspectives

When preparing reviewers, follow [active host guidance](../pancake/references/host-runtime.md). Omitted model and effort choices inherit the host. Do not read stored preferences or change the parent conversation settings.

For a nonempty task-supplied panel, spawn one independent read-only reviewer per entry when delegation is available and permitted. Queue reviewers within host concurrency limits and await each completed verdict before synthesizing. For an absent or explicitly empty panel, use independent reviewers when the consequences and available capabilities justify them. A supplied panel requests delegation, not extra passes by the lead.

Give every reviewer the same neutral brief, target snapshot or branch range, intended outcome, constraints, and evidence requirements. Ask each to inspect independently and return triggers, consequences, inspected locations, and uncertainty. Do not seed reviewers with the lead's suspected answer or other reviewers' findings. Prohibit edits, nested delegation, dependency installation, services, and external actions. If the target changes during review, identify the coverage mismatch before using the findings.

Apply requested models through supported host selection. Omit effort to inherit from the host unless explicitly requested for this task. Apply explicit task effort separately when supported. Do not invent model IDs or silently substitute another model, effort, or provider. Record requested settings and what the host actually accepted or reported for each reviewer. An unknown inherited setting remains unknown. An unsupported or failed entry leaves that perspective uncovered; report it and continue with completed evidence. Retry only when the observed failure supports a bounded retry. If delegation is unavailable, review directly and disclose that the panel did not run. Multiple passes by one agent are not independent reviewers.

Claim model diversity only when completed reviewers have distinct actual model IDs. Different reasoning efforts on one model provide independent reviews without model diversity. Different models from one provider do not establish provider diversity. Unknown selections, rejected settings, failed reviewers, and incomplete reviews remain coverage gaps.

## Judge the evidence

Inspect the evidence behind findings rather than tallying votes. Deduplicate reports of the same mechanism. Agreement can suggest where to investigate; it does not prove correctness. A lone finding can be decisive when its evidence holds. Resolve disagreements by checking the disputed contract or trigger, or leave the uncertainty explicit.

Classify useful findings as act on, consider, or unresolved. Act on means a supported issue materially threatens the stated outcome; consider means a real tradeoff whose benefit may not justify changing the approach; unresolved means evidence needed for a conclusion is missing. Reject disproved or out-of-scope claims and explain noteworthy dismissals without filling the answer with noise.

Lead with the verdict and strongest actionable findings. For each, give the assumption challenged, concrete trigger, consequence, evidence, and cheapest useful next check or correction. For proposals, cite the relevant proposal passage or assumption; for code, link inspected locations. Report review scope, actual reviewer independence, and material coverage gaps. If no actionable issue survives, say so without claiming the approach is proven safe. Stop at the verdict unless further work was authorized.
