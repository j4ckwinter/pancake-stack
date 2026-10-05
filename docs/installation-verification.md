# Installation verification

## Saved Challenge panel in 0.17.2

On 5 October 2026, the local installation was refreshed with `codex plugin add pancake-stack@pancake-stack --json`. It installed version `0.17.2` under the current `pancake-stack` marketplace. The CLI binary was byte-identical to the binary bundled with VS Code extension `26.930.51102`. These checks exercised fresh CLI sessions and app-server discovery, not the visible VS Code picker.

The [installed-panel evidence](evidence/installed-panel-2026-10-05.json) records these results.

| Check | Observed result |
| --- | --- |
| Discovery | App-server `skills/list` returned all 19 enabled, namespaced skills from the `0.17.2` cache with no discovery errors. |
| Installed resources | The manifest, Setup and Challenge instructions, catalog helper, and preference helper matched repository source bytes. |
| Setup | A fresh `$pancake-stack:setup` session used the installed catalog helper, saved two supported reviewer choices as schema 2, confirmed persistence, and preserved inherited defaults and roles. |
| Saved-panel application | A fresh `$pancake-stack:challenge` session read that saved configuration without task-supplied model choices. Retained host records show successful spawns and completed reviewer sessions for `gpt-6.1-sol` and `gpt-6-sol`, both at medium effort. |
| Missing preferences | A separate Challenge session resolved the inherited single-review fallback, performed direct review, disclosed that no independent reviewers ran, and left the missing file absent. |
| Empty panel | A separate Challenge session read an empty schema 2 panel and performed one direct review with no independent reviewers. The installed helper also resolved both empty and missing cases to supplied host values. |
| Unavailable reviewer choice | The installed catalog listed `gpt-5.6-terra`. A saved panel requesting it was reported unsupported by the active delegation host. Challenge performed direct review, disclosed the uncovered independent perspective, and selected no substitute. No rejected spawn was exercised. |
| Artifact checks | Trusted fixture assessment reproduced the consumer failure despite the passing exporter test and confirmed the project remained unchanged. All 36 repository checks passed. |

Preferences were stored at explicit temporary `--config` locations. Real user preferences were not changed. The two completed child sessions' `turn_context` records establish host-selected model and effort, not independent attestation of the remote inference runtime. Both models use the same provider. One child incorrectly described its configured preference, which reinforces using host records instead of reviewer self-description to establish selection.

Missing, empty, and reported unsupported reviewer-choice fallbacks passed. Rejected-spawn and unavailable-delegation fallback remain unverified. An additional run with `--disable multi_agent` still exposed collaboration and completed reviewers, so that flag did not establish an unavailable-delegation scenario in this host. Visible VS Code labels, picker filtering, Git-backed installation, and the default real-user preference save location remain separate checks.

The older entries below retain their original versions and pending checks. This result supersedes their pending local installation under the renamed marketplace and verifies the isolated saved-panel flow on the current CLI backend.

## Skill labels in 0.17.1

Each skill now declares an explicit UI display name in `agents/openai.yaml`. The main workflow is `Pancake`; individual workflows have short names such as `PR`, `Wtf`, and `Fix`, without the `Pancake Stack:` prefix. Internal plugin and skill identities remain unchanged.

Static inspection of VS Code extension `26.930.31730` found that its skill display-label function prefers `interface.displayName` over the formatted internal name. Repository validation checks the package and skill resources. These checks do not establish the visible picker result.

After refreshing the installation and opening a new chat, verify that typing `/pancake` still finds the bundled skills, that the main workflow displays as `Pancake`, and that selecting `PR` or `Wtf` invokes the intended namespaced skill. Filtering, ordering, and visible labels on the refreshed installation remain pending host checks. No standalone `/pancake` alias is claimed.

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
