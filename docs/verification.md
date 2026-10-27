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

## Version 0.21.17

The implementation sequence now puts needed CI, linting, test infrastructure, and shared types before dependent feature work. It preserves existing conventions and keeps setup proportional to the task. This adds one sequencing paragraph without a new skill or application setup policy.

## Version 0.21.16

Fix now places its existing distinguishing-observation instruction in initial diagnosis, conditional on ambiguity. Short goal-first prompts, mid-run corrections, and a same-chat catch-up example were added to the recipes. All 19 skills remain.

Ten natural repair trials exercised Fix, TDD, and Pancake with implementation workers permitted but not requested. All passed the bounded artifact and scope checks. The proposed parallel-work links increased reference reading in the changed importer runs without changing delegation or assessed outcomes, so they were rejected. These compact fixtures do not establish which larger repairs benefit from delegation.

Four diagnosis trials preserved the quote-service and small-control outcomes in both variants. Independent assessment confirmed causal evidence before production edits, real failing regressions, and completed quote-service review. The instruction relocation is a sequencing clarification, not a measured diagnostic improvement. The recipe additions received documentation review, not behavioral trials.

The published evaluator records [natural repair routing](https://github.com/j4ckwinter/pancake-stack-evals/blob/563502ee4c6caa43504446a6d13bdd450835d521/docs/natural-repair-routing.md) and [initial diagnosis](https://github.com/j4ckwinter/pancake-stack-evals/blob/563502ee4c6caa43504446a6d13bdd450835d521/docs/initial-diagnosis.md), including exact inputs, normalized outcomes, independent assessments, and limitations. Local package and evaluator validation completed 197 tests with one opt-in sandbox smoke skipped. These single observations per case and arm do not establish general superiority or installed-host behavior. Raw records remain private. Claude workflows and plugin installation were excluded.

## Version 0.21.15

This release expands external evaluation coverage and pins the published evaluator. The 19 shared workflows remain unchanged. Fourteen source-guidance trials cover delegated implementation, representative-unit pilots, fresh-state verification recipes, and returned worker artifacts.

Pancake and a pinned Codex adaptation of upstream pstack 0.15.32 both completed substantive delegated importer work and passed the bounded artifact checks. Both small controls stayed direct. The pilot paragraph did not produce a pilot before broad assignment in either migration run. Both recipe variants worked from empty and existing state, and both reconciliation variants preserved newer contracts while accepting compatible returned work. The three proposed wording additions were rejected; their patches and decisions remain in the evaluator.

The recipe oracle initially reused an evidence filename across independent scenarios. Both recipes correctly refused the overwrite. A corrected fixture replayed the saved artifacts successfully without rerunning models; the original failures and correction remain recorded. Stand-in setup and live worker interruption were not exercised. The returned-artifact comparison explicitly requested the parallel-work reference and does not test automatic discovery.

The [coordination evidence](https://github.com/j4ckwinter/pancake-stack-evals/blob/0159450d2c8f316185264506816292632d5decb3/docs/coordination-gaps.md) records exact inputs, artifacts, independent assessments, and limitations. These are single observations per task and arm, not evidence of general superiority or speed. Local package and evaluator checks ran 194 tests, with 193 passing and the opt-in sandbox smoke skipped; that smoke passed separately. Source-skill trials do not establish installed-host behavior. Claude workflows and plugin installation remain excluded.

## Version 0.21.14

The implementation sequence is shorter and ordered by action. Four source-skill runs across two task pairs preserved the small-refactor and compatibility outcomes, including baseline checks and independent consequential review. Complete returned guidance decreased in both pairs. These observations establish bounded behavior preservation and reading reductions, not general speed or quality gains.

Design now defaults to independent candidates and a separate judge when a consequential ownership, interface, persistence, or concurrency choice remains unresolved and materially different viable approaches remain. Established patterns, hard constraints, small changes, and explicit delegation limits keep work direct. In four design runs across two task pairs, the ambiguous task exercised the new default and the small-interface controls stayed direct. Both variants met the semantic criteria. The judge refined the candidate's contracts, at additional time and guidance cost; this is not evidence of general superiority.

A conditional cookoff extraction was tested and rejected. Both ordinary investigation and explicit comparison completed, but reading volume varied by task. The ordinary path did not show lower total guidance reading. The candidate patch and decision remain in the evaluator rather than adding another library reference.

Eight full-repository review trials compared the accepted Pancake source with a pinned Codex adaptation of Poteto. Both detected the two seeded defects and cleared the two clean controls. Independent assessment found no false actionable findings. The shared read-only, no-delegation scope does not test orchestration strengths or establish general review superiority.

The [execution-path evidence](https://github.com/j4ckwinter/pancake-stack-evals/blob/910c9f9955c2cfb1c44266ae414fd7776c2a9cb2/docs/execution-paths.md) records the source identities, trial artifacts, independent assessments, rejected candidate, and limitations. Timings are descriptive because machine load was not controlled and some package checks overlapped runs. Worker briefing content was unavailable in encrypted records. Source-skill trials do not establish installed-host behavior, and Claude workflows were excluded.

## Version 0.21.13

Delegation coordination now has one owner, reducing repeated guidance without adding skills. Pancake, Fix, and TDD load change classification before editing. Changes to agent instructions or release configuration that alter authorization, delegation, or verification behavior require independent review; wording-only edits retain direct review.

The [reading-path comparison](https://github.com/j4ckwinter/pancake-stack-evals/blob/b4f9dba8fd86d0b680e06479ebc84801c0935716/docs/reading-paths.md) recorded 149 fewer returned guidance words in each selected task pair with preserved outcomes. This measures complete returned Markdown, not tokens or general efficiency. [Sample-retention coverage](https://github.com/j4ckwinter/pancake-stack-evals/blob/b4f9dba8fd86d0b680e06479ebc84801c0935716/docs/sample-retention.md) preserved two batches of 80 observations and rejected an attempted overwrite. The recorder and tests live only in the evaluator.

Two [PR-maintenance tasks](https://github.com/j4ckwinter/pancake-stack-evals/blob/b4f9dba8fd86d0b680e06479ebc84801c0935716/docs/pr-maintenance-execution.md) executed a local forge adapter and correctly distinguished stale-head failures from the clean control. [Instruction-classification trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/b4f9dba8fd86d0b680e06479ebc84801c0935716/docs/instruction-classification.md) found that the baseline edited the shared procedure correctly but skipped independent review. The final candidate completed review for the behavioral change through Pancake and Fix, retained direct review for a title edit, and preserved test-first behavior and independent review through TDD. An earlier candidate's review completion remains unproven in its retained records.

All 179 local package and evaluator tests passed with unchanged inputs. Independent source and evaluator reviews completed. CI pins the published evaluator from [PR #9](https://github.com/j4ckwinter/pancake-stack-evals/pull/9). The [decision trail](https://github.com/j4ckwinter/pancake-stack-evals/blob/b4f9dba8fd86d0b680e06479ebc84801c0935716/docs/workflow-gap-decisions.md) records exclusions, adaptive follow-up, and limits. These are bounded source-skill observations, not broad efficacy or installed-host evidence. Raw sessions remain private. Claude workflows and plugin installation were not exercised.

## Version 0.21.12

Pancake now loads performance, prototype, and skill-evaluation detail through conditional references. Shared experiment framing, baseline, decision, and cleanup rules stay together. Every branch instruction is preserved. All 19 skills and their descriptions remain unchanged. The contributor check command now explicitly invokes Python.

The [six extraction trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/68d2b7afe0780d4ebc294cf598b4836cfb385a00/docs/experiment-references.md) passed outcome and protected-file checks in both variants. Complete returned guidance fell from 2,893 to 2,610 words for performance and from 2,893 to 2,378 for prototypes. Skill evaluation also read less guidance, but most of that difference came from incidental Check/Verify reads. These observations support this bounded split, not token savings, faster execution, or general efficacy.

[Sixteen natural-task routing trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/68d2b7afe0780d4ebc294cf598b4836cfb385a00/docs/metadata-routing.md) completed with and without source metadata. The catalog arm used applicable guidance in all eight tasks. This is source-catalog evidence, not native discovery or picker verification. [Eight unrelated acceptance-path trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/68d2b7afe0780d4ebc294cf598b4836cfb385a00/docs/acceptance-paths.md) detected both defect domains and cleared their controls in both guidance variants, showing no reason to add wording.

All 154 local package and evaluator checks passed with unchanged inputs. Independent source, evaluator, and evidence reviews completed. CI pins the published evaluator from [PR #8](https://github.com/j4ckwinter/pancake-stack-evals/pull/8). Its [decision trail](https://github.com/j4ckwinter/pancake-stack-evals/blob/68d2b7afe0780d4ebc294cf598b4836cfb385a00/docs/measured-gap-decisions.md) records the correction from incomplete CLI events to raw session call/output evidence, partial blinding, single-observation limits, and sample-retention limits. No subjects were rerun to correct the assessment packets. Raw records remain private. Claude workflows and plugin installation were not exercised.

## Version 0.21.11

Check now asks reviewers to construct a representative valid operation and exercise the complete changed acceptance path, or explicitly report a concrete unexecuted trace. Fix, TDD, and implementation share consequential preparation and final-review rules in [change review](../skills/pancake/references/change-review.md). Small local changes retain direct review. Pancake's picker description and four recipes expose existing workflows; all 19 skills remain.

The [acceptance-path trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/contract-execution-followup.md) detected the selected historical defect with the candidate instruction in the paired run and a separate adaptive repeat. The baseline missed it. Both controls retain supported residual findings, so these results do not establish clean-control specificity or general superiority.

[Direct-entrypoint trials](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/direct-entrypoints.md) found no missing Fix or TDD rule. [Four extraction trials and a local smoke](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/shared-change-review.md) preserved observed repair, test-first, and review behavior. Guidance volume increased; the extraction is retained for shared ownership, not context savings. The small [TypeScript extraction](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/boundary-extraction-decision.md) was rejected because its 23-word reduction did not justify another navigation step.

[Six source-catalog probes](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/source-catalog-routing.md) selected and read the expected guidance. One also read an unnecessary alternative. These probes do not demonstrate automatic discovery, picker behavior, or an improvement caused by the documentation change.

All 136 final local package and evaluator checks passed with both inputs unchanged. Independent source and evaluator reviews completed. CI pins the published evaluator from [PR #7](https://github.com/j4ckwinter/pancake-stack-evals/pull/7). Public records retain selected hashes and aggregate judgments; [publication provenance](https://github.com/j4ckwinter/pancake-stack-evals/blob/0c25c1c943c7ec148c24daf47e1fdd74026d38ef/docs/publication-provenance.md) maps rewritten local evidence commits while preserving actual trial identities. Raw records remain private. Authenticated Claude workflow verification remains deferred.

## Version 0.21.10

Ordinary refactors now capture affected behavior with an existing focused check before restructuring and repeat it afterward. Check moves detailed comment and suppression guidance into a conditional reference, reducing its entrypoint from 662 to 479 words. The existing 19 skills and Design decomposition remain intact.

The [workflow report](https://github.com/j4ckwinter/pancake-stack-evals/blob/afb9203cf33dec23f200e4985f0b39b933522a4e/docs/workflow-gap-results.md) records two refactor pairs and a separate guarded smoke pair. Revised runs checked behavior before and after editing; original runs checked only afterward. Twelve review runs found all presented defects and reported no actionable findings on clean controls in both variants. An ordinary-fix pair passed in both variants. Reading observations did not establish consistent total-context savings, so no further extraction was accepted.

The [historical follow-up](https://github.com/j4ckwinter/pancake-stack-evals/blob/afb9203cf33dec23f200e4985f0b39b933522a4e/docs/historical-review-followup.md) still missed the selected defect. An exploratory wording change did not improve detection and was rejected. The release pins the published evaluator from [PR #6](https://github.com/j4ckwinter/pancake-stack-evals/pull/6), with 133 passing local checks. Independent code and evidence reviews passed. These are narrow source-guidance trials on one host and model, not new installation checks or general quality claims. Claude authenticated workflow verification remains deferred.

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
