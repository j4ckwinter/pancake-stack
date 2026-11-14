# Claude Code support

Pancake Stack packages the same 19 workflows for Codex and Claude Code. Both hosts use the shared `skills/` tree. The native Claude manifests are in `.claude-plugin/`.

## Use Pancake in Claude Code

From the repository root, install the plugin from the local marketplace:

```sh
claude plugin marketplace add ./
claude plugin install pancake-stack@pancake-stack
```

The plugin then loads in every new Claude Code session. These installation commands passed for version 0.21.20 in a temporary Claude profile on Claude Code 2.1.319 on 9 November 2026. The source must be written as `./`; a bare `.` is rejected as an invalid marketplace source. Authenticated workflow behavior remains unverified because no Claude login was available. See [installation verification](installation-verification.md).

Open a new session and request a read-only explanation:

> /pancake-stack:how Explain how this project starts and where its main behavior lives. Keep this read-only and cite the implementation.

Use `/pancake-stack:pancake` for implementation and `/pancake-stack:setup` for help phrasing task-scoped reviewer choices. Other names match the [skill list](../README.md). Replace the Codex `$` prefix in [prompt recipes](recipes.md) with `/`.

Claude Code namespaces plugin skills under the plugin name, so installed skills appear as `/pancake-stack:<skill>`.

## Edit a local install

A local marketplace install reads the plugin from this checkout instead of copying it. Edits take effect at the next session start or after `/reload-plugins`. No reinstall or version bump is needed.

To load a checkout for one session without installing it, run `claude --plugin-dir .` instead.

## Delegate through the active host

Delegates inherit the active host's model and effort unless the task supplies explicit choices or you name an economy model for gathering delegates. Claude Code's Agent interface differs from Codex collaboration. Apply only controls exposed by the actual host. A supplied model ID is a request, not proof that the host accepts or applies it. Name the economy model by an alias the Agent tool accepts, such as `sonnet`; see [task settings](configuration.md#use-an-economy-model-for-gathering-work).

Reviewers still need separately identified completed verdicts. Missing or unsupported choices remain coverage gaps. Competing Design retains independent candidates and a separate judge. Direct work uses current conversation settings.

There are no bundled Python helpers or saved preference reads. Older Claude preference files remain untouched and no longer control this version. See [task settings](configuration.md) for the migration boundary.
