# Accepted safeguards

This record tracks accepted corrections, their owning layer, and evidence. “Verified” means the named check passed on the recorded scope. Guidance and observation are not enforcement of an agent's judgment.

| Observed failure | Owner | Enforcement or observation | Regression check | Status |
| --- | --- | --- | --- | --- |
| Package relationships and skill references relied on manual inspection. | `tests/package_validation.py` | Read-only repository-profile validation runs through ordinary unittest discovery. | `tests/test_package_validation.py` accepts valid changes and rejects malformed JSON, mismatched package identity, missing skills, unsupported headers, and missing or escaping links. It checks byte-for-byte preservation. | Verified for this repository profile; official schema compliance and installation remain separate. |
| Correction assessment accepted unrelated new files. | `tests/behavioral/support.py` | Declared mutable paths and top-level regression-file additions constrain artifact acceptance. | `test_correction_additions_are_limited_to_regression_files` accepts a regression check and rejects an unrelated addition. | Verified for artifact assessment; candidate execution itself is not sandboxed by this check. |
| Shared-contract migrations completed without established independent review. | Pancake implementation guidance and behavioral assessment | Judgment guidance plus inspection of actual host records. | The `records` fixture requires both live and archive contracts; tool records must establish any claimed delegation. | Unresolved workflow adherence. Artifact acceptance does not establish independent review. |
| Empty-input fixes omitted failing-before evidence in the final report. | Fix/verification guidance and behavioral assessment | Separate tool ordering from final-answer grading. | The `summary` fixture and recorded command failure before the first edit. | Reproduction observed in the focused trial; final reporting still failed. |

The [trial results](behavioral-results.md) identify the evidence and limits. Use [the evaluation procedure](behavioral-evaluation.md) for repeat runs. Update a row only when new evidence changes its status; avoid copying the underlying skill instructions into this record.
