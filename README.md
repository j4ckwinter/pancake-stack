# pancake stack

i love how quickly ai lets me move. i hate the slop i end up building, fixing, and reviewing. speed isn’t worth much if i spend the next day cleaning up.
what i do love is pancakes. so naturally, i made a stack.
these are the skills i use every day to help ai write code i actually want to keep.

## install it

the same 19 skills are packaged for Codex, Claude Code, and Cursor. pick the one you use: [Codex](#codex), [Claude Code](#claude-code), or [Cursor](#cursor).

for Codex or Claude Code, grab the repo first. if you already have it, open a terminal in that checkout instead. Cursor users can skip straight to the [Cursor instructions](#cursor).

```sh
git clone https://github.com/j4ckwinter/pancake-stack.git
cd pancake-stack
```

run the Codex or Claude Code commands below from the `pancake-stack` folder. the shell examples use bash or zsh.

### Codex

with the Codex CLI installed, run:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack --json
```

open a new Codex chat and start your request with `$pancake-stack:pancake`. if your client has a skill picker, look for **Pancake**.

CLI installation and discovery have been tested; the visible picker hasn’t. [installation details and updates](docs/codex-installation.md).

### Claude Code

with Claude Code installed, run:

```sh
claude plugin marketplace add ./
claude plugin install pancake-stack@pancake-stack
```

open a new Claude Code session and start your request with `/pancake-stack:pancake`.

the plugin reads from this checkout, so keep the folder around. edits take effect in a new session or after `/reload-plugins`. package validation and discovery passed; authenticated workflow checks are still pending. [details and one-session use](docs/claude.md).

### Cursor

with Git installed, run this from any folder to clone directly into Cursor’s local plugins folder:

```sh
git clone https://github.com/j4ckwinter/pancake-stack.git \
  "$HOME/.cursor/plugins/local/pancake-stack"
```

restart Cursor or run **Developer: Reload Window**. open **Customize** to check for the plugin, then type `/` in Agent chat and select `pancake`.

to update, run this and reload Cursor again:

```sh
git -C "$HOME/.cursor/plugins/local/pancake-stack" pull --ff-only
```

if you already copied the plugin into that folder, follow the [migration instructions](docs/cursor.md#switch-from-a-manual-copy) first. local plugin imports must be allowed. this uses Cursor’s documented local plugin folder, but loading and workflows haven’t been tested yet. [details and manual-copy fallback](docs/cursor.md).

## try it out

select pancake using your environment’s instructions above, then give it a small task:

> Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

when you have work to do, tell it what you want, where to look, and how you’ll know it works.

## use it

examples below use Codex’s `$pancake-stack:<skill>` syntax. in Claude Code, use `/pancake-stack:<skill>`. in Cursor, type `/` and select the skill by name.

pancake also handles runtime diagnosis, performance experiments, PR feedback triage, and matching an existing interface. see the [workflow recipes](docs/recipes.md#use-pancakes-specialized-workflows) for examples and the actions each request authorizes.

for substantial work, pancake delegates useful independent investigation or implementation tasks when the host and your instructions allow it. it explains each agent's assignment and brings the results together. small or tightly coupled tasks stay with the main agent.

for an interrogate-style review, request a multi-model panel:

> $pancake-stack:challenge Challenge this proposal using multi-model review. Choose two distinct supported models. Check their findings against the code and report any missing coverage. Do not apply fixes.

use `$pancake-stack:check` with the same reviewer request for a diff review. see [reviewer recipes](docs/recipes.md#request-independent-or-multi-model-review) for explicit model choices and host limitations.

there are [prompt recipes](docs/recipes.md) if you want a starting point, or you can pick a skill directly:

<details>
<summary>all the other skills</summary>

| skill | use it to |
| --- | --- |
| `$pancake-stack:setup` | choose delegate and reviewer settings for the current task. |
| `$pancake-stack:scope` | work out what a ticket needs. |
| `$pancake-stack:design` | plan a change and compare approaches. |
| `$pancake-stack:how` | explain how the code works. |
| `$pancake-stack:why` | investigate why it was built that way. |
| `$pancake-stack:teach` | explain a concept at your pace. |
| `$pancake-stack:check` | review a change for bugs and regressions. |
| `$pancake-stack:challenge` | stress-test assumptions with optional multi-model review. |
| `$pancake-stack:fix` | figure out what broke and fix it. |
| `$pancake-stack:tdd` | write and run a failing test, then implement the behavior. |
| `$pancake-stack:verify` | check it works and say what still needs checking. |
| `$pancake-stack:sift` | clean up supplied prose. |
| `$pancake-stack:wtf` | make the previous answer clearer. |
| `$pancake-stack:balls` | draft a standup with blockers, aims, and lessons learned. |
| `$pancake-stack:pr` | draft a PR title and description. |
| `$pancake-stack:handoff` | leave someone enough context to pick things up. |
| `$pancake-stack:recap` | catch up on decisions and unfinished work. |
| `$pancake-stack:reflect` | find lessons and propose improvements. |

</details>

## a bit more

[configuration](docs/configuration.md) and [setup](docs/setup.md) cover task settings and optional reviewers. [verification](docs/verification.md) covers checks and known limitations; the [installation record](docs/installation-verification.md) keeps the host-specific results.
