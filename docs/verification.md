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

## Current checks, 9 October 2026

Version 0.21.3 passed all 80 checks in the local evaluator, including JSON parsing, marketplace source resolution, all 19 skills, and historical helper tests. Independent static review found no actionable regressions in the reviewer-rule consolidation. Both hosts installed the package in temporary profiles and discovered all 19 skills with matching resources.

Two installed Codex trials exercised the consolidated reviewer rules. A migration preserved the public keyword API and archives while completing the default independent review. Challenge completed both requested reviewers, found the seeded consumer regression, and preserved the fixture. Exact prompts, hashes, and verdicts are retained in the evaluator's `docs/reviewer-consolidation.md` and `docs/evidence/reviewer-consolidation-2026-10-09.json`. These new evaluator records are committed locally; publication is separate.

A 12-trial baseline/Pancake/Poteto pilot covered a tiny edit and a compatibility migration. Eleven trials completed; one Poteto migration timed out. All retained outputs passed corrected primary artifact checks. A separate posthoc numeric audit found a compatibility restriction in one completed Poteto migration. Pancake used less time and fewer tokens than Poteto in this pilot, and more than baseline. The evaluator's `docs/three-arm-comparison.md` records the assessment correction and limits. Two repetitions per case on one host/model cannot establish broad efficacy.

Claude authenticated workflows and visible picker behavior remain unverified. The Codex trials establish fresh-context requests and completed worker verdicts, but encrypted brief text prevents a full neutrality audit. No model diversity is claimed.

## Version 0.20.0 source verification

The external suite has 70 checks, including historical helper tests. Package validation accepts all 19 skills and rejects Python files, bundled script directories, tests, hooks, and evaluation evidence in the library. Historical tests are labeled separately from current library behavior.

Two scoped source-skill trials exercised the simplified instructions. Setup explained that future-chat defaults cannot be saved and returned task wording for two reviewers with inherited settings. A Challenge trial spawned two independent reviewers, retained both completed verdicts, and found a seeded keyword-argument regression despite passing fixture tests. The fixture remained unchanged. The host accepted inherited reviewer settings without reporting exact model IDs; model diversity is not claimed.

Independent review found and corrected incomplete input hashing in the external evaluator and stale references to persistent Setup in personalization guidance. Detailed records and revision identifiers live in the [library split record](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/library-split.md) and its [evidence file](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/evidence/library-split-2026-10-07.json). The generic skill-creator validator could not run in the trial environment because PyYAML was absent; the repository-specific validator passed. Version 0.20.0 installation and authenticated Claude workflow checks remain pending.

## Automated package checks

[Package checks](../.github/workflows/checks.yml) runs on pull requests, pushes to `main`, and manual dispatch. It checks out the library and evaluator as siblings, pins evaluator revision `f3f0b76215b2d84d610ed764207556f757622417` and action revisions, grants read-only repository permissions, and retains the JSON result.

The pinned published evaluator passed its 70 checks in a local rehearsal. The newer local evaluator passed 80 checks. The pin deliberately remains on a remotely available revision until evaluator updates are published separately. The workflow has not yet run on GitHub; local execution does not establish hosted CI success. Installation and live model trials remain separate from CI.
