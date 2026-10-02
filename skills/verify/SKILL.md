---
name: verify
description: Verify requested software behavior through existing tests and relevant user interfaces, reporting evidence and coverage gaps. Use to prove a feature or fix works, rather than to review code or repair defects.
---

# Verify the outcome

Read [core values](../pancake/references/values.md) and applicable repository instructions. Establish the behavior to prove from the request, ticket, or recent change. Define the expected observable result before running checks. If no useful target can be identified, ask what behavior needs verification.

Inspect documented commands, existing tests, and available tools. Choose the smallest set of checks that covers the requested behavior and affected contracts. Reuse the project's harness before proposing new infrastructure. Inspect unfamiliar commands for side effects before running them. A build, lint check, or passing test suite proves only what it exercises.

Exercise the interface relevant to the claim when feasible. For a UI, perform the action and inspect its result. For a CLI, invoke the command and inspect output, exit status, and relevant files. For an API or library, call its supported interface and inspect the response or resulting state. Include a failure or boundary case when it materially affects the claim. Do not substitute internal state setters, mocks, or screenshots of an unrelated build for the requested behavior.

Use isolated local or test storage and accounts when available. Verification authorizes appropriate local checks, not live customer writes, external messages, deployment, or global configuration changes. Do not assume that a dry-run has no side effects. When a check requires authorization outside the task or an unavailable capability, complete the independent checks and report the specific gap. Do not modify product code, install dependencies, or generate project-specific skills merely to verify it unless separately authorized.

If starting a local instance is needed and permitted, confirm its readiness and that it runs the intended code before interacting with it. Avoid driving an existing instance with unknown ownership or shared state. Track processes and temporary resources created by the run. Clean those up on success and failure. Stop only the processes you started, and preserve relevant evidence outside disposable application state. Report cleanup failures rather than hiding them.

Capture enough evidence to connect each action with its observed result, such as command output, response bodies, screenshots, or resulting file contents. Keep artifacts proportional to the task and exclude credentials or unrelated user data. State where retained artifacts can be inspected when they add useful evidence.

Report which behaviors passed, failed, or remain unverified, with the checks and observations supporting each conclusion. Distinguish a product failure from an environment or tooling failure. Stop at verification findings unless repair was requested. Do not claim full coverage when the requested interface was not exercised or a material case remains unchecked.
