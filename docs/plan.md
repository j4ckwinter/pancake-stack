# Project plan

## Current state

Version 0.20.0 contains 19 shared workflows for Codex and Claude Code. Shipping guidance follows repository commit conventions and falls back to Conventional Commits when none is documented.

Tests, fixtures, detailed reports, and evidence have moved to the separate local `pancake-stack-evals` repository with their Git history preserved. The evaluator accepts an explicit library checkout and records both revisions. See [verification](verification.md) for the command, historical evidence, and automation gap.

The library contains no bundled Python scripts or tests. Setup helps phrase choices for the current task without saving a profile. Delegates inherit host settings unless the task explicitly overrides them. Legacy preference files remain untouched and are no longer read. Independent-review requirements remain in place.

## Next
- Verify the simplified workflows with fresh agent trials and independent review.
- Restore automatic pull-request validation once an evaluation-repository remote and access are authorized.
- Run authenticated Claude workflows and verify visible picker behavior on supported hosts.
- Exercise representative repository tasks beyond the synthetic fixtures.

Historical plans and dated verification records are retained in the evaluation repository. License selection, publication, and plugin installation require separate authorization.
