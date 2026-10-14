# Install and refresh in Codex

These commands use a local Git checkout as the marketplace source. They were tested with Codex CLI 0.160.0 in an isolated profile, including an update from 0.21.6 to 0.21.7 and a repeated install. The installed manifest and all skill resources matched the checkout at each step. See the [trial record](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/codex-refresh.md).

## Get the source

If you do not already have a checkout:

```sh
git clone https://github.com/j4ckwinter/pancake-stack.git
cd pancake-stack
```

Register that checkout once:

```sh
codex plugin marketplace add .
```

Keep this checkout at the registered location. Codex copies the plugin into its installation cache; pulling new source alone does not refresh that installed copy.

## Refresh the source

For an existing checkout, run from its root:

```sh
git pull --ff-only
```

Then install the updated copy using the next block. Registration is not required again when the checkout stays at the same path.

## Install and confirm the cached version

```sh
codex plugin add pancake-stack@pancake-stack --json |
python3 -c '
import json, pathlib, sys
receipt = json.load(sys.stdin)
installed = pathlib.Path(receipt["installedPath"])
manifest = json.loads((installed / "plugin.json").read_text())
print(manifest["name"], manifest["version"])
print(installed)
'
```

This prints the version read from the installed copy and its location. Repeating the command on the tested version retained the same installed resources. You can also inspect the active installation:

```sh
codex plugin list --marketplace pancake-stack --json
```

Open a new Codex chat after installing or refreshing. An existing chat can retain earlier instructions. This recipe verifies CLI installation and cached resources; visible picker behavior and live workflow behavior have separate [verification records](installation-verification.md).

The [official Codex plugin documentation](https://developers.openai.com/plugins/build/plugins) describes local and Git marketplace sources. This recipe tests the local-checkout route only.
