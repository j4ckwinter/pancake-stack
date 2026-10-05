# Set up Pancake Stack

Start a new Codex chat after installing the package and select `$pancake-stack:setup`. Setup first asks for a model, then a supported reasoning effort. Role customization is optional. Keep a field unset to inherit its default, then the host setting. The user has confirmed that setup loads in VS Code. Completing setup and checking saved preferences remain unverified.

Setup queries the local Codex app server for model IDs and their supported reasoning efforts before asking you to choose. If discovery fails, setup reports the reason and falls back to accessible host metadata or your host picker. A remote or overridden host can have different choices. Setup saves your choices without changing the current conversation or global Codex settings.

## Run the preference helper

Inspect the local model catalog without writing preferences:

```sh
python3 skills/setup/scripts/catalog.py
```

The helper uses the [Codex app server protocol](https://learn.chatgpt.com/docs/app-server), follows catalog pagination, and stops discovery after 15 seconds. `--codex` selects an explicit executable path. Discovery failures exit with code `2`.

Use Python 3.8 or later. From the repository root, inspect preferences with:

```sh
python3 skills/setup/scripts/preferences.py show
```

Save a complete preference object through stdin. This command writes user preferences:

```sh
python3 skills/setup/scripts/preferences.py save < config/preferences.example.json
```

Resolve preferences against observable host values:

```sh
python3 skills/setup/scripts/preferences.py resolve --host-model MODEL_ID --host-reasoning-effort EFFORT
```

Replace the placeholders with values from your host. Resolve does not apply the result. See the [configuration contract](configuration.md) for inheritance and validation rules.

## Verify without changing user preferences

Run the automated helper and fixture-support tests from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

The preference tests pass explicit temporary paths to every helper invocation. Catalog tests use a temporary fake app server to check pagination, notifications, timeouts, malformed responses, and unavailable executables. The tests do not install a plugin or write to user preference storage.

Use the [behavioral evaluation procedure](behavioral-evaluation.md) to exercise workflows on the fixtures under `tests/behavioral`. Automated fixture checks do not establish how an agent follows a skill or how the host invokes it. Keep those claims tied to workflow trials and the [installation record](installation-verification.md).

## Configure Challenge reviewers

Ask `$pancake-stack:setup` to configure a Challenge reviewer panel. Setup uses the discovered catalog, accepts already supplied choices, and guides one reviewer at a time. Ordinary setup does not ask about or change the panel. Existing panels survive default and role edits.

Saving a panel explicitly opts into schema 2, which older installed helpers cannot read. Clearing the list restores the existing review fallback while retaining schema 2. The [panel example](../config/challenge-panel.example.json) demonstrates two inherited entries, not distinct model choices. Replace those fields through setup with supported choices before expecting model diversity.

Inspect effective reviewer requests without changing preferences:

```sh
python3 skills/setup/scripts/preferences.py resolve-challenge --host-model MODEL_ID --host-reasoning-effort EFFORT
```

Replace the placeholders with observable host values. The result does not prove that delegated model selection works. Challenge reports requested settings, actual selections, and unavailable perspectives when it runs.
