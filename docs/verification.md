# Verification

Package checks, Python tests, behavioral fixtures, detailed trial reports, and evidence now live in the separate [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals) repository. That repository preserves the original Git history through `795dc890ee0b0acf24e743d82362c4a92e4202e1`. The evaluator is hosted on GitHub. A local checkout is needed to run the checks, but not to use the skills.

## Run the checks

Clone [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals) beside your Pancake Stack checkout if it is not already available:

```sh
git clone https://github.com/j4ckwinter/pancake-stack-evals.git ../pancake-stack-evals
```

Then run from the Pancake Stack checkout:

```sh
python3 -B ../pancake-stack-evals/run_checks.py --source . --output /tmp/pancake-checks.json
```

The evaluator records both repository revisions, file hashes, including nonignored untracked files, dirty state, and whether checks changed either tree. Package validation covers JSON parsing, marketplace source resolution, skill metadata, and local documentation links. Historical preference and catalog tests use archived helpers in isolated temporary storage. They do not verify current runtime features.

The evaluation repository retains [behavioral results](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/behavioral-results.md), [baseline comparisons](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/baseline-comparison.md), [installation records](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/installation-verification.md), [safeguards](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/safeguards.md), and [evidence](https://github.com/j4ckwinter/pancake-stack-evals/tree/main/docs/evidence). These records describe the methods, results, and limitations. Historical reports also remain accessible in [the library history before extraction](https://github.com/j4ckwinter/pancake-stack/tree/795dc890ee0b0acf24e743d82362c4a92e4202e1/docs).

## Evidence limits

The October 2026 baseline pilot found more consistent reproduction and independent review with Pancake. Both treatments passed their artifact checks, and Pancake used more time and tokens. A subsequent reviewer pilot detected its seeded defects but did not establish lower overhead. Neither trial establishes broad correctness benefits.

Earlier Codex installation and workflow trials passed on their recorded versions. Claude packaging and skill discovery passed, while authenticated Claude workflows remained unverified. Installation, visible picker behavior, applied model selection, and live workflow behavior remain separate from structural validation.

## Version 0.21.7

This release adds [onboarding recipes](recipes.md) for turning a ticket into an implementation brief, pausing and resuming work in a fresh chat, and drafting a pull request from the actual branch diff. Each sequence names its expected output and distinguishes read-only preparation from an authorized continuation.

All 104 external package and evaluator checks passed, including JSON parsing, marketplace source resolution, skill metadata, and local documentation links. Independent review checked the examples against the existing Scope, Handoff, Recap, PR, and Pancake contracts. These are documented prompts, not new installed-host trial results. All 19 skill implementations, the evaluator pin, and Claude workflow support remain unchanged.

## Version 0.21.6

This release adds a [repository review pilot](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/repository-review.md) and pins its evaluator. A frozen, provenance-checked evaluator repository supplies two paired review tasks. Each has a behavior-preserving refactor and a seeded regression. The suite now has 104 checks.

Sixteen isolated source-skill trials compared baseline review with Pancake Check in two counterbalanced repetitions. Each arm detected all four presented defects and reported no actionable findings on its four clean controls. Every trial completed and preserved its workspace. Independent assessment agreed with all 16 outcomes.

These are seeded defects in two real repository modules, not historical bugs or broad evidence of review superiority. Candidate checks used inspection and in-memory probes under a read-only sandbox. Separate evaluator probes exercised filesystem behavior before the trials. All 19 skill implementations remain unchanged. Claude support is unchanged.

## Version 0.21.5

This release adds a [validation-test quality pilot](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/validation-controls.md) and pins its evaluator. The evaluator checks generated rejection tests against a correct reader and separate boolean and float validation mutants. A test that rejects the wrong field cannot earn success. The suite now has 97 checks.

Four isolated source-skill trials compared current Verify guidance with a proposed clarification. Both arms passed both mutants in both repetitions and retained valid-version assertions. Independent code review and a blinded artifact assessment passed. The added wording showed no correctness advantage in this task, so all 19 skill implementations remain unchanged. The published report preserves exact input hashes, generated tests, results, and limitations.

This single synthetic task does not establish general test quality, installed-host behavior, or a performance improvement. Repository-based review coverage remains the next evaluation step. Claude support is unchanged.

## Version 0.21.4

This release updates verification documentation and the pinned evaluator. The 19 skill implementations are unchanged from 0.21.3. Shared reviewer mechanics and conditional Design references already address the earlier consolidation proposals.

The evaluator now has 86 checks and a separate [three-arm review comparison](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/review-comparison.md). Its 12-run source-skill pilot covered zero-valued configuration and deferred file consumption, each with a faulty change and a clean control. Every arm detected both seeded defects and reported no unsupported actionable findings. An independent assessor counted no unnecessary-work episodes under the predeclared rubric. Cost remains a separate observation, not evidence of unnecessary work by itself.

The pilot used unchanged 0.21.3 skills, one repetition, one candidate model, and one CLI host. It does not establish general superiority, repeatability, or installed 0.21.4 behavior. Authenticated Claude workflows remain deferred. The [installation record](installation-verification.md) retains the earlier host checks without relabeling them as a new trial.

## Version 0.21.3, 9 October 2026

Version 0.21.3 passed all 80 checks in the local evaluator, including JSON parsing, marketplace source resolution, all 19 skills, and historical helper tests. Independent static review found no actionable regressions in the reviewer-rule consolidation. Both hosts installed the package in temporary profiles and discovered all 19 skills with matching resources.

Two installed Codex trials exercised the consolidated reviewer rules. A migration preserved the public keyword API and archives while completing the default independent review. Challenge completed both requested reviewers, found the seeded consumer regression, and preserved the fixture. Exact prompts, hashes, and verdicts are retained in the evaluator's [reviewer report](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/reviewer-consolidation.md) and [evidence](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/evidence/reviewer-consolidation-2026-10-09.json).

A 12-trial baseline/Pancake/Poteto pilot covered a tiny edit and a compatibility migration. Eleven trials completed; one Poteto migration timed out. All retained outputs passed corrected primary artifact checks. A separate posthoc numeric audit found a compatibility restriction in one completed Poteto migration. Pancake used less time and fewer tokens than Poteto in this pilot, and more than baseline. The evaluator's `docs/three-arm-comparison.md` records the assessment correction and limits. Two repetitions per case on one host/model cannot establish broad efficacy.

Claude authenticated workflows and visible picker behavior remain unverified. The Codex trials establish fresh-context requests and completed worker verdicts, but encrypted brief text prevents a full neutrality audit. No model diversity is claimed.

## Version 0.20.0 source verification

The external suite has 70 checks, including historical helper tests. Package validation accepts all 19 skills and rejects Python files, bundled script directories, tests, hooks, and evaluation evidence in the library. Historical tests are labeled separately from current library behavior.

Two scoped source-skill trials exercised the simplified instructions. Setup explained that future-chat defaults cannot be saved and returned task wording for two reviewers with inherited settings. A Challenge trial spawned two independent reviewers, retained both completed verdicts, and found a seeded keyword-argument regression despite passing fixture tests. The fixture remained unchanged. The host accepted inherited reviewer settings without reporting exact model IDs; model diversity is not claimed.

Independent review found and corrected incomplete input hashing in the external evaluator and stale references to persistent Setup in personalization guidance. Detailed records and revision identifiers live in the [library split record](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/library-split.md) and its [evidence file](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/evidence/library-split-2026-10-07.json). The generic skill-creator validator could not run in the trial environment because PyYAML was absent; the repository-specific validator passed. Version 0.20.0 installation and authenticated Claude workflow checks remain pending.

## Automated package checks

[Package checks](../.github/workflows/checks.yml) runs on pull requests, pushes to `main`, and manual dispatch. It checks out the library and evaluator as siblings, pins evaluator revision `b2453e0b13acd8f66875ecd6388c0082273f0b2a` and action revisions, grants read-only repository permissions, and retains the JSON result.

The 0.21.4 evaluator update was [published through PR #1](https://github.com/j4ckwinter/pancake-stack-evals/pull/1), and its 86 checks passed locally on 12 October 2026. Version 0.21.5 pins the [validation evaluator from PR #2](https://github.com/j4ckwinter/pancake-stack-evals/pull/2), with 97 passing local checks. Version 0.21.6 pins the [repository-review evaluator from PR #3](https://github.com/j4ckwinter/pancake-stack-evals/pull/3), with 104 passing local checks. Earlier [hosted CI at library revision `1405ff6`](https://github.com/j4ckwinter/pancake-stack/actions/runs/37963572728) used the older 70-check evaluator. Consult [current Actions results](https://github.com/j4ckwinter/pancake-stack/actions) for the exact library revision and hosted outcome. Installation and live model trials remain separate from CI.
