---
name: verify
description: Verify requested software behavior through existing tests and relevant user interfaces, reporting evidence and coverage gaps. Use to prove a feature or fix works, or to prepare a requested reusable verification recipe.
---

# Verify the outcome

Read [core values](../pancake/references/values.md) and applicable repository instructions. Establish the behavior to prove from the request, ticket, or recent change. Define the expected observable result before running checks. If no useful target can be identified, ask what behavior needs verification.

For a requested reusable project recipe, or when a relevant recipe already exists, read [project verification recipes](references/recipes.md). Reuse existing recipes only after checking their relevant assumptions. Do not generate a recipe during every verification task.

Inspect documented commands, existing tests, and available tools. Choose the smallest set of checks that covers the requested behavior and affected contracts. Reuse the project's harness before proposing new infrastructure. Inspect unfamiliar commands for side effects before running them. A build, lint check, or passing test suite proves only what it exercises.

Exercise the interface relevant to the claim when feasible. For a UI, perform the action and inspect its result. For a CLI, invoke the command and inspect output, exit status, and relevant files. For an API or library, call its supported interface and inspect the response or resulting state. Include a failure or boundary case when it materially affects the claim. Do not substitute internal state setters, mocks, or screenshots of an unrelated build for the requested behavior.

Check that the observation can distinguish the intended behavior from the relevant failure. An assertion that a mock was called, a value exists, or no exception occurred may be insufficient for the claimed outcome. Prefer a concrete expected output or observable effect grounded in the contract, independent of the code under test. For a meaningful absence, exercise the triggering condition and inspect the relevant state rather than accepting an empty fixture as proof. Mocks can isolate dependencies, but results must still exercise the behavior being claimed.

For a defect, use the original scenario and comparable before-and-after evidence when available. Do not alter the expected result to match broken behavior. For behavior-preserving changes, check the relevant contract rather than internal call order unless that order is itself required. Verification alone does not authorize adding or deleting tests; report ineffective checks and propose the focused correction when editing is outside scope.

For work delivered in units, associate each result with the artifact and state checked. Verify a prerequisite before relying on it, then exercise the combined outcome after integration. A collection of passing isolated checks cannot establish an untested interaction. Recheck earlier evidence when later changes invalidate its assumptions, without rerunning unrelated checks by default.

Use isolated local or test storage and accounts when available. Verification authorizes appropriate local checks, not live customer writes, external messages, deployment, or global configuration changes. Do not assume that a dry-run has no side effects. When a check requires authorization outside the task or an unavailable capability, complete the independent checks and report the specific gap. Do not modify product code, install dependencies, or generate project-specific skills merely to verify it unless separately authorized.

If starting a local instance is needed and permitted, confirm its readiness and that it runs the intended code before interacting with it. Avoid driving an existing instance with unknown ownership or shared state. Track processes and temporary resources created by the run. Clean those up on success and failure. Stop only the processes you started, and preserve relevant evidence outside disposable application state. Report cleanup failures rather than hiding them.

Capture enough evidence to connect each action with its observed result, such as command output, response bodies, screenshots, or resulting file contents. Keep artifacts proportional to the task and exclude credentials or unrelated user data. State where retained artifacts can be inspected when they add useful evidence.

Report which behaviors passed, failed, or remain unverified, with the checks and observations supporting each conclusion. Distinguish a product failure from an environment or tooling failure. Stop at verification findings unless repair was requested. Do not claim full coverage when the requested interface was not exercised or a material case remains unchecked.
