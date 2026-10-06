# pancake stack

i love how quickly ai lets me move. i hate the slop i end up building, fixing, and reviewing. speed isn’t worth much if i spend the next day cleaning up.
what i do love is pancakes. so naturally, i made a stack.
these are the skills i use every day to help ai write code i actually want to keep.

## try it out

Pancake Stack packages one shared set of 19 skills for Codex and Claude Code.

### Codex

run these from the repo:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack
```

then open a new Codex chat.

In the skill picker, the main workflow is **Pancake**. Individual skills use short labels such as **PR**, **Wtf**, and **Fix**. Their internal names remain namespaced. On hosts that include skills in slash autocomplete, type `/pancake` to filter the list and select **Pancake**. This is picker selection, not a standalone slash alias. See the [installation record](docs/installation-verification.md) for host verification.

start with one small task:

> $pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

### Claude Code

Load the plugin for one session from the repo:

```sh
claude --plugin-dir .
```

Then use the same task with Claude Code's native skill syntax:

> /pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

Use `/pancake-stack:setup`, `/pancake-stack:design`, or any other skill below by replacing the Codex `$` prefix with `/`. The workflows, review requirements, and verification rules come from the same files. Each host keeps its own model preferences.

Claude Code 2.1.291 has validated the package and discovered all 19 skills. Authenticated workflow and reviewer-setting parity checks remain pending. See [Claude Code support](docs/claude.md) for installation and verification scope.

### Choose the work

then choose what you need:

1. use `$pancake-stack:setup` if you want saved model and reasoning preferences. you can also leave settings inherited from your host.
2. use `$pancake-stack:pancake` for implementation. give it the outcome, relevant files, and how you will know it works.
3. use `$pancake-stack:design` before implementation when you need to settle the approach.

setup saves your preferences for later. it doesn't switch the model in your current chat.

see [prompt recipes](docs/recipes.md) for concrete tasks and host limitations.

## the rest

you can also reach for a skill directly when you know what you need.

<details>
<summary>all the other skills</summary>

| skill | use it to |
| --- | --- |
| `$pancake-stack:scope` | Work out what a ticket needs. |
| `$pancake-stack:design` | Plan a change and compare approaches. |
| `$pancake-stack:how` | Explain how the code works. |
| `$pancake-stack:why` | Investigate why it was built that way. |
| `$pancake-stack:teach` | Explain a concept at your pace. |
| `$pancake-stack:check` | Review a change for bugs and regressions. |
| `$pancake-stack:challenge` | Stress-test assumptions and decisions. |
| `$pancake-stack:fix` | Figure out what broke and fix it. |
| `$pancake-stack:tdd` | Write and run a failing test, then implement the behavior. |
| `$pancake-stack:verify` | Check it works and say what still needs checking. |
| `$pancake-stack:sift` | Clean up supplied prose. |
| `$pancake-stack:wtf` | Make the previous answer clearer. |
| `$pancake-stack:balls` | Draft a standup with blockers, aims, and lessons learned. |
| `$pancake-stack:pr` | Draft a PR title and description. |
| `$pancake-stack:handoff` | Leave someone enough context to pick things up. |
| `$pancake-stack:recap` | Catch up on decisions and unfinished work. |
| `$pancake-stack:reflect` | Find lessons and propose improvements. |

</details>

Repository checks run with `python3 -B -m unittest discover -s tests -v`. They validate package relationships, documented skills, the repository's plain single-line skill headers, relative inline links, preference helpers in temporary storage, and behavioral fixture assessment. The package checks use a limited repository profile rather than implementing the full portable JSON schema, YAML, or Markdown standards. They do not install the plugin or change global preferences. See [accepted safeguards](docs/safeguards.md) for evidence and remaining workflow gaps.

Challenge and consequential implementation review support separate optional reviewer panels. Design can run competing independent proposals and an independent judge when explicitly requested. These workflows stay proportionate by default. Setup preserves existing preferences and upgrades the schema only when you choose a new saved panel. See [configuration](docs/configuration.md) and [setup](docs/setup.md). Model selection depends on the active delegation host.
