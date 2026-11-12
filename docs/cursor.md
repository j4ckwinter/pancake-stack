# Cursor support

Cursor supports the existing root [plugin.json](../plugin.json) and shared `skills/` tree through the portable Agent Plugins format. No separate Cursor manifest is needed for these 19 skills. See Cursor’s [supported plugin formats](https://cursor.com/docs/reference/plugins).

## Load a local copy

These instructions follow Cursor’s [local plugin loading guide](https://cursor.com/docs/plugins#test-plugins-locally). They have not yet been tested in Cursor for Pancake Stack.

From the Pancake Stack checkout, copy the manifest, skills, and referenced documentation into a new local plugin directory:

```sh
mkdir -p "$HOME/.cursor/plugins/local"
mkdir "$HOME/.cursor/plugins/local/pancake-stack" &&
  cp -R plugin.json skills docs README.md "$HOME/.cursor/plugins/local/pancake-stack/"
```

The second `mkdir` refuses an existing destination, preventing an accidental merge with an older copy. This is a snapshot; checkout edits will not update it. For updates, move the previous copy outside the local plugins directory, then repeat the copy.

Restart Cursor or run **Developer: Reload Window**. In **Customize**, check that Pancake Stack and its 19 skills appear. Type `/` in Agent chat and select `pancake`, then send:

> Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

Cursor documents skill selection through the [slash picker](https://cursor.com/docs/skills). Use the displayed entry instead of assuming another host’s namespaced syntax. Select `setup` for help phrasing task settings.

Local imports must be allowed; Enterprise administrators control this setting. A marketplace installation with the same name takes precedence. Cursor skips symlinks whose targets are outside its local plugins directory.

## Distribution and verification

This guide provides local loading, not a public marketplace listing. Public distribution requires a separate submission and review through the [Cursor Marketplace](https://cursor.com/marketplace/publish).

Repository checks validate the package and skill references. Cursor loading, picker discovery, invocation, and delegated review remain unverified. The shared [host guidance](../skills/pancake/references/host-runtime.md) applies: use only exposed host controls, preserve task permissions, and report unsupported reviewer choices or missing independent review. Package validation does not establish those host behaviors.
