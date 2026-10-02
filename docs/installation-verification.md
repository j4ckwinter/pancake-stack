# Installation verification

Checked on 2 October 2026 with VS Code extension `26.930.21537` and its bundled `codex-cli 0.159.0-alpha.12.1`.

## Verified behavior

- Local marketplace registration and plugin installation succeeded.
- The installed manifest and setup resources matched the source files.
- Codex backend discovery returned the enabled skill `pancake-stack:setup`.
- The user invoked setup in VS Code and received its preference prompt.
- The installed catalog helper returned eight model IDs with their supported reasoning efforts.

The initial live setup prompt requested manual IDs. The updated skill now runs the catalog helper before asking for choices. Its updated conversational behavior still needs the user's retest.

## Remaining checks

- Complete setup in VS Code and verify the selected preferences were saved.
- Install from GitHub in a clean user environment.
- Verify any shorter slash-command invocation forms once the relevant skills exist.

The candidate GitHub install flow is:

```sh
codex plugin marketplace add j4ckwinter/pancake-stack
codex plugin add pancake-stack@pancake-stack-local
```

`pancake-stack-local` is the catalog's name even when registered from Git. The Git-backed flow has not been tested.
