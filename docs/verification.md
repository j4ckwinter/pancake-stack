# Verification

Package checks, Python tests, behavioral fixtures, detailed trial reports, and evidence now live in the separate [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals) repository. That repository preserves the original Git history through `795dc890ee0b0acf24e743d82362c4a92e4202e1`. The evaluator is hosted on GitHub. A local checkout is needed to run the checks, but not to use the skills.

## Run the checks

Clone [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals) beside your Pancake Stack checkout if it is not already available:

```sh
git clone https://github.com/j4ckwinter/pancake-stack-evals.git ../pancake-stack-evals
```

Run from the Pancake Stack checkout using the evaluator revision pinned in its CI workflow. A detached temporary worktree keeps an existing evaluator checkout and its uncommitted work intact:

```sh
pancake_evaluator_ref="$(sed -n 's/^          ref: //p' .github/workflows/checks.yml)"
test -n "$pancake_evaluator_ref"
git -C ../pancake-stack-evals fetch origin "$pancake_evaluator_ref"
pancake_evaluator_worktree="$(mktemp -d "${TMPDIR:-/tmp}/pancake-evals.XXXXXX")"
git -C ../pancake-stack-evals worktree add --detach "$pancake_evaluator_worktree" "$pancake_evaluator_ref"
python3 -B "$pancake_evaluator_worktree/run_checks.py" --source "$PWD" --output /tmp/pancake-checks.json
```

Inspect the command's outcome and `/tmp/pancake-checks.json`. Afterward, remove the temporary checkout:

```sh
git -C ../pancake-stack-evals worktree remove "$pancake_evaluator_worktree"
```

The `ref` comes from this checkout's [CI workflow](../.github/workflows/checks.yml), so an older library checkout uses its own evaluator pin. These are package checks; they do not install the plugin or register a marketplace.

The evaluator records both repository revisions, file hashes, including nonignored untracked files, dirty state, and whether checks changed either tree. Package validation covers JSON parsing, marketplace source resolution, skill metadata, and local documentation links. Historical preference and catalog tests use archived helpers in isolated temporary storage. They do not verify current runtime features.

The evaluation repository retains [behavioral results](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/behavioral-results.md), [baseline comparisons](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/baseline-comparison.md), [installation records](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/installation-verification.md), [safeguards](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/safeguards.md), and [evidence](https://github.com/j4ckwinter/pancake-stack-evals/tree/main/docs/evidence). These records describe the methods, results, and limitations. Historical reports also remain accessible in [the library history before extraction](https://github.com/j4ckwinter/pancake-stack/tree/795dc890ee0b0acf24e743d82362c4a92e4202e1/docs).

## Evidence limits

The October 2026 baseline pilot found more consistent reproduction and independent review with Pancake. Both treatments passed their artifact checks, and Pancake used more time and tokens. A subsequent reviewer pilot detected its seeded defects but did not establish lower overhead. Neither trial establishes broad correctness benefits.

Earlier Codex installation and workflow trials passed on their recorded versions. Claude packaging and skill discovery passed, while authenticated Claude workflows remained unverified. Installation, visible picker behavior, applied model selection, and live workflow behavior remain separate from structural validation.

## Version 0.21.9

Design now loads boundary, lifecycle, and migration guidance through conditional references. Its entry point contains 852 whitespace-separated words, down from 1,392. This measures the entry file, not total context consumption or model performance.

Explicit independent design cookoffs, including requests with candidate model choices, route to the existing candidate-isolation and separate-judge protocol. Planning guidance now separates the implementation sequence, phase tracking, and delegated-work mechanics. Shared resource isolation applies to partitioned workers as well as competing implementations.

The external evaluator records the [Design reading-path comparison](https://github.com/j4ckwinter/pancake-stack-evals/blob/52476b13decd8677b94a6077478dba4a5d83ed1f/docs/design-reading-paths.md), source identities, observed reads, outputs, and limitations. These are source-skill trials, not installed-host verification. The historical assessor detection gap remains unresolved; existing structural-variant checks do not establish improved review detection. Claude authenticated workflow status is unchanged.

All 127 local package and evaluator checks passed with both inputs unchanged. Independent code and evidence reviews completed. Ten comparison trials and one separate routing trial completed; the blinded assessment recorded 30 passed criteria and two unavailable neutral-brief criteria. Worker filename discovery outside the project and bundle is recorded as a scope limitation, separately from artifact preservation. CI pins the evaluator delivered in [evaluator PR #5](https://github.com/j4ckwinter/pancake-stack-evals/pull/5).

## Version 0.21.8

Design now applies the shared fresh-context rules to independent candidates as well as the judge. One [source-skill trial](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/design-isolation.md) observed fresh candidate and judge launches with completed verdicts. Encrypted briefs limit the neutrality audit.

The updated evaluator guards input identity in every live suite and adds [historical review](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/historical-review.md) and [context recovery](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/context-recovery.md). Both review arms missed the selected historical defect in both repetitions while reporting genuine additional gaps. The original control and a separate calibration follow-up retain their identities and cannot establish clean-control specificity. Current assessor regressions cover malformed archives, actual producer/reader compatibility, empty tests and both Boolean values. Recovery reached 20/20 required facts per arm. These small trials establish no general quality advantage.

All 121 package and evaluator checks passed. Independent implementation reviews and an evidence-consistency audit completed. The [Codex refresh recipe](codex-installation.md) records a tested local-checkout update and cached-version check. Local package verification now resolves CI's pinned evaluator through a temporary detached checkout. The [decision trail](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/gap-pass.md) records the corrections and limits. Claude authenticated workflow status is unchanged.

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

[Package checks](../.github/workflows/checks.yml) runs on pull requests, pushes to `main`, and manual dispatch. It checks out the library and evaluator as siblings, pins the evaluator and action revisions, grants read-only repository permissions, and retains the JSON result.

The 0.21.4 evaluator update was [published through PR #1](https://github.com/j4ckwinter/pancake-stack-evals/pull/1), and its 86 checks passed locally on 12 October 2026. Version 0.21.5 pins the [validation evaluator from PR #2](https://github.com/j4ckwinter/pancake-stack-evals/pull/2), with 97 passing local checks. Version 0.21.6 pins the [repository-review evaluator from PR #3](https://github.com/j4ckwinter/pancake-stack-evals/pull/3), with 104 passing local checks. Earlier [hosted CI at library revision `1405ff6`](https://github.com/j4ckwinter/pancake-stack/actions/runs/37963572728) used the older 70-check evaluator. Consult [current Actions results](https://github.com/j4ckwinter/pancake-stack/actions) for the exact library revision and hosted outcome. Installation and live model trials remain separate from CI.
