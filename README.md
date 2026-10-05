# pancake stack

i love how quickly ai lets me move. i hate the slop i end up building, fixing, and reviewing. speed isn’t worth much if i spend the next day cleaning up.
what i do love is pancakes. so naturally, i made a stack.
these are the skills i use every day to help ai write code i actually want to keep.

## try it out

run these from the repo:

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack
```

then open a new Codex chat.

In the skill picker, the main workflow is **Pancake**. Individual skills use short labels such as **PR**, **Wtf**, and **Fix**. Their internal names remain namespaced. On hosts that include skills in slash autocomplete, type `/pancake` to filter the list and select **Pancake**. This is picker selection, not a standalone slash alias. See the [installation record](docs/installation-verification.md) for host verification.

two things to start with:

1. use `$pancake-stack:setup` to pick your models and reasoning effort.
2. use `$pancake-stack:pancake` when a task needs some rigor. tell it what you need, and it picks the relevant workflow.

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

Challenge supports an optional configured reviewer panel for independent reviews using different models. Setup preserves existing preferences and opts into schema 2 only when you choose a panel. See [configuration](docs/configuration.md) and [setup](docs/setup.md). Model selection depends on the active delegation host.
