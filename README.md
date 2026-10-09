# pancake stack

i love how quickly ai lets me move. i hate the slop i end up building, fixing, and reviewing. speed isn’t worth much if i spend the next day cleaning up.
what i do love is pancakes. so naturally, i made a stack.
these are the skills i use every day to help ai write code i actually want to keep.

## try it out

the same skills work in Codex and Claude Code. run these commands from the repo.

### Codex

```sh
codex plugin marketplace add .
codex plugin add pancake-stack@pancake-stack
```

open a new Codex chat, then give it a task:

> $pancake-stack:pancake Explain how this project starts and where its main behavior lives. Keep this read-only and cite the code you inspect.

in hosts with a skill picker, look for **Pancake**. CLI installation and discovery have been tested; visible picker behavior remains unverified. see the [installation record](docs/installation-verification.md).

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

for substantial work, pancake delegates useful independent investigation or implementation tasks when the host and your instructions allow it. it explains each agent's assignment and brings the results together. small or tightly coupled tasks stay with the main agent.

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

[configuration](docs/configuration.md) and [setup](docs/setup.md) cover task settings and optional reviewers. [verification](docs/verification.md) covers checks, recorded results, and known limitations.
