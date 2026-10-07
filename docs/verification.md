# Verification

Package checks, Python tests, behavioral fixtures, detailed trial reports, and evidence now live in the separate local repository `../pancake-stack-evals`. That repository preserves the original Git history through `795dc890ee0b0acf24e743d82362c4a92e4202e1`. It has no remote. These sibling paths are maintainer checkout locations, not dependencies needed to use the skills.

## Run the checks

From a Pancake Stack checkout with the evaluation repository beside it:

```sh
python3 -B ../pancake-stack-evals/run_checks.py --source . --output /tmp/pancake-checks.json
```

The evaluator records both repository revisions, file hashes, including nonignored untracked files, dirty state, and whether checks changed either tree. Package validation covers JSON parsing, marketplace source resolution, skill metadata, and local documentation links. Historical preference and catalog tests use archived helpers in isolated temporary storage. They do not verify current runtime features.

The evaluation repository retains `docs/behavioral-results.md`, `docs/baseline-comparison.md`, `docs/installation-verification.md`, `docs/safeguards.md`, and `docs/evidence/`. Read those files from that checkout for the methods, results, and limitations. Public links can be added if that repository is published. Historical reports also remain accessible in [the library history before extraction](https://github.com/j4ckwinter/pancake-stack/tree/795dc890ee0b0acf24e743d82362c4a92e4202e1/docs).

## Evidence limits

The October 2026 baseline pilot found more consistent reproduction and independent review with Pancake. Both treatments passed their artifact checks, and Pancake used more time and tokens. A subsequent reviewer pilot detected its seeded defects but did not establish lower overhead. Neither trial establishes broad correctness benefits.

Earlier Codex installation and workflow trials passed on their recorded versions. Claude packaging and skill discovery passed, while authenticated Claude workflows remained unverified. Installation, visible picker behavior, applied model selection, and live workflow behavior remain separate from structural validation.

## Automation gap

The former in-repository test workflow has been removed because its tests moved. GitHub cannot access this local-only evaluation repository. Automatic pull-request validation is pending an authorized remote and access configuration. When available, CI should check out a pinned evaluator revision beside the exact library revision and run the command above. Until then, maintainers run the external checks before committing.
