# Pancake Stack

Pancake Stack is the foundation for a shared stack of Codex skills, starting with the Codex extension in VS Code.

This repository contains plugin metadata, a local marketplace entry, an empty skills directory, and a proposed configuration contract. It contains no skills or runnable workflows.

The intended experience is:

- `/add-plugin pancake-stack` installs the published plugin.
- `/setup pancake-stack` selects models and reasoning effort.
- `/pancake` invokes the future rigorous workflow.

These commands are proposed. They are not implemented or verified host aliases. Installation by name also needs a published distribution source.

The root `plugin.json` uses the current portable plugin format in the [OpenAI plugin build documentation](https://developers.openai.com/plugins/build/plugins). The repository marketplace points to this directory.

Codex documents `codex plugin marketplace add .` for local marketplace registration. Local CLI help also exposes `codex plugin add pancake-stack@pancake-stack-local` for installation after registration. These commands change local Codex state. This project has not run that command or tested installation end to end in VS Code.

[Configuration](docs/configuration.md) defines the proposed preferences. [Foundation plan](docs/plan.md) records the scope and verification. Skills, setup behavior, and publication remain future work. A license has not been selected.
