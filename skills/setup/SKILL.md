---
name: setup
description: Configure Pancake Stack model and reasoning effort preferences. Use for Pancake Stack setup.
---

# Set up Pancake Stack

Configure Pancake Stack only. This skill saves preferences for future Pancake Stack workflows. It does not change the current conversation's model, global host settings, or enforce a token budget.

Read [active host guidance](../pancake/references/host-runtime.md) before using preference helpers or delegated settings. On Claude Code, add `--host claude` before every helper subcommand.

Resolve `scripts/preferences.py` relative to this `SKILL.md` file's installed directory, not the workspace directory. Run the helper with Python 3.8 or later. The helper uses only the Python standard library.

1. Run `python3 <skill-directory>/scripts/preferences.py show` to read existing preferences. Missing preferences return the all-null configuration without writing a file. If reading fails, report the error and preserve the file. Do not reset a malformed or unsupported configuration.
2. Discover supported model and effort choices using [active host guidance](../pancake/references/host-runtime.md) before asking for choices. On Codex, try the catalog helper and report actual failures. On Claude Code, try `scripts/catalog.py --host claude`, report actual failures, and fall back to observable active-host metadata or picker information. Never invoke the Codex catalog for Claude. Present available choices alongside inheritance. Do not invent a catalog or supported effort values.
3. For a request only to configure Challenge or consequential implementation reviewers, skip the default and role questions below and follow the panel selection guidance before saving. Preserve existing defaults and roles. Otherwise guide selection one choice at a time. Accept choices already supplied by the user without asking again.
   - Start with the default model. State the current choice in one sentence. Show a numbered list of the discovered model IDs, plus an option to keep the current setting or inherit from the active host. Ask the user to reply with a number or model name. Do not show the full reasoning matrix or role settings yet. Do not invent model rankings or recommendations from catalog order.
   - After the model selection, offer only its supported reasoning efforts, plus inheritance. Ask for one effort. If the model inherits and the active host model is unknown, explain that briefly instead of assuming compatibility. Accept “inherit both” without another effort question.
   - Then offer to finish with the current role settings or customize implementation, review, and research. Keep existing role overrides unless the user changes them. For a new configuration, roles inherit the defaults. Ask about one role at a time only if customization is requested.
   - Keep each choice list in the final reply that asks for the selection. Do not leave choices only in progress messages, tool output, or temporary forms. End the turn and wait for an answer. If using a choice tool, also leave the choices in the final reply.
   - Keep prompts short. Explain inheritance as “use your current host setting.” Introduce role inheritance only during customization. Keep catalog provenance, token-budget distinctions, schema details, and host limitations out of routine choice prompts unless they affect the user's decision or the user asks. Saving preferences does not switch the current chat's model. State that once in the saved result.

Keep existing fields and schema version unless the user changes them. Preserve all panels in schema 2 or 3 during ordinary default or role edits. Do not upgrade a schema during unrelated setup.

For an explicit request to configure Challenge reviewers, use the discovered catalog and guide one reviewer at a time. Accept a supplied list without repeating choices. Offer keeping the saved list, clearing it to the single review fallback, or choosing supported model and effort pairs. Resolve nullable fields independently through review, defaults, then the host and check each effective pair. Do not introduce panel questions into routine setup. When configuring Challenge on schema 1, explain before saving that this explicitly upgrades to schema 2 and older installed helpers cannot read it. Preserve schema 3 when already present. Preserve existing default and role fields. An empty list retains schema 2 or 3 after any required upgrade and uses the existing single review fallback. Do not spawn reviewers during setup.

For an explicit request to configure consequential implementation reviewers, use the same catalog and reviewer selection flow for `implementationReviewers`. Before upgrading schema 1 or 2, explain that schema 3 is required and older installed helpers cannot read it. Preserve defaults, roles, and existing Challenge choices; add an empty `challengeReviewers` list when upgrading schema 1. Keep schema 3 when clearing the implementation panel. An empty list restores the existing single independent review fallback for consequential implementation. Ordinary setup must not introduce implementation panel questions. Do not spawn reviewers during setup.

Keep existing fields unless the user changes them. A field of `null` inherits independently from the defaults, then the host. Preserve preferences if the user cancels or has not finished choosing. Check effective model and effort pairs after inheritance. Resolve unsupported combinations with the user before saving.

4. Send the complete selected JSON object to `python3 <skill-directory>/scripts/preferences.py save` through stdin. Use a structured process invocation or a safely quoted JSON file redirected to stdin. Never interpolate user model strings into shell code. Save once the user has chosen values. Report a validation or filesystem error without claiming success.
5. Run `show` again to confirm persistence and show the saved preferences. When current host values are observable, run `resolve --host-model <value> --host-reasoning-effort <value>` with safely passed arguments to show effective preferences for each role. For panel changes, also run `resolve-challenge` or `resolve-implementation-review` for the changed panel with the same observable host arguments to confirm the effective reviewer requests. Omit unknown host arguments. A remaining `null` means inheritance could not be resolved. Report persistence separately from application using the guidance below. The current parent conversation remains unchanged.

## Report preferences accurately

After confirming persistence, summarize the choices changed by the user and the saved file location. State once that these preferences configure future Pancake workflows and leave the current chat unchanged. Avoid a full schema dump unless requested.

If effective preferences are requested or inheritance affects the result, distinguish saved values from resolved values. Resolve model and effort independently through role, defaults, then observable host values. For a non-null resolved value, identify its source from those fields. An unresolved null means “inherits from the active host; current value unavailable.” Never infer the current model or effort from catalog order or a tool's list of supported choices.

Resolution selects a requested value; it does not demonstrate application. Describe it as a preference for future work. Catalog availability does not establish that the active host can select that model or effort for a delegated task. Explain a known limitation when it affects an explicit selection; otherwise defer application reporting to the workflow that actually uses it. Do not test application by spawning workers or changing host settings during setup.

Keep the existing implementation, review, and research roles. Do not add role names, presets, or model-family substitutions without a requested workflow that consumes them.

## Preference object

`schemaVersion` is the integer `1`, `2`, or `3`. Schema 1 remains the default and has no panel field. Schema 2 also requires `challengeReviewers`, a list of objects containing exactly `model` and `reasoningEffort`. An empty list falls back to the review preference. Entries use the same nullable string fields and inherit through review, defaults, then host. `resolve-challenge` returns the effective reviewer list without writing or applying it. Schema 3 requires both `challengeReviewers` and `implementationReviewers`, with the same list and inheritance rules. `resolve-implementation-review` returns the effective implementation reviewer list. Older helpers reject unsupported versions; upgrade only after explicitly choosing the corresponding panel configuration. `defaults` contains `model` and `reasoningEffort`. `roles` contains `implementation`, `review`, and `research`, each with those same fields. Values are `null` or nonempty trimmed strings. All fields are required. Extra fields are rejected.

By default the helper stores Codex preferences at `$CODEX_HOME/pancake-stack/config.json`, or `~/.codex/pancake-stack/config.json`. With `--host claude`, it uses `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, or `~/.claude/pancake-stack/config.json`. Host selection is not a field in the saved object. `--config <path>` before a subcommand overrides that path for an explicitly requested location or isolated verification.

The helper checks the object structure. It cannot check account availability or model and effort compatibility. Obtain that evidence from the host before describing a selection as supported.
