# Pancake Stack

A Codex plugin for a shared stack of skills, starting with VS Code.

Setup selects model and reasoning effort preferences. How explains existing code with implementation references. Wtf rewrites the previous answer in plain language. Check reviews changes. Fix diagnoses defects. Pancake applies proportionate rigor to the requested task. Balls prepares a brief standup update for a mixed audience. Design proposes software changes grounded in the existing code. Why investigates historical rationale and separates recorded reasons from inference. Verify checks requested behavior and reports evidence and coverage gaps. Handoff prepares a continuation note for a new chat or colleague. Pr drafts a review-ready title and description from the actual change.

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

[Core values](skills/pancake/references/values.md) guide these workflows. They are shared instructions, not global host settings.

`/add-plugin pancake-stack`, `/setup pancake-stack`, and `/pancake` remain the intended shortcuts. Their exact host behavior is unverified.

[Setup](docs/setup.md) documents helper usage. [Configuration](docs/configuration.md) defines inheritance and storage. [Verification](docs/installation-verification.md) records tested behavior. [Plan](docs/plan.md) tracks remaining work.

The package uses the [official plugin format](https://developers.openai.com/plugins/build/plugins). Public distribution and a license remain to be selected.
