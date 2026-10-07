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

## Version 0.20.0 source verification

The external suite has 70 checks, including historical helper tests. Package validation accepts all 19 skills and rejects Python files, bundled script directories, tests, hooks, and evaluation evidence in the library. Historical tests are labeled separately from current library behavior.

Two scoped source-skill trials exercised the simplified instructions. Setup explained that future-chat defaults cannot be saved and returned task wording for two reviewers with inherited settings. A Challenge trial spawned two independent reviewers, retained both completed verdicts, and found a seeded keyword-argument regression despite passing fixture tests. The fixture remained unchanged. The host accepted inherited reviewer settings without reporting exact model IDs; model diversity is not claimed.

Independent review found and corrected incomplete input hashing in the external evaluator and stale references to persistent Setup in personalization guidance. Detailed records and revision identifiers live in the [library split record](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/library-split.md) and its [evidence file](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/evidence/library-split-2026-10-07.json). The generic skill-creator validator could not run in the trial environment because PyYAML was absent; the repository-specific validator passed. Version 0.20.0 installation and authenticated Claude workflow checks remain pending.

## Automation gap

The former in-repository test workflow has been removed because its tests moved. The evaluator is now hosted on GitHub, but automatic pull-request validation remains deferred. When configured, CI should check out a pinned evaluator revision beside the exact library revision and run the command above. Until then, maintainers run the external checks before committing.
