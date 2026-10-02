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

Use independent read-only reviewers when the consequences and available host capabilities justify them. Give each the same target, intended outcome, constraints, and evidence requirements. Ask them to inspect the source independently and return triggers, consequences, inspected locations, and uncertainty. Do not seed them with the lead's suspected answer. Bound concurrency to host limits and prohibit edits and external actions.

Respect Pancake's existing review preference when a supported host capability can apply it. Standalone challenge uses the current agent settings unless the user supplies supported choices; it does not change preferences or require setup. Do not invent model IDs, switch the parent model, or select extra providers without authorization. Different model perspectives are useful only when actually available and selected. If delegation is unavailable, review directly and disclose the lack of independence. Multiple passes by one agent are not independent reviewers.

## Judge the evidence

Inspect the evidence behind findings rather than tallying votes. Deduplicate reports of the same mechanism. Agreement can suggest where to investigate; it does not prove correctness. A lone finding can be decisive when its evidence holds. Resolve disagreements by checking the disputed contract or trigger, or leave the uncertainty explicit.

Classify useful findings as act on, consider, or unresolved. Act on means a supported issue materially threatens the stated outcome; consider means a real tradeoff whose benefit may not justify changing the approach; unresolved means evidence needed for a conclusion is missing. Reject disproved or out-of-scope claims and explain noteworthy dismissals without filling the answer with noise.

Lead with the verdict and strongest actionable findings. For each, give the assumption challenged, concrete trigger, consequence, evidence, and cheapest useful next check or correction. For proposals, cite the relevant proposal passage or assumption; for code, link inspected locations. Report review scope, actual reviewer independence, and material coverage gaps. If no actionable issue survives, say so without claiming the approach is proven safe. Stop at the verdict unless further work was authorized.
