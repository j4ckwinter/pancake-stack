# Proposed configuration contract

This contract describes future setup behavior. The plugin does not read, validate, or write preferences yet.

[The example](../config/preferences.example.json) has `schemaVersion` equal to `1`. `defaults` contains `model` and `reasoningEffort`. `roles` contains `implementation`, `review`, and `research`, each with the same two fields.

A role field of `null` inherits its corresponding default. A default field of `null` inherits the host setting. The all-null example therefore inherits the host for every role.

An explicit `model` is a nonempty model ID supported by the host. An explicit `reasoningEffort` is a nonempty effort string supported by that host and model. Model availability and supported effort values come from the host. This contract does not maintain a fixed model list.

Reasoning effort expresses the user's reasoning preference. It does not enforce a numeric token budget. The plugin must not silently change the parent conversation's model or global Codex configuration. A future setup workflow must explain any host action required to apply a preference.

The proposed user storage path is `$CODEX_HOME/pancake-stack/config.json`. When `CODEX_HOME` is unset, the path is `~/.codex/pancake-stack/config.json`. No file is written there in this foundation. Project overrides are deferred.
