# Pancake Stack

Pancake Stack is the foundation for a shared stack of Codex skills, starting with the Codex extension in VS Code.

This repository contains plugin metadata, a local marketplace entry, an empty skills directory, and a proposed configuration contract. It contains no skills or runnable workflows.

The planned Codex experience is:

- Install the package through Codex's plugin tooling.
- `$setup pancake-stack` selects models and reasoning effort.
- `$pancake` invokes the future rigorous workflow.

The setup and pancake skills are not implemented. The original `/add-plugin pancake-stack`, `/setup pancake-stack`, and `/pancake` forms remain unverified. Codex documents `$` mentions for invoking skills in its IDE extension. The installed extension also adds enabled skills to its slash picker, so `/pancake` remains the intended shortcut pending a live check.

The root `plugin.json` uses the current portable plugin format in the [OpenAI plugin build documentation](https://developers.openai.com/plugins/build/plugins). The repository marketplace points to this directory.

Local installation passed using the Codex binary bundled with the VS Code extension. From this repository, run:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack-local
codex plugin list --marketplace pancake-stack-local --json
```

These commands register the marketplace and install the plugin in your local Codex configuration. Verification reported the plugin as installed and enabled. Workflow invocation in the VS Code composer remains untested because this package contains no skills. See the [installation verification](docs/installation-verification.md) for evidence and limits.

[Configuration](docs/configuration.md) defines the proposed preferences. [Foundation plan](docs/plan.md) records the scope and verification. Skills, setup behavior, and publication remain future work. A license has not been selected.
