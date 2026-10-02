---
name: setup
description: Configure Pancake Stack model and reasoning effort preferences. Use for Pancake Stack setup or $pancake-stack:setup.
---

# Set up Pancake Stack

Configure Pancake Stack only. This skill saves preferences for future Pancake Stack workflows. It does not change the current conversation's model, global Codex settings, or enforce a token budget.

Resolve `scripts/preferences.py` relative to this `SKILL.md` file's installed directory, not the workspace directory. Run the helper with Python 3.8 or later. The helper uses only the Python standard library.

1. Run `python3 <skill-directory>/scripts/preferences.py show` to read existing preferences. Missing preferences return the all-null configuration without writing a file. If reading fails, report the error and preserve the file. Do not reset a malformed or unsupported configuration.
2. Discover available models and their supported reasoning efforts through host metadata or tools actually accessible in this session. Codex app-server `model/list` metadata includes `model` and `supportedReasoningEfforts` when that host API is accessible. Do not invent a catalog or assume that a model ID is available to this account. If discovery is unavailable, explain that limitation and ask the user for supported values from the host's model picker.
3. Ask for default model and reasoning effort together. Offer inheritance as the default for unset preferences. Explain that reasoning effort is a host setting rather than a numeric token budget. Offer optional overrides for implementation, review, and research. Keep existing fields unless the user changes them. A field of `null` inherits independently from the corresponding default, then the host. Preserve existing preferences if the user cancels or has not finished choosing.
Check each effective model and effort pair after inheritance. A role model override can inherit an effort that its model does not support. Resolve that mismatch with the user before saving.

4. Send the complete selected JSON object to `python3 <skill-directory>/scripts/preferences.py save` through stdin. Use a structured process invocation or a safely quoted JSON file redirected to stdin. Never interpolate user model strings into shell code. Save once the user has chosen values. Report a validation or filesystem error without claiming success.
5. Run `show` again to confirm persistence and show the saved preferences. When current host values are observable, run `resolve --host-model <value> --host-reasoning-effort <value>` with safely passed arguments to show effective preferences for each role. Omit unknown host arguments. A remaining `null` means inheritance could not be resolved. Explain that a future workflow must apply supported role choices through host capabilities. The current parent conversation remains unchanged.

## Preference object

`schemaVersion` is the integer `1`. `defaults` contains `model` and `reasoningEffort`. `roles` contains `implementation`, `review`, and `research`, each with those same fields. Values are `null` or nonempty trimmed strings. All fields are required. Extra fields are rejected.

The helper stores preferences at `$CODEX_HOME/pancake-stack/config.json`, or `~/.codex/pancake-stack/config.json` when `CODEX_HOME` is unset. `--config <path>` before a subcommand overrides that path for an explicitly requested location or isolated verification.

The helper checks the object structure. It cannot check account availability or model and effort compatibility. Obtain that evidence from the host before describing a selection as supported.
