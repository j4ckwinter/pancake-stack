# Pancake Stack

A Codex plugin for a shared stack of skills, starting with VS Code.

Setup selects model and reasoning effort preferences. How explains existing code with implementation references. Wtf rewrites the previous answer in plain language. Check reviews changes, including hidden consumers and compatibility assumptions when relevant. Fix diagnoses defects. Pancake applies proportionate rigor to the requested task, with a defined implementation sequence, change review, verification, and failure handling. Balls prepares a brief standup update for a mixed audience. Design proposes software changes grounded in the existing code. Why investigates historical rationale and separates recorded reasons from inference. Verify checks requested behavior and reports evidence and coverage gaps. Handoff prepares a continuation note for a new chat or colleague. Pr drafts a review-ready title and description from the actual change. Scope turns a ticket into a grounded implementation brief.

## Install locally

From this repository, run:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack-local
```

These commands register the marketplace and install the plugin in your local Codex configuration.

Start a new Codex chat and select `$pancake-stack:setup`. Setup lists local model choices and saves the preferences you select. Saving does not switch the current chat's model.

Use `$pancake-stack:how` to ask about code, for example “how does model discovery work?” It investigates without changing files. This first version uses the current agent and model.

Use `$pancake-stack:wtf` to restate the previous answer more clearly. `/wtf` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:check` for a read-only change review, `$pancake-stack:fix` for a defect, and `$pancake-stack:pancake` for a rigorous task. These new skills have not yet been verified in the live Codex picker. Pancake reads saved role preferences, but applies them only when the host supports selection for that work. It otherwise uses the current agent settings.

Use `$pancake-stack:balls` to prepare a short spoken update covering blockers, aims, and lessons learned. It uses the current ticket, branch, staged changes, and unstaged changes, alongside your notes. `/balls` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:design` to compare approaches and propose interfaces before coding. It returns a proposal without editing files unless implementation is also requested. `/design` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:why` to investigate why existing code or a design decision took its current form. It starts with local history and documentation. `/why` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:verify` to check that a feature or fix works through the relevant interface using existing tools. It reports verification results without repairing code unless requested. `/verify` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:handoff` to summarize the objective, current repository state, decisions, verification, blockers, and next action. It returns the note in chat and saves a file only when requested. `/handoff` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:pr` to draft a PR title and description from the ticket and branch diff. It creates or updates a remote PR only when explicitly requested. `/pr` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:scope` to establish the outcome, acceptance criteria, relevant code, boundaries, and unresolved decisions for a ticket. It returns a brief without implementing the work. `/scope` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:sift` to remove filler and vague phrasing from prose while preserving meaning and voice. Pancake reads it as its writing standard for updates and written output. Unlike wtf, sift can edit supplied text or authorized documents. `/sift` is the intended shortcut, pending a live picker check.

Use `$pancake-stack:challenge` to stress-test a design or consequential change against concrete counterexamples. It returns an evidence-based verdict without applying fixes unless requested. Pancake uses it for contested consequential assumptions. `/challenge` is an intended shortcut, pending a live picker check.

Use `$pancake-stack:reflect` to identify durable lessons from the current task and propose improvements to code, tests, tooling, or guidance. It does not apply changes unless requested. `/reflect` is an intended shortcut, pending a live picker check.

For authorized performance work, prototypes, and skill evaluations, Pancake loads [measured-experiment guidance](skills/pancake/references/experiments.md). It establishes a baseline, compares observations, and reports uncertainty without adding a separate command.

Verify can also create a [project-specific verification recipe](skills/verify/references/recipes.md) when requested. It reuses established tools and reports recipes as drafts until their documented paths have been exercised.

Pancake can use [candidate comparison and parallel-work guidance](skills/pancake/references/parallel-work.md) when alternatives or separable work justify it. It keeps candidate state isolated, checks combined results, and reports missing coverage. No separate cookoff command is added.

For dependent phases, broad migrations, and material uncertainty, Pancake uses [substantial-work guidance](skills/pancake/references/substantial-work.md). It checks each unit and the combined outcome, revises plans from evidence, and preserves unfinished state.

During substantial work, [decision-trail guidance](skills/pancake/references/decision-trail.md) keeps consequential choices and supporting evidence recoverable. A separate saved record is optional and requires a request.

Design guidance starts from caller usage, makes data ownership and valid states explicit, and revisits shared assumptions when workarounds recur. It remains a proposal unless implementation is requested.

For technical documentation, Sift loads [technical-writing guidance](skills/sift/references/technical-writing.md) to match the reader’s purpose and make instructions and factual claims clear.

Check also examines relevant comments, claimed constraints, and lint or type-check suppressions. It reports evidence-backed correctness problems and preserves useful rationale; review remains read-only.

Setup distinguishes saved preferences from resolved inheritance. Pancake reports whether explicit model and effort preferences were applied through host capabilities or fell back to current settings.

For runtime symptoms and profiling captures, Pancake loads [forensics guidance](skills/pancake/references/forensics.md). It traces observations to source, distinguishes hypotheses from confirmed mechanisms, and keeps diagnosis separate from repair.

For appearance-preserving migrations and interface matching, Pancake loads [visual-parity guidance](skills/pancake/references/visual-parity.md). It compares equivalent states, preserves reference evidence, and reports capture limits and untested states.

For requested PR status and maintenance, Pancake loads [PR-maintenance guidance](skills/pancake/references/pr-maintenance.md). It assesses CI and feedback against the tested revision, bounds retries, and keeps remote actions within the requested scope.

For requested delivery or its preparation, Pancake loads [shipping guidance](skills/pancake/references/shipping.md). It checks current artifacts and dependencies, confirms the delivery result, and keeps merge, release, and deployment scope explicit.

Substantial-work guidance also tracks unit ownership, dependencies, evidence, and continuation limits. A requested plan remains a plan; sustained work uses actual host capabilities and stops on an explicit pause.

Handoff includes [continuation guidance](skills/handoff/references/continuation.md) for requested pickup and explicit pauses. It reconciles notes with current state and preserves incomplete work without automatic commits or cleanup.

For requested worktree cleanup, Pancake loads [cleanup guidance](skills/pancake/references/worktree-cleanup.md). It checks ownership, active use, and retained work before removal, including untracked and ignored data.

[Core values](skills/pancake/references/values.md) guide these workflows. They are shared instructions, not global host settings.

`/add-plugin pancake-stack`, `/setup pancake-stack`, and `/pancake` remain the intended shortcuts. Their exact host behavior is unverified.

[Setup](docs/setup.md) documents helper usage. [Configuration](docs/configuration.md) defines inheritance and storage. [Verification](docs/installation-verification.md) records tested behavior. [Plan](docs/plan.md) tracks remaining work.

The package uses the [official plugin format](https://developers.openai.com/plugins/build/plugins). Public distribution and a license remain to be selected.

Use `$pancake-stack:recap` to recover decisions, unfinished work, and current state for a project or topic. It starts with supplied context, reconciles repository evidence, and searches prior sessions only when requested and safely scoped. `/recap` remains an intended shortcut pending host verification.

Use `$pancake-stack:teach` for a guided explanation of code or a software concept. It adapts to your question, uses concrete examples, and preserves uncertainty about design reasons. `/teach` remains an intended shortcut pending host verification.

Verify can audit or update an existing project recipe when requested, using [maintenance guidance](skills/verify/references/maintenance.md). It checks actual paths and separates stale instructions, product regressions, and unavailable prerequisites. An audit stays read-only; updates remain scoped to the recipe and its owned harness.

Design and Pancake implementation can load [TypeScript guidance](skills/design/references/typescript.md) for meaningful variants, authoritative types, and runtime boundary validation. It follows existing project tooling and conventions.
