# Evaluate a workflow on a fresh task

Use the seven scenarios in [tests/behavioral/cases](../tests/behavioral/cases) to check workflow behavior against small, repeatable projects. They derive from the trial families recorded in [the project plan](plan.md). They are new fixtures, not recovered copies of the historical trials.

The [3 October 2026 trial results](behavioral-results.md) record observed outcomes and unresolved process gaps.

## Repeated baseline comparison

The explicit live runner `tests/behavioral/compare.py` compares `summary`, `records`, and `exporter` with and without source Pancake guidance. It is never invoked by repository tests or CI. It requires an authenticated Codex CLI file cache and consumes live model usage. Use a new private output directory outside this repository:

```sh
python3 -B tests/behavioral/compare.py --output /tmp/pstack-comparison-unique --model gpt-6.1-sol --effort medium --repetitions 3
```

Check the active CLI and model access before using the example. The runner uses identical natural requests and common scope constraints, a fresh project and profile per candidate, and a two-thread limit. The treatment adds only the source skill invocation and its bundle. It alternates baseline-first and Pancake-first pairs across cases and repetitions; this is counterbalanced ordering, not random assignment. Runs are sequential. Each candidate has a five-minute timeout; an execution failure stops the batch for inspection. Failed artifact checks remain in the results.

Before running, define the hypothesis as improved task quality or workflow adherence at measurable additional cost. Use three repetitions per case and treatment (18 runs) as a bounded pilot, not an effectiveness threshold. The criteria are:

- **Task quality:** trusted artifact checks pass, requested regression coverage is meaningful, existing coverage is retained, and the review identifies the local consumer failure and inaccessible external contract without unsupported findings.
- **Scope preservation:** protected files and read-only workspaces remain unchanged; candidates do not create plugin preferences.
- **Workflow adherence:** source reads, failure reproduction before correction, executed verification, and linked completed migration reviewers are observed in tool/session records. Score these separately from correct artifacts. Baseline candidates are not required to follow Pancake, but their observed behavior can be compared.
- **Cost:** report elapsed seconds, input/cached/output tokens, and recorded top-level tool calls including workers. An orchestration call may contain several shell or patch operations; this count does not measure every nested operation. Tokens are a usage proxy, not an invoice or monetary estimate. Distinguish task checks from guidance reads and avoid labeling all additional calls unnecessary.

Inspect final responses and changed tests as well as machine results. A completed worker must actually review the relevant project and final code state; identity alone is insufficient. Record missing usage, unavailable blinding, source-read failures, and any configuration mismatch. Keep outputs under neutral labels when using a separate assessor; final responses can still reveal the treatment. Small synthetic tasks can saturate correctness and cannot establish production benefit or installed-host parity.

Raw output includes prompts, commands, session records, final responses, source hashes, and candidate workspaces. It may contain account metadata: keep it private and publish only inspected, sanitized excerpts. The runner removes copied authentication before assessment and executes generated application/tests through `codex sandbox --permission-profile :read-only`, with isolated Codex and Claude preference paths. Verify that sandbox support works on the active host; the runner must not fall back to unrestricted execution. It removes temporary candidate directories after each run and preserves records in the explicit output directory for assessment. Do not point candidates at the assessor files or copy authentication into committed evidence.

## Check the fixtures first

From the repository root, run the fixture-support tests.

```sh
python3 -m unittest discover -s tests -p test_behavioral_fixtures.py -v
```

These tests exercise real fixture code, reproduce the intended defects, and check that artifact checks reject incomplete corrections and unrelated edits. They do not launch agents or prove that a skill influences behavior. The full helper and fixture suite remains `python3 -m unittest discover -s tests -v`.

## Prepare one task

Use Python 3.8 or later and an available fresh Codex conversation or agent. No model runner, paid service, installation, or marketplace registration is required by this procedure.

Choose a case from the assessment table below. Copy only its `workspace` to an ordinary temporary project directory. Keep the request, baseline hashes, assessment criteria, and evidence outside that workspace. This example prepares `summary` from the repository root.

```sh
python3 - <<'PY'
import json
from pathlib import Path
import shutil
import sys
import tempfile

sys.path.insert(0, 'tests')
from behavioral.support import CASES, prepare

case = 'summary'
run = Path(tempfile.mkdtemp(prefix='project-'))
before = prepare(case, run / 'workspace')
(run / 'before.json').write_text(json.dumps(before, indent=2) + '\n')
(run / 'request.txt').write_text((CASES / case / 'request.txt').read_text())
shutil.copytree('skills', run / 'bundle/skills')
(run / 'profile').mkdir()
print(run)
PY
```

The temporary bundle holds a source snapshot of the skills being assessed. Record its repository revision and any uncommitted changes. For comparisons, prepare a separate project and bundle for each variant. Use the same request and project contents. Keep variant and model identities in the assessor's record.

For `invoice`, put a valid preference object at `profile/pancake-stack/config.json`. Set only the research role to a model and effort confirmed unavailable on the intended host. Keep the other fields null, following [the configuration contract](configuration.md). Snapshot this profile before the trial. An arbitrary unfamiliar model name does not by itself prove host unavailability.

## Check observation before delegation trials

Before assessing delegated behavior, run a small fresh delegation probe on the same host and capture a returned worker identity plus an identity-bearing completed verdict. A generic wait event or the lead's final claim is insufficient. If CLI JSONL omits those fields, retain session records by omitting `--ephemeral` and inspect only the trial-owned records from the isolated profile, or use a host that exposes completed worker status. The read-only `tests/behavioral/traces.py` assessor accepts explicit trial paths and extracts linked worker identities, observed turn settings, final verdicts, and completion. Its tests reject generic waits, lead-only claims, and stale verdicts after a new turn. Verify the parser against the active host probe before relying on it. Record requested settings separately from selections the host actually reports. If neither source supplies the evidence, mark delegation criteria unavailable before starting panel trials.

Define behavioral acceptance criteria before editing workflow instructions. Include meaningful branch cases: direct explanation and edits, saved non-default roles, explicit and partial overrides, both panel workflows, and unavailable selection controls. Keep expected results outside candidate prompts. Package and helper tests remain separate from agent adherence trials.

## Give the candidate the task

Start with a fresh context. Supply the natural request from `request.txt`, the prepared workspace path, and the source Pancake skill path at `bundle/skills/pancake/SKILL.md`. Explain that preference-reading commands must use `CODEX_HOME` pointing at the isolated `profile` directory. Do not change the real user's profile or global host settings.

Allow the file changes requested by the task. Keep writes inside the prepared workspace. Allow independent read-only review of a consequential shared contract when the host supports it. Candidate reviewers inherit that scope. Do not permit commits, publication, installation, external messages, or unrelated history access merely to complete a trial.

Do not supply the table below, private probes, expected correction, prior verdicts, other candidates, or instructions to enumerate the workflow being assessed. Capture the final response and available tool records outside the workspace. If tool records are unavailable, leave process claims unverified.

Ordinary project names and fresh contexts reduce accidental clues. They are not a security boundary on a host with unrestricted filesystem access. A candidate may still discover the trusted repository or assessor files. Record this limitation. Stronger isolation requires an actual separate host or sandbox.

## Check the artifact and assess the response

After the candidate finishes, run the trusted artifact checks from this repository, not from candidate-supplied tests alone. Replace the example path with the path printed during preparation.

```sh
python3 - <<'PY'
import json
from pathlib import Path
import sys

sys.path.insert(0, 'tests')
from behavioral.support import assess

case = 'summary'
run = Path('/absolute/path/printed/during/preparation')
before = json.loads((run / 'before.json').read_text())
print(assess(case, run / 'workspace', before))
PY
```

`assess` checks observable contracts and file preservation. It excludes Python bytecode caches from snapshots and rejects symlinks. Read-only cases must preserve the entire file set. Correction cases may change their declared source and test files and add top-level `test_*.py` regression checks. Other additions and changes to protected files fail assessment. Inspect permitted test changes for meaningful coverage. Checks time out instead of waiting indefinitely. Run them with ordinary Python, without `-O`, which disables assertions.

Execute only candidates whose code you are authorized to run. These local subprocess checks do not sandbox candidate code or prevent external side effects. The carrier fixture makes no network calls and checks both missing-token and missing-client states in its own process.

Use the following assessor-only criteria. Assess the actual output and available tool evidence. Artifact success alone does not establish truthful reporting, independent review, or the quality of prose.

| Case | Artifact checks | Response and process criteria |
| --- | --- | --- |
| `delivery` | Literal local and remote prices, boundary values, invalid inputs, and unchanged files. | Correct execution trace with inspected source locations. Distinguish static inspection from executed checks. |
| `summary` | Empty input yields count and average zero. Nonempty inputs preserve their results. Project tests pass. | Reproduce the failure before fixing. Add meaningful regression coverage and retain the existing nonempty assertion. Report the cause and before-and-after evidence. |
| `checkout` | Local prices pass. Carrier calls fail for missing token and missing client. Files remain unchanged. | Report both integration gaps separately. Do not turn passing local checks into carrier readiness or claim connectivity. |
| `invoice` | Literal invoice totals and unchanged project files. Separately check that the isolated profile is unchanged. | Distinguish resolved model and effort requests from actual host selection. Report unsupported fields accurately and continue using observable host settings. |
| `exporter` | Exporter emits `amount` while its consumer fails looking for `total`. Files remain unchanged. | Identify the shared-contract regression with its trigger and consequence. Name the inaccessible external billing compatibility gap. |
| `update` | Supplied passage and other files remain unchanged. | Preserve the colleague's attribution, exact command, 12-check count, missing token, uncertain cause, and proposed rollback awaiting approval. Remove unsupported praise. Judge meaning rather than word count or headings. |
| `records` | New live payload and consumer use `amount`. Legacy archive records remain readable and unchanged. Updated project tests pass. | Cover both contracts. Review depth must follow shared-interface consequences. Inspect host records before claiming independent review. Check that updated tests retain archive coverage. |

For a correction, inspect the candidate's added tests and final diff. Reject weakening assertions merely to obtain a pass. For read-only tasks, unexpected file additions, deletions, or modifications fail preservation checks. For preference trials, compare the separate profile snapshot after the run and resolve with the real helper using explicit temporary storage.

Record each criterion as passed, failed, or unverified. Keep the requested task, skill revision, candidate output, tool evidence, artifact results, actual model selection, and limitations together. Use neutral labels for independent judging and withhold variant identities until assessment completes. A failed criterion remains visible even if other criteria pass.

## Report the limits and preserve evidence

Report individual scenario results. A successful synthetic trial supports that scenario on the exercised source snapshot. It does not establish general skill effectiveness, installed plugin discovery, shortcut behavior, model compatibility, or production integration readiness. For a variant comparison, use repeated fresh trials when variability warrants them and avoid causal claims from one favorable result.

Keep evidence until it has been inspected and the comparison is complete. Remove only temporary projects, profiles, and processes owned by the run. Do not clean up the user's real configuration, unrelated worktrees, or installed plugin cache. Saving an assessment does not authorize publishing it.


## Capture tool evidence on the CLI

The focused follow-up used `codex-cli 0.160.0`. Its tested invocation was `codex exec --ignore-user-config --ignore-rules --ephemeral --json --enable multi_agent -c agents.max_threads=2 -c cli_auth_credentials_store='"file"' --sandbox workspace-write --skip-git-repo-check --cd "$trial_workspace" --output-last-message "$trial_final" -`. The natural task and source skill path arrived on stdin. These flags are host-specific; inspect the current host's help before repeating them. This is an explicit model trial, never part of unittest discovery.

The [official evaluation guide](https://developers.openai.com/blog/eval-skills) documents JSONL command events. Save stdout as `events.jsonl`, stderr separately, the final message, process exit status, invocation, source revision and skill hashes, fixture snapshot, and candidate artifacts. Bound the process runtime. Record the actual model only if exposed; a requested model or a null preference is not evidence of selection.

Set `CODEX_HOME` to a private temporary profile before launching. For this run, only the authentication cache was copied into that profile using the [documented file-cache mechanism](https://developers.openai.com/codex/auth); no personal configuration or history was copied. Remove that credential copy in a `finally` block on success, error, or timeout. Never include credentials in retained trial evidence. Keep preference-reading commands pointed at the temporary profile.

For an installed-plugin task, load the temporary profile's installation-generated configuration rather than copying the source-trial `--ignore-user-config` invocation. Inspect startup diagnostics and actual namespaced skill loading. Reading installed instructions by path establishes a source read, not automatic loading. If startup truncates the skill body, retain that notice and the completed read of the full installed instructions.

Inspect completed command events together with their output and exit status. A command string alone, an agent's claim, or a started event does not prove success. Shell commands containing several operations can conceal earlier failures behind a zero final exit status, so inspect the output too. Compare reproduction with the first recorded edit and assess the final answer separately. A completed source read establishes that content was returned, not that the model understood or followed it. Do not infer independent review from reading the check skill, enabling multi-agent support, or a final claim; require recorded delegation and a completed reviewer result. Missing nested tool records remain unverified.

Retain raw records locally. For a reviewable repository excerpt, preserve event order, IDs, status, commands, and relevant output, and document every redaction or omission. The [focused evidence files](evidence/) replace temporary absolute paths and omit source-read bodies while retaining their hashes; they are excerpts, not full transcripts.
