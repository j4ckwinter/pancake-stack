# Project plan

## Current state

The library contains 19 shared workflows packaged for Codex, Claude Code, and Cursor. [plugin.json](../plugin.json) declares the current version. All hosts share the same workflow tree and task-scoped settings. Delegates inherit host settings unless the task explicitly overrides them or loaded instructions name an economy model for gathering delegates. Setup saves no preferences; legacy preference files remain untouched.

Shared reviewer execution, context isolation, completion tracking, and coverage rules live in [host-runtime.md](../skills/pancake/references/host-runtime.md). Challenge retains its review trigger; [change review](../skills/pancake/references/change-review.md) owns consequential preparation and implementation review for Fix, TDD, and the implementation sequence. The library remains declarative, without bundled executable helpers or tests.

Checks, fixtures, and detailed evidence live in [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals). [CI](../.github/workflows/checks.yml) checks out a pinned published evaluator beside the library. See [verification](verification.md) for evidence and limits.

Codex and Claude Code installed and discovered all 19 skills in isolated profiles for version 0.21.3. Installed Codex trials exercised a consequential migration with the default independent reviewer and a two-reviewer Challenge panel. A separate baseline/Pancake/Poteto pilot measured outcomes and overhead; it does not establish general superiority.

Check now traces representative valid operations through changed acceptance gates. Direct Fix and TDD trials demonstrated the existing safeguards; a shared reference makes consequential preparation and review ownership explicit. The TypeScript split was rejected, and existing specialized workflows gained clearer metadata and recipes. Selective experiment references now reduce observed reading in three bounded task pairs while preserving their outcomes. Natural-request routing and unrelated acceptance cases extend coverage without adding skill wording. Delegation guidance now has a single owner, and pre-edit classification covers consequential agent-instruction changes. External evaluation adds retained sample batches and executed PR-maintenance cases. The implementation sequence is now shorter, and unresolved consequential design choices default to independent exploration while small or settled choices remain direct. A conditional cookoff split was rejected after mixed reading results. New coordination coverage exercises delegated implementation, fresh-state recipes, and returned artifacts. Pilot, recipe, and late-result wording additions were rejected after bounded trials. See the [0.21.15 verification record](verification.md#version-02115) for evidence and limits.

Natural repair trials now cover direct entrypoints with implementation workers permitted but not requested. Additional routing links were rejected after they increased reading without changing observed outcomes. Fix moves its existing ambiguous-cause observation earlier, with bounded behavior preserved. Short task and steering recipes use the existing skills. See the [0.21.16 verification record](verification.md#version-02116) for evidence and limits.

Versions 0.21.17 and 0.21.18 put needed application foundations before dependent features and add scoped Comment Critic review before implementation correctness review. Version 0.21.19 adds explicit multi-model panels to Check and Challenge while ordinary Check remains direct. Bounded source-skill trials covered panel routing, completed verdicts, and unsupported-model gaps; they did not measure an accuracy or cost advantage. See the [0.21.17](verification.md#version-02117), [0.21.18](verification.md#version-02118), and [0.21.19](verification.md#version-02119) records.

Version 0.21.20 strengthens Verify with selective failure-detection checks, baseline comparisons for existing fixes, and optional model-to-code verification guidance. Check distinguishes introduced or newly exposed regressions from unrelated pre-existing defects. Five bounded source-skill trials exercised these paths. They do not establish improvement over prior guidance or installed-host behavior. All 19 skills remain. See the [0.21.20 verification record](verification.md#version-02120).

Version 0.21.23 states the shared evidence, verification, and permission guards once in the core values and removes sentences that only restated them. The entry skill's task-choice section and competing designs defer to host guidance for delegate settings, and the comment pass before implementation review runs directly. One independent reviewer read the change; no agent trials ran. See the [0.21.23 verification record](verification.md#version-02123).

Version 0.21.24 lets read-only gathering delegates run on an economy model that the user names, while reviewers, candidates, judges, implementation workers, and the lead keep their settings. Two Claude Code trials observed the named model on gathering delegates and the inherited model on a reviewer; gathering accuracy was not compared. See the [0.21.24 verification record](verification.md#version-02124).

Version 0.21.25 licenses the library under MIT and records authenticated Claude Code use on 2.1.326. Skill content is unchanged; no new agent trials ran. See the [0.21.25 verification record](verification.md#version-02125).

Version 0.21.26 makes the README lead with pancake as the single entry point. Skill content is unchanged; no agent trials ran. See the [0.21.26 verification record](verification.md#version-02126).

Cursor uses the existing portable manifest. The [Cursor guide](cursor.md) documents local loading. On 21 November 2026 Jack reported that installed Cursor loads and runs the skills, and that current installed Codex workflows were checked. No evaluator record backs either report.

On 21 November 2026, 34 headless Claude Code trials from source skill trees ran authenticated How, Fix, Check, Setup, reviewer panels and competing Design. Requested delegate models and efforts matched what session records showed applied. A named `haiku` economy model for gathering found every environment-variable read on one fixture at under half the inherited model's reported cost. Multi-model and same-model panels both found every seeded defect with no false findings. The 0.21.23 values consolidation showed no regression against the earlier tree. See the [Claude workflow checks](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/claude-workflow-checks.md).

## Next

1. Define and run a bounded real-repository evaluation in the external evaluator. Select representative implementation and review tasks, pin the inputs and baseline, and define correctness and scope checks before running trials. Record outcomes, time, tokens, and limitations. Include acceptance-path review and valid-operation controls; existing repository and synthetic trials do not establish a general advantage.
2. Verify visible skill-picker behavior on supported hosts. Headless Claude trials cannot observe it.
3. Use observed failures or measured benefits to choose further guidance changes. Multi-model and same-model review were indistinguishable on saturated cases; claim better detection only after harder cases separate them. Retain rejected wording experiments and their reasons in the evaluator. Economy-model gathering matched the inherited model on one fixture; check more fixtures before claiming general parity.

Keep the CI evaluator pin on a published, verified revision and run package checks after library changes. Keep tests, trial artifacts, and detailed evidence in the external evaluator. Planning these checks does not authorize installation changes or live experiments.

Historical plans and dated verification records remain in the evaluation repository. License selection, publication, and changes to a user's plugin installation require separate authorization.
