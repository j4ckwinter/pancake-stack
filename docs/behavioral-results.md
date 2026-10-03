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
