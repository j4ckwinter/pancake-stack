---
name: setup
description: Configure Pancake Stack model preferences for delegates and reviewer panels. Use for Pancake Stack setup.
---

# Set up Pancake Stack

Save model preferences for future delegates and reviewer panels. Direct work uses current host settings. Delegates inherit host effort unless a task explicitly requests an effort. Setup does not change the current conversation or global host settings.

Read [active host guidance](../pancake/references/host-runtime.md) before using helpers. On Claude Code, add `--host claude` before every preference subcommand. Resolve `scripts/preferences.py` relative to this installed skill, not the workspace. Use Python 3.8 or later.

1. Run `python3 <skill-directory>/scripts/preferences.py show`. Missing preferences return the all-null object without writing. Report read failures and preserve the file. If any saved effort is non-null, explain that it remains stored but is inactive. Do not clear it during model setup.
2. Discover models through the active host's catalog helper before asking for choices. On Claude Code, use `scripts/catalog.py --host claude`. Report discovery failures and use observable active-host metadata or the user's picker. Never use the other host's catalog. Catalog effort metadata does not create a saved effort choice.
3. Accept choices already supplied by the user. For panel-only requests, skip default and role questions and follow the panel guidance below. Otherwise offer the default model first, then optional customization of implementation, review, and research models. Ask about one choice at a time. Show discovered model IDs alongside keeping the current model or inheriting. Do not rank models from catalog order. Keep the choices in the final reply asking for selection and wait for an answer. Explain inheritance as "use your current host setting." Do not ask for effort.
4. Change only the selected model fields. Preserve loaded schema version, unedited roles, panels, and legacy effort values. For new objects or panel entries, set `reasoningEffort` to `null`. Preserve preferences if the user cancels or has not finished choosing. Send the complete object through stdin to `python3 <skill-directory>/scripts/preferences.py save`. Use structured process arguments or a safely quoted JSON file. Never interpolate user strings into shell code. Report errors without claiming success.
5. Run `show` again to confirm persistence. If effective choices are requested, run `resolve` and the resolver for each changed panel. Supply `--host-model` only when observable. Optional `--host-reasoning-effort` reports an observable host value; it is informational and does not select delegate effort. Omit unknown host values. Summarize changed models and storage location. State once that saving leaves the current chat unchanged.

## Configure reviewer panels

For an explicit panel request, guide one reviewer model at a time or accept a supplied list. Offer keeping the saved list, clearing it to the single review fallback, or choosing supported models. Nullable models inherit through review, defaults, then the host. Preserve list order and duplicates. Duplicate models still request separate independent reviewers. Do not introduce panel questions into ordinary setup or spawn reviewers during setup.

Challenge uses `challengeReviewers`. Configuring it on schema 1 explicitly upgrades to schema 2. Explain before saving that older helpers cannot read that version. Preserve schema 3 when already present. Preserve defaults, roles, and the implementation panel. Clearing the list retains the loaded schema and restores the single review fallback.

Consequential implementation review uses `implementationReviewers` and requires schema 3. Explain the upgrade before saving on schema 1 or 2. Preserve defaults, roles, and Challenge choices. Add an empty `challengeReviewers` list when upgrading schema 1. Clearing the implementation list retains schema 3 and restores the single independent reviewer fallback.

When changing an existing reviewer model, retain that entry's legacy effort value. New entries use null effort. Explicitly removing an entry removes its stored values. Do not silently rebuild unaffected entries or delete legacy effort during unrelated edits.

## Report preferences accurately

Distinguish stored models, resolved requests, and observed application. Model inheritance follows role, defaults, then observable host model. Unknown inheritance stays null. Never infer the host model or effort from catalog order.

Saved `reasoningEffort` values remain visible in `show` for compatibility but no longer influence resolution. Resolve commands disclose non-null legacy effort on stderr. Resolved effort comes only from a supplied observable host value or remains null. It must not become a delegate override. Explicit task effort remains supported through the active interface and is not saved by Setup.

Catalog availability does not prove account access or delegated selection. Report known limitations when they affect a model choice. Defer application evidence to the workflow that actually delegates. Do not spawn workers or change host settings to test Setup.

## Preference object

Schemas 1, 2, and 3 keep their existing exact fields. `defaults` and each of `implementation`, `review`, and `research` under `roles` contain `model` and `reasoningEffort`. Values are null or nonempty trimmed strings. All fields are required, and extra fields are rejected. Effort fields are inactive compatibility data. See the [configuration contract](../../docs/configuration.md).

Schema 2 also requires `challengeReviewers`. Schema 3 requires both reviewer lists. Each entry contains exactly `model` and `reasoningEffort`. An empty or absent panel resolves to one review model. `resolve` returns the three roles. `resolve-challenge` and `resolve-implementation-review` return their respective reviewer lists. Reading never upgrades or rewrites storage.

Codex storage is `$CODEX_HOME/pancake-stack/config.json`, defaulting to `~/.codex/pancake-stack/config.json`. Claude storage is `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, defaulting to `~/.claude/pancake-stack/config.json`. `--config <path>` before the subcommand overrides either location for an explicitly requested path or isolated verification. Never read the other host as a fallback.
