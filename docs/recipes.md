# Give Pancake a concrete task

Use these prompts in a Codex chat after installing the plugin. Replace the example behavior and paths with your project's details. Select the installed skill in the host picker when available. The `$pancake-stack:...` text invokes a skill in chat, not a shell command.

In Claude Code, use `/pancake-stack:...` with the same task text. Setup helps phrase task choices without saving preferences. Use choices supported by the active host when requesting particular reviewer or candidate models. See [Claude Code support](claude.md) for observed host coverage.

## Start with a read-only walkthrough

> $pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only. Cite inspected code and name anything you could not verify.

No setup is required to inherit your current Codex settings. After installing or refreshing the plugin, open a new chat. A stale chat can still expose older installed instructions. Installed Codex 0.21.3 trials exercised the task-scoped default reviewer and a requested two-reviewer Challenge. See the [installation record](installation-verification.md) for those results and the [refresh recipe](codex-installation.md) for updating the cached copy. Visible picker behavior remains a separate check.

## Trace a behavior

> $pancake-stack:how Explain how the import command handles cancellation and releases resources. Keep this read-only. Cite the implementation and distinguish observed behavior from assumptions.

Expect an execution trace with inspected code locations and explicit evidence gaps. If you need the reason behind a choice, use `$pancake-stack:why` and name the decision. Ask it to separate recorded rationale from inference.

## Turn a ticket into an implementation brief

Give Scope the ticket text and the relevant project context.

> $pancake-stack:scope Our ticket says cancelling an import must stop further writes and tell the caller it was cancelled. Inspect the current import flow and its tests. Produce a brief with current behavior, observable acceptance criteria, compatibility constraints, and unresolved product choices. Keep this read-only and return the brief in chat.

Review the proposed criteria and resolve any product choices before requesting implementation. A scope brief does not start the work. If a consequential design choice remains, use the [design recipe](#compare-and-challenge-a-design) first.

> $pancake-stack:pancake Implement the cancellation behavior described in the accepted brief above. Preserve the existing successful-import behavior. Verify the acceptance criteria through the supported interface with isolated local data. Report the changes, checks, and remaining gaps. Do not commit, push, or deploy.

Use the [authorized-run recipe](#finish-an-authorized-run) when you want to grant delivery permissions as well.

## Compare and challenge a design

> $pancake-stack:design Propose how to add cancellation to our import job. Inspect the current job lifecycle and callers. Compare extending that design with a separate cancellation owner. Show caller usage, failure recovery, and a verification plan. Do not edit files.

You can also request independent exploration explicitly.

> $pancake-stack:design Explore two competing designs for migrating live invoice payloads from total to amount. Use independent candidate agents and a separate independent judge. Preserve readability of stored total records without rewriting the archive. Compare compatibility, ownership, failure recovery, migration cost, and verification against the existing approach. Keep the project unchanged.

This is task-specific and does not save preferences. Small changes and choices settled by an existing pattern or hard constraint remain direct Design work. Unresolved consequential choices with materially different viable approaches use independent exploration by default. Explicit delegation limits still apply. If you want model diversity, supply supported candidate models and a judge model. Omitted models inherit the active host settings for both candidates and the judge. Effort inherits from the host unless requested separately for this task. The judge receives anonymized proposals after the candidates complete. Missing candidates or an unavailable judge remain explicit gaps.

Then challenge the concrete proposal.

> $pancake-stack:challenge Challenge the cancellation proposal above against the current implementation. Find a concrete ordering or failure that breaks its assumptions. Report supported findings and missing evidence. Do not apply fixes.

To request model diversity, supply supported reviewer models in the challenge prompt for this task. Challenge launches one independent reviewer per selected entry when the host supports delegation. It reports actual selections and uncovered perspectives. Different models from the same provider do not establish provider diversity.

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

## Pause and resume in a fresh chat

Ask Handoff to stop the current task and preserve a concrete resume point.

> $pancake-stack:handoff Pause the import-cancellation work. Stop task-owned workers from making further edits. Inspect the current branch and local changes. Return a handoff with the objective, accepted decisions, completed and unfinished work, checks actually run, active resources, authorization limits, and the next action. Preserve my edits. Do not commit, stash, or clean up unrelated work.

Copy the returned note into the new chat in the same repository. The note remains in the conversation unless you explicitly request a file. Use Recap to check the note against the current workspace before continuing.

> $pancake-stack:recap Use the handoff below to recover the import-cancellation task. Inspect the current branch and relevant changes. Identify anything that differs from the note, distinguish previous check results from current evidence, and state the next useful action. Keep this read-only. Do not search other conversations.

Paste the handoff after that prompt. Once the recovered state is clear, request continuation separately.

> $pancake-stack:pancake Continue the unfinished import-cancellation work from the reconciled handoff above. Preserve the accepted requirements and my unrelated edits. Complete the remaining checks. Do not commit, push, or deploy.

## Prepare a pull request description

Use PR after a change is ready to describe. Replace `main` with the actual review base.

> $pancake-stack:pr Draft a title and description for the current branch against main. Use the accepted import-cancellation brief and inspect the actual diff. Explain the caller-visible behavior, the verification already performed, and material limits. Identify local changes that are not yet committed separately from the copyable description. Do not create or update a remote PR.

Expect a draft in chat. This request does not run new tests or publish the branch. If verification is still needed, use the [verification recipe](#prove-a-specific-outcome) first. To publish afterward, name the repository, source branch, and base, and explicitly authorize any required push and PR creation.

## Use Pancake's specialized workflows

These workflows are references within Pancake, not separate skills. Invoke Pancake and describe the outcome and allowed actions.

> $pancake-stack:pancake Investigate why the worker's memory grows using the captured profiles in traces/. Separate observed evidence from hypotheses and identify the next useful measurement. Keep this read-only; do not repair the code.

> $pancake-stack:pancake Compare the current parser with the proposed cache on the supplied workload. Run a bounded local experiment with repeated measurements and correctness checks. Report the result and uncertainty. Keep prototypes and results in the agreed temporary directory; do not change production code.

> $pancake-stack:pancake Check the status and review feedback for PR 42. Report blockers and assess each comment against the current diff. Keep this read-only; do not post replies, change code, merge, or start a watcher.

> $pancake-stack:pancake Match the settings page to the supplied reference while preserving behavior. Use the required states and viewports from the supplied brief, capture the current rendering, implement the corrections, and compare the result. Report any state or tool you could not verify. Do not commit or publish.

Runtime diagnosis separates evidence from proposed repairs. Experiments need comparable measurements and correctness checks. PR triage needs current forge evidence. Visual parity needs rendered comparisons; source inspection alone does not establish a match.

## Finish an authorized run

> $pancake-stack:pancake Implement cancellation for the import job using the agreed design above. Continue until the caller observes cancellation, further writes stop, and the relevant checks pass. Use isolated local data. Keep a short plan with checked milestones and record consequential decisions. You may commit the completed change. Do not push or deploy. If a required decision or unavailable capability blocks completion, preserve the state and explain the next action.

Supply a reviewer panel in the implementation request when you need more than the default single independent reviewer for consequential work.

> For this implementation, use two independent reviewers. Both should inherit the active host settings. Report each completed verdict and any missing coverage.

You can request supported reviewer models and effort explicitly for the task. Setup can help phrase those choices but does not save them. Local, low-impact work still permits direct review. Expect completed reviewer results and requested-versus-observed selection evidence when you supply overrides.

Name the outcome and allowed actions rather than relying on "loop until done" alone. Expect checked milestones and a final account of the result. A long run does not grant unrelated external actions or schedule unattended work.

## Avoid host and evidence traps

- Use the documented skill names or the host picker. Shorter slash aliases remain unverified in the [installation record](installation-verification.md).
- Check the installed version before a host trial. Reading a repository skill file does not prove that the host discovers or invokes the installed plugin.
- Treat explicit model choices as requests. Available host metadata does not prove that an override was applied. See [configuration](configuration.md).
- Keep installation checks separate from repository validation. See the [installation record](installation-verification.md) for the tested host, dated results, and pending checks. Local and Git-backed CLI installation under the current marketplace name have been verified. Visible VS Code checks remain separate.
- Ask for evidence through the interface your claim concerns. Distinguish static findings from runtime observations and mark cases that could not run.


## Continue a sustained task

> $pancake-stack:pancake Continue the agreed migration through its checked milestones. Keep owners, dependencies, current revisions, verification evidence, and the next action in the existing plan. Use handoff if continuation is blocked. You may commit verified units. Do not push, merge, deploy, or schedule background work.

Existing substantial-work and handoff guidance covers a single sustained run. Request a durable shared coordination artifact when multiple sessions or owners need to recover state. Name a specific PR and allowed actions before requesting monitoring. This plugin does not currently provide a PR watcher or promise work after the active session ends. Add monitoring helpers when an actual PR lifecycle requires them.
