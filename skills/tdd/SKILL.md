---
name: tdd
description: Develop through a failing test before changing production code. Use for explicit TDD, test-first bug fixes, or requested regression tests with a practical test path.
---

# Develop through a failing test

Read [core values](../pancake/references/values.md) and applicable repository instructions. Use this workflow for requested test-first development. When the failure or intended behavior is unclear, use the reproduction and diagnosis guidance in [fix](../fix/SKILL.md) before starting the cycle below.

## Establish the behavior

Identify the requested observable result, affected interface, and existing test harness. Preserve behavior outside the request. Choose a small test that exercises the real interface and asserts a concrete result independent of the implementation. A mock-call assertion or a test that compares the function with itself does not establish the requested behavior.

If a useful test needs unavailable services, broad infrastructure, brittle mocks, or production-only state, explain the limit and choose the closest executable check. Do not create a framework or claim a test-first result when no failing-before check was run.

When only tests are requested, add and run the requested coverage, report whether it passes or exposes a defect, and stop without editing production code. A passing test is valid coverage of working behavior; do not manufacture a failure. Use the cycle below when implementation changes are authorized.

## Run the cycle

1. Add the smallest test for one requested behavior before editing production code. Keep existing assertions intact unless the requested contract changes.
2. Run that test against the current implementation. Inspect the failure and confirm it comes from the missing or broken behavior. A syntax error or missing dependency is not the required failure; correct the check or investigate before proceeding. If the intended behavior already exists, retain useful coverage and report that no production correction was needed.
3. Make the smallest production change that satisfies the behavior and its cause. Do not weaken the expected result to obtain a pass.
4. Rerun the same test and relevant nearby checks. Confirm both the requested result and preserved behavior.
5. Refactor only when it improves the affected code within scope. Rerun the checks after refactoring. Repeat the cycle for the next behavior when needed.

Review the resulting change with [check](../check/SKILL.md). Use the [implementation review guidance](../pancake/references/implementation.md#review-the-affected-contracts) for consequential contracts and independent-review capability limits. Passing tests do not replace review.

## Report the evidence

Name the test or executable check, the failure observed before the implementation change, and its result afterward. Include relevant preserved behavior, review results, and remaining gaps. Distinguish a passing existing test from a new regression that demonstrated the defect. Report an unexercised before-state explicitly rather than describing the work as a completed test-first cycle.
