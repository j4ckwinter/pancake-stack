# Pancake Stack

Pancake Stack is the foundation for a shared stack of Codex skills, starting with the Codex extension in VS Code.

This repository contains plugin metadata, a local marketplace entry, a setup skill with a preference helper, and a configuration contract. The rigorous workflow remains planned.

The Codex experience is:

- Install the package through Codex's plugin tooling.
- `$pancake-stack:setup` selects models and reasoning effort.
- `$pancake` invokes the future rigorous workflow.

The setup skill is implemented and discovered by the Codex backend as `pancake-stack:setup`. The pancake skill remains planned. Live setup invocation in the VS Code composer remains unverified. The original `/add-plugin pancake-stack`, `/setup pancake-stack`, and `/pancake` forms remain unverified. Codex documents `$` mentions for invoking skills in its IDE extension. The installed extension also adds enabled skills to its slash picker, so `/pancake` remains the intended shortcut pending a live check.

The root `plugin.json` uses the current portable plugin format in the [OpenAI plugin build documentation](https://developers.openai.com/plugins/build/plugins). The repository marketplace points to this directory.

Local installation passed using the Codex binary bundled with the VS Code extension. From this repository, run:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack-local
codex plugin list --marketplace pancake-stack-local --json
```

These commands register the marketplace and install the plugin in your local Codex configuration. Verification passed for versions `0.0.1` and `0.1.0`. The backend discovered the enabled setup skill in version `0.1.0`. Conversational invocation remains unverified. See the [installation verification](docs/installation-verification.md) for evidence and limits.

[Setup](docs/setup.md) documents the setup skill and isolated tests. [Configuration](docs/configuration.md) defines the preferences. [Foundation plan](docs/plan.md) records the scope and verification. Rigorous skills and publication remain future work. A license has not been selected.
