---
name: fix
description: Diagnose and fix a reported software defect with focused verification. Use for broken behavior, errors, and regression fixes.
---

# Fix a defect

Read [core values](../pancake/references/values.md) and applicable repository instructions.

Establish expected and actual behavior from the report and implementation. Reproduce the failure on the relevant surface when feasible. If reproduction is unavailable, state the missing evidence and proceed only as far as the available evidence supports.

Trace the symptom through its inputs, state changes, and callers. Identify the cause before changing code. Preserve existing contracts unless the requested fix requires changing them. Prefer a focused correction over a broad cleanup.

If repeated corrections fail the same scenario, compare their observed results and write down the assumption they share. Inspect whether the failure originates in the product, environment, or observation method before another patch. Seek a narrow observation that distinguishes the proposed cause from alternatives. A failed correction is evidence against its hypothesis, not permission to add more guards.

For ownership, timing, or distribution failures, inspect the relevant actors and their state or lifecycle. Find what assigns the problematic state before compensating for it. Use existing diagnostics first; do not require an actor census for an unrelated local defect or create instrumentation outside the authorized scope. Missing observations remain explicit gaps. Revisit the assumption when evidence contradicts it, while preserving useful verified work.

Choose a correction that removes the demonstrated cause and preserves relevant contracts. A retry, fallback, or symptom guard is appropriate only when the behavior requires it and its limits are understood. If the cause needs an action outside scope or a product decision, explain the dependency and complete independent checks; do not conceal the unresolved defect behind passing unrelated tests.

Add a regression test when it can exercise the failure reliably through the real interface. Demonstrate failure before the fix and success after it when feasible. Use an existing executable check instead when a new test would require brittle mocks or substantial infrastructure.

Repeat the original failing scenario after the fix under comparable conditions and record the result. If it cannot be exercised, report that gap without treating other passing tests as proof that the reported defect is resolved. Run checks appropriate to the affected behavior and inspect the final diff for unintended changes.

Finish with the cause and correction, followed by the original command or action, its observed failure, and its result after the fix. Include other relevant checks and remaining limitations. Use the observations already collected; do not claim a reproduction or successful check that did not occur.
