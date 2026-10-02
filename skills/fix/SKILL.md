---
name: fix
description: Diagnose and fix a reported software defect with focused verification. Use for broken behavior, errors, and regression fixes.
---

# Fix a defect

Read [core values](../pancake/references/values.md) and applicable repository instructions.

Establish expected and actual behavior from the report and implementation. Reproduce the failure on the relevant surface when feasible. If reproduction is unavailable, state the missing evidence and proceed only as far as the available evidence supports.

Trace the symptom through its inputs, state changes, and callers. Identify the cause before changing code. Preserve existing contracts unless the requested fix requires changing them. Prefer a focused correction over a broad cleanup.

Add a regression test when it can exercise the failure reliably through the real interface. Demonstrate failure before the fix and success after it when feasible. Use an existing executable check instead when a new test would require brittle mocks or substantial infrastructure.

Run checks appropriate to the affected behavior and inspect the final diff for unintended changes. Report the cause, the correction, verification results, and any remaining limitation. Do not claim a reproduction or successful check that did not occur.
