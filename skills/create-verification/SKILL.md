---
name: create-verification
description: Create a project-local verification skill that proves the app works the way a user drives it, or that formally checks a property where tests reach least. Use when the user asks for a verification skill, a control skill, or a reusable model check for a repository.
---

# Create a verification skill

Read [core values](../pancake/references/values.md) and applicable repository instructions. The user's request authorizes writing one project-local skill and the scratch state needed to prove it, nothing more. Do not change product code, install global tools, commit, or publish unless the request covers it.

The skill is written for an agent who reads it cold, mid-task, and has never seen the app. Use the repository's real commands, paths, and names, and leave no placeholders. Put it where the active host loads project skills, as [host guidance](../pancake/references/host-runtime.md) describes, with frontmatter that names the app or area and says when to use it; without frontmatter it never registers. If a maintained verification guide or harness already covers the need, extend it instead and say so.

## Choose the kind from the code

Answer from the repository first, and ask the user only what cannot be observed. If the user named an area or a bug, start there.

- **Drive the app** when the project has no scripted way to prove user-facing behavior. Find the primary surface, how it starts locally, how an agent can drive it (existing harnesses first), what evidence can be captured, and whether two instances can run side by side. Follow [project verification recipes](../verify/references/recipes.md) for the content: prerequisites, launch and readiness from empty state, a read-only check that the running instance is the intended one, the drive steps, evidence that survives cleanup, and cleanup of only what the run started. Map the few user-facing features the request covers, one entry per feature with how to reach it, how to drive it, and the end state that proves it. Map more only when asked.
- **Check a property formally** when a promise the code makes would harm users if broken and tests rarely reach the breaking case, such as ordering, retries, concurrency, or a parser. Pick the strongest such target, not the easiest, and the cheapest tool that can answer it. Follow [formal verification](../verify/references/formal-verification.md) for the method. The generated skill states the property and the harm in one plain sentence each, gives one rerun command with a pinned tool version, records which files and functions the check covers and the commit at which that was last confirmed, and tells the next agent how to tell a real bug from a modeling error.

If the checkout does not build or start as-is, report that precisely before writing steps against it.

## Prove it before handing it over

Follow the generated skill once, as the next agent would.

- For a drive skill: launch, run the readiness check, drive one mapped feature, capture evidence, and clean up. Confirm the evidence still exists afterwards.
- For a formal skill: run the check on a scratch copy with a change that breaks the property in the real code, confirm it catches the break, then confirm the check on the unchanged code passes or fails only on findings you will report.

Fix the skill, not the scenario, when a step fails, and run its cleanup after every failed attempt. Take expected results from the contract, not from what the code does now. A current-code failure is a finding: report it with its counterexample in the code's terms, list it in the skill as a known failure rather than an expected result, and do not weaken the property or edit product code. If the proof ran in a stand-in for the real target, list the steps the stand-in did that the target will not; they remain unverified. A skill that was never run is a draft and is reported as one.

## Hand off

Report the skill's location, what it covers, the proving run and its result, findings, and what it does not cover. Maintaining the skill later follows [recipe maintenance](../verify/references/maintenance.md). Saving the skill does not authorize committing it.
