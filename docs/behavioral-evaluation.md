# Evaluate a workflow on a fresh task

Use the seven scenarios in [tests/behavioral/cases](../tests/behavioral/cases) to check workflow behavior against small, repeatable projects. They derive from the trial families recorded in [the project plan](plan.md). They are new fixtures, not recovered copies of the historical trials.

The [3 October 2026 trial results](behavioral-results.md) record observed outcomes and unresolved process gaps.

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
