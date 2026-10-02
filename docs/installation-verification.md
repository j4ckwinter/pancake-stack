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

## Current Pancake host trial

On 2 October 2026, this conversation exposed installed skills from version `0.3.0`. Its cached manifest also reports `0.3.0`; repository version `0.14.27` includes Pancake and the later workflow changes. The earlier source-path trials do not verify this installed copy.

Refresh the local installation using the host's plugin installation flow, then start a new VS Code Codex chat. Before testing, confirm the selected Pancake skill resolves to the updated installed copy and its manifest reports `0.14.27`. Do not replace a missing installed skill with a repository file path, because that would repeat the source-path checks.

Select `$pancake-stack:pancake` in the new chat and send:

> Explain how the setup preference helper resolves a role's model and reasoning effort. Keep this read-only. Cite the implementation and distinguish saved preferences from choices actually applied by the host.

Record the installed version, whether the picker offers Pancake, the answer, relevant source citations, any preference fallback notice, and `git status --short` before and after. A correct answer should describe independent field resolution from role override to defaults to observable host settings. Resolving preferences alone does not apply them. The workspace should remain unchanged.

The local installation was refreshed with `codex plugin add pancake-stack@pancake-stack-local --json`. The CLI reported version `0.14.27` at `/Users/jackwinter/.codex/plugins/cache/pancake-stack-local/pancake-stack/0.14.27`. Byte comparison confirmed the installed manifest and all 32 skill files match repository source. This confirms installation contents, not discovery in a new VS Code chat.

This first host trial remains pending. Passing it would verify discovery and one read-only workflow, not implementation, independent review, all preference combinations, or shorter slash aliases. The [official packaging guide](https://developers.openai.com/plugins/build/plugins) describes local marketplace refresh behavior; availability can vary by host surface.

### Installed-resource check

After refresh, this session's available-skill catalog exposed all 16 skills from the `0.14.27` cache, including `pancake-stack:pancake`. The assistant read installed Pancake, How, values, and Sift resources and inspected the repository preference helper for the prepared explanation. Resolution in `skills/setup/scripts/preferences.py` treats model and reasoning effort independently, using role override, defaults, then supplied host values. The helper prints resolved preferences; it does not select the host model.

Running the installed helper's `resolve` command returned null for both fields in all three roles. Host values were not supplied, so null remains inheritance rather than an observed model selection. `git status --short` was empty before and after this read-only check.

This confirms current-session catalog exposure and use of installed resources. The user has not yet selected Pancake in a fresh VS Code picker chat. That discovery and invocation check remains pending; this assistant-directed check does not establish shortcut behavior or independent workflow selection.

The candidate GitHub install flow is:

```sh
codex plugin marketplace add j4ckwinter/pancake-stack
codex plugin add pancake-stack@pancake-stack
```

The marketplace is now named `pancake-stack`. Earlier results above used its previous name, `pancake-stack-local`, and retain the original commands and cache paths. Installation under the renamed marketplace and the Git-backed flow remain unverified. Existing installations keep the previous marketplace identity until migrated.
