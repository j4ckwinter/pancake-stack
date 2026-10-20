# Project plan

## Current state

The library contains 19 shared workflows for Codex and Claude Code. [plugin.json](../plugin.json) declares the current version. Both hosts share the same workflow tree and task-scoped settings. Delegates inherit host settings unless the task explicitly overrides them. Setup saves no preferences; legacy preference files remain untouched.

Shared reviewer execution, context isolation, completion tracking, and coverage rules live in [host-runtime.md](../skills/pancake/references/host-runtime.md). Challenge retains its review trigger; [change review](../skills/pancake/references/change-review.md) owns consequential preparation and implementation review for Fix, TDD, and the implementation sequence. The library remains declarative, without bundled executable helpers or tests.

Checks, fixtures, and detailed evidence live in [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals). [CI](../.github/workflows/checks.yml) checks out a pinned published evaluator beside the library. See [verification](verification.md) for evidence and limits.

Both hosts installed and discovered all 19 skills in isolated profiles for version 0.21.3. Installed Codex trials exercised a consequential migration with the default independent reviewer and a two-reviewer Challenge panel. A separate baseline/Pancake/Poteto pilot measured outcomes and overhead; it does not establish general superiority.

Check now traces representative valid operations through changed acceptance gates. Direct Fix and TDD trials demonstrated the existing safeguards; a shared reference makes consequential preparation and review ownership explicit. The TypeScript split was rejected, and existing specialized workflows gained clearer metadata and recipes. See the [0.21.11 verification record](verification.md#version-02111) for bounded evidence and reading-volume limits.

## Next

- Keep the CI evaluator pin on a published, verified revision.
- Authenticated Claude workflows remain deferred. Visible picker behavior remains unverified on supported hosts.
- Extend repository evaluation beyond the two paired review tasks to other projects and implementation work. The first 16 repository review trials passed in both arms; they do not establish general superiority.
- Extend acceptance-path review beyond the historical fixture. The revised instruction detected that target in bounded trials; residual assessor addition-scope limitations remain documented in the evaluator.
- Retain current Verify wording. The validation-test pilot passed with current and proposed guidance.

Historical plans and dated verification records remain in the evaluation repository. License selection, publication, and changes to a user's plugin installation require separate authorization.
