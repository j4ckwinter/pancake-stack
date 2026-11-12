# Cursor support

Cursor supports the existing root [plugin.json](../plugin.json) and shared `skills/` tree through the portable Agent Plugins format. No separate Cursor manifest is needed for these 19 skills. See Cursor’s [supported plugin formats](https://cursor.com/docs/reference/plugins).

## Clone into Cursor

Cursor documents the directory in its [local plugin loading guide](https://cursor.com/docs/plugins#test-plugins-locally). Cloning directly into it keeps the package updateable with Git. This recipe has not yet been tested in Cursor for Pancake Stack.

With Git installed, run from any directory:

```sh
git clone https://github.com/j4ckwinter/pancake-stack.git \
  "$HOME/.cursor/plugins/local/pancake-stack"
```

This creates a checkout of the repository's default branch. It does not include uncommitted changes from another checkout. If the destination already contains a manual copy, follow [Switch from a manual copy](#switch-from-a-manual-copy) first.

Restart Cursor or run **Developer: Reload Window**. In **Customize**, check that Pancake Stack and its 19 skills appear. Type `/` in Agent chat and select `pancake`, then send:

> Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

Cursor documents skill selection through the [slash picker](https://cursor.com/docs/skills). Use the displayed entry instead of assuming another host’s namespaced syntax. Select `setup` for help phrasing task settings.

Local imports must be allowed; Enterprise administrators control this setting. A marketplace installation with the same name takes precedence. Cursor skips symlinks whose targets are outside its local plugins directory.

## Update a cloned install

```sh
git -C "$HOME/.cursor/plugins/local/pancake-stack" pull --ff-only
```

Reload Cursor after updating. This follows the default branch, not a pinned release. If Git reports local changes or divergent history, resolve them in that checkout before retrying; do not discard edits just to update the plugin.

## Switch from a manual copy

Move the existing `pancake-stack` folder outside `~/.cursor/plugins/local`, preserving any edits you want to keep. Then run the clone command above and reload Cursor. The Git update command applies only to a cloned install.

## Manual-copy fallback

To try an existing checkout, including uncommitted changes, copy the manifest, skills, and referenced documentation instead. Run from that checkout with no existing destination:

```sh
mkdir -p "$HOME/.cursor/plugins/local"
mkdir "$HOME/.cursor/plugins/local/pancake-stack" &&
  cp -R plugin.json skills docs README.md "$HOME/.cursor/plugins/local/pancake-stack/"
```

The second `mkdir` refuses an existing destination. Reload Cursor after copying. This is a snapshot; checkout edits will not update it. To replace it, move the previous copy outside the local plugins directory and repeat the copy.

## Distribution and verification

This guide provides local loading, not a public marketplace listing. Public distribution requires a separate submission and review through the [Cursor Marketplace](https://cursor.com/marketplace/publish).

Repository checks validate the package and skill references. Cursor loading, picker discovery, invocation, and delegated review remain unverified. The shared [host guidance](../skills/pancake/references/host-runtime.md) applies: use only exposed host controls, preserve task permissions, and report unsupported reviewer choices or missing independent review. Package validation does not establish those host behaviors.
