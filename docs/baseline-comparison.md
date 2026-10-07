# Baseline comparison, 7 October 2026

Pancake changed observed workflow behavior in this pilot, but did not improve the requested artifact outcomes: both treatments passed all nine tasks. Pancake reproduced the local defect before fixing it in all three runs and completed independent migration review in all three runs; the baseline did neither. These steps took more time and tokens. One Pancake migration also introduced an unrequested keyword-argument compatibility risk that its independent reviewer missed.

## Method

The [retained evidence](evidence/baseline-comparison-2026-10-07.json) covers three repetitions each of a local fix (`summary`), shared-contract migration (`records`), and read-only review (`exporter`), with and without source Pancake guidance. Each of the 18 sequential runs used a fresh workspace and private Codex profile, the same natural request and scope constraints, and a five-minute timeout. Pair order alternated across cases and repetitions. All runs finished without timeout or retry.

Codex CLI 0.160.0 ran on macOS. All 18 candidates and three child reviewers reported `gpt-6.1-sol` with medium effort. The source snapshot was `7d99d0e`; skill and fixture hashes are retained. The baseline had no Pancake invocation. The treatment added its source skill path and bundle, not an installed plugin. This compares against a clean CLI profile, not the user's configured daily environment.

Trusted artifact checks ran in a read-only sandbox. A separate assessor inspected shuffled, neutrally labeled before/after workspaces and final answers, without treatment or candidate model identities. Answers can reveal workflow, so this was not fully blinded. The coordinator inspected execution records unblinded to establish process claims. The [procedure and explicit runner](behavioral-evaluation.md#repeated-baseline-comparison) support another comparison; live trials remain outside CI.

## Outcomes and usage

Each row contains three runs. Time and tokens show median (minimum–maximum). Token totals sum input and output across the parent and workers; cached input is already included. These are usage counts, not monetary costs. Shell commands count completed command actions, including worker actions; one command may contain several checks.

| Task | Treatment | Artifact passes | Seconds | Total tokens | Median shell commands |
| --- | --- | --- | --- | --- | --- |
| Local fix | Baseline | 3/3 | 32.2 (24.6–34.8) | 76,409 (61,472–76,554) | 4 |
| Local fix | Pancake | 3/3 | 45.9 (43.0–50.6) | 121,229 (100,894–122,167) | 5 |
| Migration | Baseline | 3/3 | 32.9 (29.3–33.3) | 77,868 (77,427–77,948) | 4 |
| Migration | Pancake | 3/3 | 76.4 (74.1–80.5) | 301,893 (251,985–304,997) | 14 |
| Review | Baseline | 3/3 | 26.9 (24.4–27.7) | 77,406 (77,112–77,568) | 4 |
| Review | Pancake | 3/3 | 34.2 (32.3–34.9) | 88,415 (70,179–89,150) | 6 |

All fixes retained existing nonempty coverage and added meaningful empty-input regression coverage. All migrations verified live `amount` payloads and preserved archived `total` records. All six reviews identified and reproduced the local consumer failure, disclosed the inaccessible external billing contract, and left files unchanged. The separate assessor found no false or missed review findings. Protected files and isolated preferences remained unchanged across all 18 runs.

Process evidence differs from artifact success:

- **Reproduction before the fix:** Pancake 3/3; baseline 0/3. Each Pancake run executed a new regression that failed before the production edit and passed afterward. Baseline runs fixed the issue and then verified it. Baseline was not instructed to follow Pancake's process.
- **Completed independent migration review:** Pancake 3/3; baseline 0/3. Child identities, matching workspaces, their own verdicts, inspected source, and executed tests establish completion. All three reviewers returned no findings.
- **Additional compatibility risk:** in `run-03`, Pancake changed `create_invoice(total)` to `create_invoice(amount)` as well as renaming the payload key. A post-hoc sandbox probe confirmed that `create_invoice(total=19.5)` succeeds on the original and the other five migrations, but raises `TypeError` on this candidate. No supplied caller uses that keyword, so this is separate from the requested live/archive success. The independent review did not catch it.

Across nine tasks per treatment, baseline candidate time totaled 266.0 seconds and Pancake 472.0 seconds. Total recorded tokens were 679,764 and 1,450,909 respectively. Timing includes startup and reviewer waits, but excludes preparation and trusted assessment. Input, cached-input, output, top-level tool calls, and shell actions remain separate in the evidence. Guidance reads, reproduction, and reviewer work explain additional actions; this study does not classify every extra call as unnecessary.

## Interpretation and limits

The repeated observations support a process benefit on these tasks, with measurable overhead. They do not demonstrate better code correctness or better review findings. These tiny fixtures saturate the artifact score, and the keyword issue shows that passing the probes and adding a reviewer do not establish complete compatibility.

Keep this baseline before testing instruction consolidation. A useful next comparison would preserve reproduction and review behavior while reducing guidance-reading cost, and use harder tasks with explicit API compatibility criteria. Do not shorten instructions merely because this pilot used more tokens.

There are only three observations per task and treatment, one candidate model, one host, no random assignment, and no installed-plugin or Claude coverage. Host-reported settings do not expose internal model behavior; caching and service latency can affect cost and timing. Source skills, prompts, settings, and fixtures stayed fixed. The usage collector was corrected during the batch to exclude inherited pre-worker events and count orchestration/custom calls; every run was recollected from retained raw sessions using the final collector. Copied authentication and temporary candidate directories were removed. Raw records remain private; committed excerpts omit account metadata, system prompts, and long guidance outputs while retaining hashes.
