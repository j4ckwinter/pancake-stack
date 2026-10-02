# Installation verification

Verified on 2 October 2026 with VS Code extension `openai.chatgpt-26.930.21537-darwin-arm64` and its bundled `codex-cli 0.159.0-alpha.12.1`.

## Local installation results

The following commands ran successfully against this repository:

```sh
codex plugin marketplace add /Users/jackwinter/dev/pancake-stack --json
codex plugin add pancake-stack@pancake-stack-local --json
codex plugin list --marketplace pancake-stack-local --json
```

Marketplace registration returned `pancake-stack-local`. Installation returned version `0.0.1`. Listing returned `installed: true` and `enabled: true`.

The installed package is at `~/.codex/plugins/cache/pancake-stack-local/pancake-stack/0.0.1`. Its parsed manifest matches the source manifest. It contains no `SKILL.md` files.

This check registered the marketplace and installed the plugin in the user's local Codex configuration. It did not create workflow preferences.

## Invocation contract

The [official skill documentation](https://learn.chatgpt.com/docs/build-skills) describes `$` mentions for explicit skill invocation in Codex CLI and the IDE extension. The planned entry points are `$setup pancake-stack` and `$pancake`. These remain proposed until the skills exist and their picker entries are checked.

The [documented IDE slash commands](https://learn.chatgpt.com/docs/developer-commands?surface=ide) do not establish `/add-plugin`, `/setup`, or `/pancake` as supported aliases. Plugin packaging alone does not establish those commands.

Local extension inspection adds evidence beyond the documented built-in commands. Its `webview/assets/app-initial-cda1f6c9f354.js` groups enabled skills under `composer.slashCommands.skillsGroup` and inserts a skill mention when a skill is selected through `onSelectFromInlineSlash`. The extension also contains plugin installation UI resources. This supports the possibility of `/pancake` in the skill picker after implementation. The exact entry name, namespacing, and live execution remain unchecked.

The [official packaging documentation](https://developers.openai.com/plugins/build/plugins) describes Git marketplace registration with `codex plugin marketplace add owner/repo`. For this repository, the candidate distribution flow is:

```sh
codex plugin marketplace add j4ckwinter/pancake-stack
codex plugin add pancake-stack@pancake-stack-local
```

The Git-backed install was not run. The marketplace name remains `pancake-stack-local` because that is the catalog's identity, even when registered from Git.

## Verification limits

Step 2 added the setup skill and bumped the package to `0.1.0`. A second `codex plugin add pancake-stack@pancake-stack-local --json` installed that version successfully. The bundled Codex app server's `skills/list` response reported the installed skill as `pancake-stack:setup`, with `enabled: true` and plugin ID `pancake-stack@pancake-stack-local`. Use `$pancake-stack:setup` as the backend-discovered name. The earlier `$setup pancake-stack` form remains unverified.

The local package installation passed through the extension's bundled CLI. No VS Code UI automation was available. Backend discovery of setup passed, but no live conversational skill invocation was tested. Composer discovery, actual workflow execution, and Git-backed installation remain unverified.

After setup and pancake skills are implemented, a new Codex chat must verify their picker entries and execution. This installation result proves package installation only.
