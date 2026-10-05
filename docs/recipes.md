# Give Pancake a concrete task

Use these prompts in a Codex chat after installing the plugin. Replace the example behavior and paths with your project's details. Select the installed skill in the host picker when available. The `$pancake-stack:...` text invokes a skill in chat, not a shell command.

## Trace a behavior

> $pancake-stack:how Explain how the setup preference helper resolves a role's model and reasoning effort. Keep this read-only. Cite the implementation. Distinguish saved preferences from choices actually applied by the host.

Expect an execution trace with inspected code locations and explicit evidence gaps. If you need the reason behind a choice, use `$pancake-stack:why` and name the decision. Ask it to separate recorded rationale from inference.

## Compare and challenge a design

> $pancake-stack:design Propose how to add cancellation to our import job. Inspect the current job lifecycle and callers. Compare extending that design with a separate cancellation owner. Show caller usage, failure recovery, and a verification plan. Do not edit files.

Then challenge the concrete proposal.

> $pancake-stack:challenge Challenge the cancellation proposal above against the current implementation. Find a concrete ordering or failure that breaks its assumptions. Report supported findings and missing evidence. Do not apply fixes.

To request model diversity, first use setup to select a Challenge reviewer panel, or supply supported reviewer model and effort pairs in the challenge prompt for this task only. Challenge launches one independent reviewer per selected entry when the host supports delegation. It reports actual selections and uncovered perspectives. Different models from the same provider do not establish provider diversity.

Expect a recommendation first, then a verdict grounded in the proposal and inspected code. A design request or challenge does not authorize implementation.

## Repair a reported failure

> $pancake-stack:fix The import command exits successfully when its input file is missing. It should exit nonzero and identify the missing file. Reproduce through the command, find the cause, make a focused fix, and repeat the failing scenario. Use temporary local files.

Supply the actual command, error output, and expected behavior when you have them. Expect the cause, correction, and verification evidence. If the original scenario cannot run, the answer must identify that limit.

## Implement through a failing test

> $pancake-stack:tdd Fix the summary command so an empty JSON list returns count and average zero. Add a focused regression test, run it against the broken implementation, then make the correction. Preserve the nonempty result and report the failing-before and passing-after evidence.

Use `tdd` when you want a test-first cycle. Use `fix` when the cause still needs investigation. Expect a failure caused by the requested behavior before production edits, followed by the same check passing. An unavailable service or impractical harness must remain an explicit limit; the skill should not invent infrastructure or claim an unobserved failure.

## Prove a specific outcome

> $pancake-stack:verify Verify that cancelling an import stops further writes and reports cancellation to the caller. Exercise the supported interface using isolated local data. Check the normal completion path too. Report what passed, failed, or remains unverified. Do not change product code or user settings.

Expect observations tied to the requested behavior. A passing build alone does not demonstrate cancellation. If you need repeatable project instructions, explicitly request a reusable verification recipe and its destination.

## Review a change

> $pancake-stack:check Review the staged and unstaged changes for bugs and regressions. Follow affected callers and stored-data contracts. Give each actionable finding a file location, trigger, and consequence. Keep this read-only and report verification gaps.

For committed work, supply the commit or branch range instead. Expect actionable findings or a no-findings verdict with coverage limits. A clean workspace does not identify which committed change you intended to review.

## Finish an authorized run

> $pancake-stack:pancake Implement cancellation for the import job using the agreed design above. Continue until the caller observes cancellation, further writes stop, and the relevant checks pass. Use isolated local data. Keep a short plan with checked milestones and record consequential decisions. You may commit the completed change. Do not push or deploy. If a required decision or unavailable capability blocks completion, preserve the state and explain the next action.

Name the outcome and allowed actions rather than relying on "loop until done" alone. Expect checked milestones and a final account of the result. A long run does not grant unrelated external actions or schedule unattended work.

## Avoid host and evidence traps

- Use the documented skill names or the host picker. Shorter slash aliases remain unverified in the [installation record](installation-verification.md).
- Check the installed version before a host trial. Reading a repository skill file does not prove that the host discovers or invokes the installed plugin.
- Treat resolved model preferences as requests. The helper does not select the host model, and catalog availability does not prove that an override was applied. See [configuration](configuration.md).
- Keep installation checks separate from repository validation. See the [installation record](installation-verification.md) for the tested host, dated results, and pending checks, including installation under the renamed marketplace.
- Ask for evidence through the interface your claim concerns. Distinguish static findings from runtime observations and mark cases that could not run.
