# Claude Code support

Pancake Stack 0.20.0 packages the same 19 workflows for Codex and Claude Code. Both hosts use the shared `skills/` tree. The native Claude manifests are in `.claude-plugin/`.

## Use Pancake in Claude Code

From the repository root, load the plugin for one session:

```sh
claude --plugin-dir .
```

Then request a read-only explanation:

> /pancake-stack:how Explain how this project starts and where its main behavior lives. Keep this read-only and cite the implementation.

Use `/pancake-stack:pancake` for implementation and `/pancake-stack:setup` for help phrasing task-scoped reviewer choices. Other names match the [skill list](../README.md). Replace the Codex `$` prefix in [prompt recipes](recipes.md) with `/`.

The local marketplace flow is:

```sh
claude plugin marketplace add .
claude plugin install pancake-stack@pancake-stack
```

These installation commands passed for the recorded earlier package in a temporary Claude profile. Version 0.20.0 installation and authenticated workflow behavior remain unverified. See [installation verification](installation-verification.md).

## Delegate through the active host

Workers inherit the active host's model and effort unless the task supplies explicit choices. Claude Code's Agent interface differs from Codex collaboration. Apply only controls exposed by the actual host. A supplied model ID is a request, not proof that the host accepts or applies it.

Reviewers still need separately identified completed verdicts. Missing or unsupported choices remain coverage gaps. Competing Design retains independent candidates and a separate judge. Direct work uses current conversation settings.

There are no bundled Python helpers or saved preference reads. Older Claude preference files remain untouched and no longer control this version. See [task settings](configuration.md) for the migration boundary.
