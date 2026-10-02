# Pancake Stack

A Codex plugin for a shared stack of skills, starting with VS Code.

Setup selects model and reasoning effort preferences. The rigorous pancake workflow is planned.

## Install locally

From this repository, run:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack-local
```

These commands register the marketplace and install the plugin in your local Codex configuration.

Start a new Codex chat and select `$pancake-stack:setup`. Setup lists local model choices and saves the preferences you select. Saving does not switch the current chat's model.

`/add-plugin pancake-stack`, `/setup pancake-stack`, and `/pancake` remain the intended shortcuts. Their exact host behavior is unverified.

[Setup](docs/setup.md) documents helper usage. [Configuration](docs/configuration.md) defines inheritance and storage. [Verification](docs/installation-verification.md) records tested behavior. [Plan](docs/plan.md) tracks remaining work.

The package uses the [official plugin format](https://developers.openai.com/plugins/build/plugins). Public distribution and a license remain to be selected.
