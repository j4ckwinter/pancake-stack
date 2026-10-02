# Set up Pancake Stack

Start a new Codex chat after installing the package and select `$pancake-stack:setup`. The backend reports that exact namespaced skill name. Setup asks for default model and reasoning effort preferences and optional role overrides. Keep a field unset to inherit its default, then the host setting. Live conversational invocation in the VS Code composer remains unverified.

Use models and efforts supported by your host. If setup cannot read a model catalog, provide supported values from your host picker. Setup saves your choices without changing the current conversation or global Codex settings. The rigorous `$pancake` workflow is not implemented yet.

## Run the preference helper

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

Run the behavioral tests from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

The tests pass explicit temporary preference paths to every helper invocation. They check read and save behavior, inheritance, malformed input, refusal to overwrite corrupt preferences, and filesystem failures. They do not install a plugin or write to user preference storage.
