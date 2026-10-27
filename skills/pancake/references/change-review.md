# Prepare and review consequential changes

Classify by the affected contract, not line count. Changes to shared interfaces, serialized payload fields, persisted-data compatibility, security boundaries, or concurrency require independent review. Changes to agent instructions or release configuration also require independent review when they alter authorization, delegation, or verification behavior. Wording-only edits that preserve behavior, and local changes without these contracts, can use direct review.

## Before consequential edits

Identify the host's independent-review capability and permitted reviewer scope before editing. This is a capability check only; select the implementation-review panel when the change is ready for review. Investigation or code delegates and a separately requested pre-implementation Challenge apply their task choices when preparing that work. Carry these facts in the existing plan or conversation; a separate artifact is optional.

For consequential TypeScript data shapes or boundary handling, read [TypeScript guidance](../../design/references/typescript.md).

Settle consequential interface, ownership, compatibility, or persistence choices before implementation with [design](../../design/SKILL.md). Use [challenge](../../challenge/SKILL.md) when a consequential assumption is disputed or needs adversarial examination. Do not require it for every change. Resolve supported findings within the authorized scope before relying on the affected assumption. Small local changes can use the existing shape directly. Resolve repository facts through inspection; leave required product decisions explicit rather than guessing.

## Review the completed change

Before reviewing an implementation diff with code comments or suppressions, run the scoped [comment review](comment-cleanup.md). Resolve accepted findings within the authorized task before correctness review. A read-only review reports findings without edits.

Inspect the completed diff using [check](../../check/SKILL.md), including affected callers and contracts. Passing tests do not replace review.

Use a task-supplied implementation reviewer list when present. An absent or explicitly empty list retains one independent reviewer for consequential work. Do not use a Challenge panel for implementation review. Before launching reviewers, read and follow the [shared execution, context, settings, and coverage protocol](host-runtime.md). Require a completed verdict for each selected entry or report its concrete coverage gap.

Ask reviewers to inspect independently through [check](../../check/SKILL.md). Inspect and deduplicate findings by mechanism rather than vote count. Resolve supported findings within scope before completion and keep material disagreement explicit when evidence cannot settle it.

When independent review is required or requested, include the completed independent-review verdict before completion or the concrete capability or permission limit and direct-review result. If a reviewer is still running, wait for its verdict rather than reporting completion.
