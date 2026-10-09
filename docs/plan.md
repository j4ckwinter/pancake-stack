# Project plan

## Current state

The library contains 19 shared workflows for Codex and Claude Code. [plugin.json](../plugin.json) declares the current version. Both hosts share the same workflow tree and task-scoped settings. Delegates inherit host settings unless the task explicitly overrides them. Setup saves no preferences; legacy preference files remain untouched.

Shared reviewer execution, context isolation, completion tracking, and coverage rules live in [host-runtime.md](../skills/pancake/references/host-runtime.md). Challenge and implementation retain their own review triggers. The library remains declarative, without bundled executable helpers or tests.

Checks, fixtures, and detailed evidence live in [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals). [CI](../.github/workflows/checks.yml) checks out a pinned published evaluator beside the library. Its command passed locally; the new workflow has not yet run on GitHub. See [verification](verification.md) for evidence and limits.

Both hosts installed and discovered all 19 skills in isolated profiles for version 0.21.3. Installed Codex trials exercised a consequential migration with the default independent reviewer and a two-reviewer Challenge panel. A separate baseline/Pancake/Poteto pilot measured outcomes and overhead; it does not establish general superiority.

## Next

- Observe the configured GitHub workflow after an authorized push. Publish evaluator updates separately before advancing its pin.
- Run authenticated Claude workflows and verify visible picker behavior on supported hosts.
- Exercise representative repository tasks beyond the synthetic fixtures.

Historical plans and dated verification records remain in the evaluation repository. License selection, publication, and changes to a user's plugin installation require separate authorization.
