# pancake stack

i love how quickly ai lets me move. i hate the slop i end up building, fixing, and reviewing. speed isn’t worth much if i spend the next day cleaning up.
what i do love is pancakes. so naturally, i made a stack.
these are the skills i use every day to help ai write code i actually want to keep.

the library contains readable playbooks and plugin metadata, with no bundled Python scripts or test suite.

## try it out

the same skills work in Codex and Claude Code. run these commands from the repo.

### Codex

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack
```

open a new Codex chat, then give it a task:

> $pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

you can also select **Pancake** in the skill picker. see the [installation record](docs/installation-verification.md) for what’s been tested.

### Claude Code

load the plugin for one session:

```sh
claude --plugin-dir .
```

then give it the same task, using `/` instead of `$`:

> /pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

Claude Code has validated the package and found all 19 skills. authenticated workflow and reviewer-setting checks are still pending. see [Claude Code support](docs/claude.md) for details.

## use it

reach for `$pancake-stack:pancake` when you have work to do. tell it what you want, where to look, and how you’ll know it works.

use `$pancake-stack:design` when you want to settle the approach first. use `$pancake-stack:setup` to phrase delegate and reviewer choices for the current task. delegates inherit host settings unless you request an override. setup runs no bundled scripts and saves no preferences.

there are [prompt recipes](docs/recipes.md) if you want a starting point, or you can pick a skill directly:

<details>
<summary>all the other skills</summary>

| skill | use it to |
| --- | --- |
| `$pancake-stack:scope` | work out what a ticket needs. |
| `$pancake-stack:design` | plan a change and compare approaches. |
| `$pancake-stack:how` | explain how the code works. |
| `$pancake-stack:why` | investigate why it was built that way. |
| `$pancake-stack:teach` | explain a concept at your pace. |
| `$pancake-stack:check` | review a change for bugs and regressions. |
| `$pancake-stack:challenge` | stress-test assumptions and decisions. |
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

[configuration](docs/configuration.md) and [setup](docs/setup.md) cover task settings and optional reviewers. [verification](docs/verification.md) explains the external evaluation repository, recorded results, and remaining gaps.

Tests and evaluation tools live in the separate local `pancake-stack-evals` repository. Maintainers can run them against this checkout with:

```sh
python3 -B ../pancake-stack-evals/run_checks.py --source . --output /tmp/pancake-checks.json
```

The evaluation repository is local-only, so automatic GitHub checks are pending a remote and access configuration. Using the skills does not require the evaluation repository.
