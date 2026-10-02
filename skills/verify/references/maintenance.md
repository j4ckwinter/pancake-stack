# Maintain an existing verification recipe

Use this guidance when the user requests an audit or update of an existing project verification guide, skill, or its owned harness. Ordinary verification does not authorize saved documentation edits. Locate the named target or a clearly relevant existing recipe. If several plausible targets remain, ask which one. If none exists, report that and propose creation rather than inventing a maintenance target.

Establish the requested coverage and edit scope before running checks. For an audit, inspect and report without editing. For an authorized update, change only the recipe and its owned harness within that scope. Product repairs require separate authorization. Reuse the existing layout; a feature map, extra scripts, and one agent per feature are not prerequisites.

Compare documented prerequisites, commands, inputs, expected outcomes, and cleanup with current source and repository instructions. Follow the specific behaviors the recipe claims to cover. Inspect a feature index if one exists, including missing or duplicated references. Identify omitted behavior only from a concrete relevant implementation or contract. Record supported drift findings, not speculative completeness claims.

Exercise the agreed paths through their actual interface using the recipe's isolation and launch guidance. Source inspection alone does not establish that the recipe works. Group compatible checks where useful, preserving independent case outcomes. Check instance readiness before driving it and after surprising failures; return to a known state or restart only an instance owned by this run when needed. Preserve evidence outside disposable state and confirm it survives cleanup. Remove only processes and scratch state created by the run.

Classify discrepancies before changing instructions.

- Recipe drift means the instructions or harness no longer reach supported behavior. Confirm the current contract, correct within authorized scope, and rerun affected steps.
- Product regression means the implementation violates the intended contract. Preserve the expectation and report the failure; do not rewrite assertions or documentation to accept it.
- Environment limitation means a prerequisite or capability prevents the check. Name the attempted path and missing prerequisite. The behavior remains unverified, even if that limitation is expected.
- Unclear intent means source behavior and documented expectations disagree without enough evidence to identify the intended contract. Report the discrepancy and seek the missing decision rather than guessing.

After any harness or command correction, execute the corrected path and relevant cleanup before calling it verified. Recheck prior evidence if the correction changes its assumptions. Leave unexecuted instructions explicitly unverified. Do not install dependencies, alter global configuration, or use production services merely to make the maintenance pass complete.

Report the target and revision or state inspected, paths exercised, observed outcomes, confirmed corrections, product findings, and unverified paths. Distinguish source-reviewed coverage from executed coverage. A partially completed audit is not a clean verdict. Saved edits do not authorize commits, PR creation, or publication.
