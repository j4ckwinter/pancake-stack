---
name: setup
description: Configure Pancake Stack model and reasoning effort preferences. Use for Pancake Stack setup or $pancake-stack:setup.
---

# Set up Pancake Stack

Configure Pancake Stack only. This skill saves preferences for future Pancake Stack workflows. It does not change the current conversation's model, global Codex settings, or enforce a token budget.

Resolve `scripts/preferences.py` relative to this `SKILL.md` file's installed directory, not the workspace directory. Run the helper with Python 3.8 or later. The helper uses only the Python standard library.

1. Run `python3 <skill-directory>/scripts/preferences.py show` to read existing preferences. Missing preferences return the all-null configuration without writing a file. If reading fails, report the error and preserve the file. Do not reset a malformed or unsupported configuration.
2. Run `python3 <skill-directory>/scripts/catalog.py` before asking for model choices. It starts a local Codex app server, requests `model/list`, and returns model IDs with supported reasoning efforts. Present those choices alongside inheritance. If `codex` is absent from PATH but the host provides its executable location, retry with `--codex <executable-path>`. Do not claim discovery is unavailable without trying the helper. On failure, report the actual reason and use accessible host metadata, or ask for values from the host picker. Do not invent a catalog. A separate local server may use different configuration from a remote or overridden host. In that case, treat the active host's catalog as authoritative.
3. For a request only to configure Challenge reviewers, skip the default and role questions below and follow the panel selection guidance before saving. Preserve existing defaults and roles. Otherwise guide selection one choice at a time. Accept choices already supplied by the user without asking again.
   - Start with the default model. State the current choice in one sentence. Show a numbered list of the discovered model IDs, plus an option to keep the current setting or inherit from Codex. Ask the user to reply with a number or model name. Do not show the full reasoning matrix or role settings yet. Do not invent model rankings or recommendations from catalog order.
   - After the model selection, offer only its supported reasoning efforts, plus inheritance. Ask for one effort. If the model inherits and the active host model is unknown, explain that briefly instead of assuming compatibility. Accept “inherit both” without another effort question.
   - Then offer to finish with the current role settings or customize implementation, review, and research. Keep existing role overrides unless the user changes them. For a new configuration, roles inherit the defaults. Ask about one role at a time only if customization is requested.
   - Keep each choice list in the final reply that asks for the selection. Do not leave choices only in progress messages, tool output, or temporary forms. End the turn and wait for an answer. If using a choice tool, also leave the choices in the final reply.
   - Keep prompts short. Explain inheritance as “use your current Codex setting.” Introduce role inheritance only during customization. Keep catalog provenance, token-budget distinctions, schema details, and host limitations out of routine choice prompts unless they affect the user's decision or the user asks. Saving preferences does not switch the current chat's model. State that once in the saved result.

Keep existing fields and schema version unless the user changes them. Preserve a schema 2 Challenge panel during ordinary default or role edits. Do not upgrade schema 1 during unrelated setup.

For an explicit request to configure Challenge reviewers, use the discovered catalog and guide one reviewer at a time. Accept a supplied list without repeating choices. Offer keeping the saved list, clearing it to the single review fallback, or choosing supported model and effort pairs. Resolve nullable fields independently through review, defaults, then the host and check each effective pair. Do not introduce panel questions into routine setup. Before the first panel save, explain that this explicitly upgrades to schema 2 and older installed helpers cannot read it. Preserve existing default and role fields. An empty list keeps schema 2 and uses the existing single review fallback. Do not spawn reviewers during setup.

Keep existing fields unless the user changes them. A field of `null` inherits independently from the defaults, then the host. Preserve preferences if the user cancels or has not finished choosing. Check effective model and effort pairs after inheritance. Resolve unsupported combinations with the user before saving.

4. Send the complete selected JSON object to `python3 <skill-directory>/scripts/preferences.py save` through stdin. Use a structured process invocation or a safely quoted JSON file redirected to stdin. Never interpolate user model strings into shell code. Save once the user has chosen values. Report a validation or filesystem error without claiming success.
5. Run `show` again to confirm persistence and show the saved preferences. When current host values are observable, run `resolve --host-model <value> --host-reasoning-effort <value>` with safely passed arguments to show effective preferences for each role. For panel changes, also run `resolve-challenge` with the same observable host arguments to confirm the effective reviewer requests. Omit unknown host arguments. A remaining `null` means inheritance could not be resolved. Report persistence separately from application using the guidance below. The current parent conversation remains unchanged.

## Report preferences accurately

After confirming persistence, summarize the choices changed by the user and the saved file location. State once that these preferences configure future Pancake workflows and leave the current chat unchanged. Avoid a full schema dump unless requested.

If effective preferences are requested or inheritance affects the result, distinguish saved values from resolved values. Resolve model and effort independently through role, defaults, then observable host values. For a non-null resolved value, identify its source from those fields. An unresolved null means “inherits from Codex; current value unavailable.” Never infer the current model or effort from catalog order or a tool's list of supported choices.

Resolution selects a requested value; it does not demonstrate application. Describe it as a preference for future work. Catalog availability does not establish that the active host can select that model or effort for a delegated task. Explain a known limitation when it affects an explicit selection; otherwise defer application reporting to the workflow that actually uses it. Do not test application by spawning workers or changing host settings during setup.

Keep the existing implementation, review, and research roles. Do not add role names, presets, or model-family substitutions without a requested workflow that consumes them.

## Preference object

`schemaVersion` is the integer `1` or `2`. Schema 1 remains the default and has no panel field. Schema 2 also requires `challengeReviewers`, a list of objects containing exactly `model` and `reasoningEffort`. An empty list falls back to the review preference. Entries use the same nullable string fields and inherit through review, defaults, then host. `resolve-challenge` returns the effective reviewer list without writing or applying it. Older helpers reject schema 2; use it only after explicitly choosing panel configuration. `defaults` contains `model` and `reasoningEffort`. `roles` contains `implementation`, `review`, and `research`, each with those same fields. Values are `null` or nonempty trimmed strings. All fields are required. Extra fields are rejected.

The helper stores preferences at `$CODEX_HOME/pancake-stack/config.json`, or `~/.codex/pancake-stack/config.json` when `CODEX_HOME` is unset. `--config <path>` before a subcommand overrides that path for an explicitly requested location or isolated verification.

The helper checks the object structure. It cannot check account availability or model and effort compatibility. Obtain that evidence from the host before describing a selection as supported.
