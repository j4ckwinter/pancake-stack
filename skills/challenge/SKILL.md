---
name: challenge
description: Challenge assumptions in a software design or consequential code change with evidence-based adversarial or multi-model review. Use for interrogate-style reviews, blind spots, contested decisions, or requests to stress-test an approach. Use check for routine diff review.
---

# Challenge the approach

Read [core values](../pancake/references/values.md), [sift](../sift/SKILL.md), and applicable repository instructions.

## Establish the target

Use the supplied proposal, files, diff, or branch range. For recent local work, include staged, unstaged, and relevant untracked changes; for a branch, establish the base from evidence instead of assuming main. A clean workspace does not mean there are no committed changes. If the target cannot be inferred, ask what to challenge.

State the intended outcome, constraints, and the assumptions that matter, from the request, commits, and any description. Inspect enough code and callers to tell existing safeguards from proposed ones. A design can be challenged before code exists; label its assumptions and proposed contracts as such. Do not invent requirements to make an approach fail.

## Break it

Look for a concrete input, state, ordering, failure, or consumer that defeats the stated outcome, across contracts, data ownership, recovery, concurrency, security boundaries, and needless complexity where they apply. Read the surrounding code and tests to check whether each suspect is already handled.

Prove a finding when a safe run can settle it without writing files, such as an existing test or a command that feeds the triggering input to the real code. Record the command, its output, and the output the intent requires. Write a repro script or temporary copy only when the request authorizes it. Do not edit the target, install dependencies, start services, or make live external writes merely to challenge it. A finding that no safe run can settle needs a traced trigger through inspected code and stays labeled unproved. Leave out style, naming, and risks that need a future change to matter.

## Independent perspectives

An explicit multi-model request, independent reviewer count, or nonempty task-supplied panel selects independent read-only reviewers through the shared protocol below. Otherwise use independent reviewers when the consequences and available capabilities justify them. A supplied panel requests delegation, not extra passes by the lead.

Before launching reviewers, read and follow the [shared execution, context, settings, and coverage protocol](../pancake/references/host-runtime.md). Require a completed verdict for each selected entry or report its concrete coverage gap before synthesizing.

## Judge and report

Weigh evidence, not votes. Rerun or recheck each finding before keeping it, merge findings that share a cause, and keep a lone finding whose evidence holds. Resolve disagreement by checking the disputed contract or trigger, or leave it open.

Classify what survives:

- **Act on**: a supported issue that threatens the stated outcome.
- **Consider**: a real tradeoff whose benefit may not justify changing the approach.
- **Unresolved**: the evidence needed for a conclusion is missing.

Lead with the verdict and the strongest findings. For each, give the assumption challenged, the trigger, the consequence, the evidence or command output, and the cheapest next check or correction, linking inspected locations or the proposal passage. Note dropped claims only when the dismissal is informative. Report the scope, actual reviewer independence, and coverage gaps. If nothing actionable survives, say so without calling the approach proven safe.
