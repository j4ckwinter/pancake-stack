# Workflow trials on 3 October 2026

These trials used the repository-source skills based on `602da98` with the changes prepared for `0.16.4`. Each task ran in a fresh agent context against its own temporary project and preference profile. The agents inherited the parent model. This was independent task execution with no provider diversity. The coordinating assessor knew the case and source variant, so assessment was not blinded.

The fixtures are derived from the seven historical trial families. They do not reproduce the original historical environments. The candidate tasks received natural requests and source skill paths, without private acceptance probes or expected corrections. All filesystem access remained unrestricted. The setup reduces accidental clues but cannot establish that assessor files were inaccessible.

## Observed outcomes

| Task | Checked outcome | Remaining evidence limit |
| --- | --- | --- |
| Delivery explanation | Correct rates, threshold, rejected inputs, and source locations. Trusted artifact checks passed and files were unchanged. | The candidate correctly described its work as static inspection. Parent execution proves fixture behavior, not candidate execution. |
| Empty-input fix | The final command returned count and average zero for empty input, preserved nonempty results, and passed project tests. The original nonempty assertion survived alongside an added regression test. | The final reply named the divide-by-zero cause and passing checks but did not include a failing-before result. Parent fixture tests reproduce the baseline failure; that does not establish that the candidate reproduced it before editing. |
| Carrier verification | The response reported missing token and missing client separately and declined integration readiness. Local rates and both failure states passed trusted artifact checks. Files were unchanged. | No live carrier service, credentials, or production policy were exercised. |
| Preference fallback | The response distinguished unavailable requested model and effort from retained host settings. Invoice checks passed. Project and isolated profile were unchanged. | Exact host model and effort were not exposed. Fixture resolution does not prove model-selection behavior. |
| Exporter review | The response identified the renamed field breaking the consumer, despite a passing exporter test. Trusted checks reproduced that mismatch. Files were unchanged. | External billing compatibility remained inaccessible. |
| Prose rewrite | The reply preserved the colleague's attribution, exact command and count, missing token, uncertain cause, and proposed rollback awaiting approval. It removed unsupported praise. Source files were unchanged. | Meaning was assessed directly by the coordinator. Artifact checks alone cannot judge prose quality. |
| Live-record migration | New payloads and consumer used `amount`; archived `total` records, archive reader, and unrelated note were preserved. Trusted checks and updated project tests passed. | The candidate reported direct review despite independent review being available. No completed independent review was established. |

The migration result prompted a narrower completion requirement in [implementation guidance](../skills/pancake/references/implementation.md). A fresh follow-up used that revised source and passed both data contracts, but again reported direct review. The wording change therefore has no demonstrated adherence improvement. This process gap remains an observable failure criterion for future trials. Adding further instructions without evidence about routing or execution would not establish a fix.

The candidate outputs and parent artifact checks support the observations above. Full candidate tool transcripts were not audited, so workflow reads, reproduction ordering, and other process claims remain unverified unless independently established. Host completion status and final replies establish that the listed candidate tasks completed; they do not prove every claimed tool action.

## Measurement-validity trial

A separate fresh task assessed a benchmark for summing the squares of 100000 integer rows. The apparently fast implementation returned an unconsumed generator. The candidate rejected adopting it from the original timing and measured complete eager and consumed-lazy operations instead.

Its retained measurement artifact contains 40 alternating pairs after five warmup pairs on Python 3.9.6. It records 80 successful measured sums and zero failures, with input construction outside timing. Median durations were about 2.379 ms and 2.387 ms. The corresponding ranges were 2.245 to 2.496 ms and 2.252 to 2.545 ms. The observed difference was smaller than the variation, so the response made no speedup claim.

Parent inspection confirmed the sample counts and independently called both implementations. The eager result and consumed generator both produced `333328333350000`. The raw measurement artifact supports the reported local observations. It does not prove that the guidance caused the response, identify a production bottleneck, or establish end-to-end performance.

## Repository verification

The fixture-support tests exercise baseline failures, literal outputs, incomplete corrections, protected-file mutations, read-only additions and deletions, isolated preference resolution, symlink rejection, and correction-file scope. Independent review found that the first assessor accepted arbitrary new files during correction tasks. The corrected assessor limits additions to top-level regression-test files, with a test that accepts a real regression check and rejects an unrelated addition.

An independent read-only reviewer reran all eleven focused checks and found no remaining actionable issues in that correction or the revised completion wording. This review covers the repository change. It does not supply the independent review missing from the migration candidates' own workflows.

Use the [evaluation procedure](behavioral-evaluation.md) to repeat these scenarios. Installed discovery, host shortcuts, global configuration, and marketplace registration remain separate checks documented in [the installation record](installation-verification.md).


## Focused tool-record follow-up

Two additional trials used the unchanged `437490f` skill snapshot, version `0.16.4`, on `codex-cli 0.160.0`. Each used a fresh temporary workspace and profile, ignored user configuration and rules, and enabled the CLI's multi-agent feature with a two-thread limit. The prompt explicitly permitted independent read-only review. The exact model and reasoning effort were not exposed in the retained events or stderr; null resolved preferences do not identify either. Feature configuration and prompt wording alone do not prove the candidate's available tool inventory. The coordinator inspected tool records and was not blinded. No guidance variant or causal comparison was tested.

Both processes exited zero and both trusted artifact assessments passed. The [summary evidence](evidence/summary-2026-10-03.json) and [migration evidence](evidence/records-2026-10-03.json) retain event order, commands, outputs, final replies, invocation, source hashes, and final project files. Temporary paths are replaced with `$TRIAL_ROOT`; returned skill bodies are replaced with their paths and hashes. Output hashes and raw JSONL hashes refer to the original local records. The raw files remain in the run's local temporary storage. No credentials are retained in either profile or repository evidence.

| Criterion | Tool evidence | Assessment |
| --- | --- | --- |
| Summary source reads | Completed `item_1`, `item_3`, and `item_6` returned Pancake, implementation, values, sift, check, and verify guidance. | Reads observed; comprehension and adherence cannot be inferred. |
| Summary reproduction order | `item_6` exited 1 with `ZeroDivisionError`, before the first recorded edit, `item_8`. `item_9` subsequently passed two tests and both CLI inputs. | Failing-before and passing-after behavior observed. |
| Summary final report | Final `item_10` names the correction and passing checks but omits the prior failure and cause. | Reporting criterion failed despite correct artifacts and observed reproduction. |
| Migration source reads | Completed `item_1`, `item_2`, and `item_3` returned implementation and review guidance alongside the live and archive code. | Reads observed; this run does not support missing guidance reads as the explanation. |
| Migration contracts | `item_5` edits producer, live consumer, and tests; `item_6` passes live and archive tests. Trusted assessment separately confirms both contracts and protected files. | Artifact criterion passed. |
| Migration review | Final `item_7` says affected callers and contracts were reviewed. The trace has no delegation or completed reviewer event. | Independent review remains unverified; the required workflow criterion is not established. Reading the check skill is not independent review. |

Shell batches deserve separate inspection: summary `item_5` has a zero final exit status despite a `git status` failure in a workspace without Git. That output does not establish a successful Git inspection. The command records do establish that the requested source content was returned. Neither trial demonstrates a general adherence improvement, and no stronger wording was added to implementation guidance on the basis of these runs.

The [accepted safeguards](safeguards.md) distinguish verified package validation and artifact boundaries from these unresolved workflow requirements.
