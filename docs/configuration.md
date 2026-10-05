# Configuration contract

[The example](../config/preferences.example.json) has `schemaVersion` equal to the integer `1`. `defaults` contains `model` and `reasoningEffort`. `roles` contains `implementation`, `review`, and `research`, each with the same two fields. All fields are required. Extra fields, duplicate JSON keys, and unsupported schema versions are rejected.

A role field of `null` inherits its corresponding default. A default field of `null` inherits the host setting. Each field inherits independently. The all-null example therefore inherits the host for every role. An unavailable host value remains `null` in resolved output.

An explicit `model` or `reasoningEffort` is a nonempty trimmed string. The preference helper validates the structure, not account availability or model and effort compatibility. Setup first runs the bundled catalog helper against the local Codex app server. If discovery fails, it uses accessible host metadata or the user's host picker. Effective pairs need verification after inheritance. A role model override can inherit an effort that its model does not support.

Reasoning effort expresses the user's reasoning preference. It does not enforce a numeric token budget. Saving preferences does not change the parent conversation's model or global Codex configuration. Future workflows must apply supported preferences through available host capabilities.

User storage is `$CODEX_HOME/pancake-stack/config.json`. When `CODEX_HOME` is unset or empty, the path is `~/.codex/pancake-stack/config.json`. Project overrides are deferred. The helper's `--config` flag selects an explicit file path for isolated checks or a user-requested location.

`show` returns the complete configuration. A missing file returns the all-null object without creating directories. `save` accepts the complete JSON object on stdin and atomically replaces the preference file. It refuses to overwrite a malformed or unsupported existing configuration. Repeated saves converge to the same content. Concurrent setup sessions use the last completed save, so finish one setup session before starting another.

`resolve` returns effective preferences by role. Optional `--host-model` and `--host-reasoning-effort` arguments provide observable host values. It reads without writing or applying preferences. Validation and filesystem failures print an error to stderr and exit with code `2`.

See [Set up Pancake Stack](setup.md) for invocation and helper usage.

## Optional Challenge reviewer panel

Schema 1 stays supported with its exact existing fields and output. Schema 2 adds the required `challengeReviewers` list. Each entry contains exactly `model` and `reasoningEffort`, with the same nullable trimmed string rules. A reviewer field inherits independently through the review role, defaults, then supplied host values. An empty list returns one effective review pair. `resolve` still returns only the three existing roles.

[The panel example](../config/challenge-panel.example.json) contains two all-null entries to demonstrate the shape. These resolve to the same settings and do not demonstrate model diversity. Select distinct model IDs supported by your active host to request diversity. Duplicate model choices remain valid independent perspectives, including choices with different reasoning efforts.

`resolve-challenge` returns a list of effective reviewer pairs. It accepts the same optional host arguments as `resolve` and never writes or applies preferences. Missing storage returns one inherited review pair without creating directories. Schema 1 and an empty schema 2 panel use the same fallback.

Selecting a saved panel explicitly opts into schema 2. Older installed helpers reject schema 2. Update the installed plugin before opting in; ordinary setup preserves schema 1 and does not migrate it automatically. Ordinary schema 2 preference edits preserve the panel. Clearing the list retains schema 2 and restores the single review fallback.

Only Challenge consumes the panel. Task-supplied reviewer choices replace it for that task without persistence. With delegation available, Challenge launches one reviewer per selected entry, queues host limits, and awaits verdicts. Unsupported or failed choices remain uncovered and must be reported. Model IDs and reasoning efforts must be supported by the actual delegation host, not merely the catalog server. Distinct completed model IDs establish model diversity; they do not by themselves establish provider diversity.
