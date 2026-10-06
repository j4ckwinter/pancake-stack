# Clean up comments

Use this reference when the user explicitly requests comment cleanup or an audit of unnecessary comments. Ordinary implementation and change review do not require a comment-removal pass. Follow repository conventions and keep the work within the requested files or diff. If no scope can be established from the request or task context, ask for it rather than assuming the whole repository or a base branch.

When cleanup accompanies an implementation task, limit edits to comments attached to the code changed for that task, including adjacent comments whose claims the change affects. Reading a file or editing one function does not authorize cleaning up other functions or the whole file. Preserve unrelated working-tree changes. A standalone cleanup request may explicitly name a broader file, directory, or diff scope; use that scope only when requested. Inspect outside the edit scope when needed to understand a comment, without expanding cleanup to the inspected code.

## Inspect before removing

Read each candidate with the code it describes. Remove redundant narration, stale banners, misleading claims, and commented-out dead code when their purpose is established and editing is authorized. Preserve useful intent and rationale that the implementation does not express. If a comment is inaccurate but records a necessary constraint, correct its claim from evidence rather than discarding the constraint.

Keep legal and license headers, public API documentation, and directives used by compilers, linters, formatters, generators, or other tooling. Preserve compatibility requirements, external limitations, and relevant issue or RFC links. A comment-like token inside a string, fixture, or generated output may be program data; inspect its consumers before treating it as removable prose. Follow the source generator's ownership rather than editing generated files directly.

For an ambiguous comment, trace the relevant behavior, callers, tests, and available rationale. Use [how](../../how/SKILL.md) or [why](../../why/SKILL.md) when needed. Leave unresolved rationale intact and report the uncertainty. Do not use a deletion quota or assume that fewer comments means clearer code.

## Separate cleanup from repairs

When a comment explains confusing names, synchronized flags, hidden sequencing, or a workaround, identify the exact code and the burden it creates. Propose a rename, type, extraction, or design change only when it addresses that problem. Comment cleanup alone does not authorize application-code refactoring. For an authorized repair, follow [the implementation sequence](implementation.md) and check the affected behavior.

Inspect lint and type-check suppressions against the diagnostic, its reason, and the actual implementation. A suppression may protect a necessary external workaround. Remove one only when evidence and an appropriate check establish that it is obsolete or its underlying problem has been fixed within scope. Report an unresolved correctness issue separately from optional cleanup; do not silence a diagnostic elsewhere to make removal pass.

When a comment records an invariant, preserve it until any proposed replacement safeguard is implemented and verified. Choose a type, boundary validation, test, or lint rule that owns the actual constraint. Check that it rejects the relevant invalid case and permits a valid case before deleting documentation made redundant by that enforcement. Keep rationale or exceptions the safeguard does not express. If encoding is outside scope or remains unverified, retain the comment and report the proposed safeguard.

## Verify and report

Inspect each comment edit against the task's changed code or explicitly requested cleanup scope. Revert any task-owned cleanup outside that boundary while preserving unrelated user edits. Inspect the diff for accidental code, directive, or data changes. Run the existing checks relevant to the affected files, including generation, documentation, lint, or behavioral checks where comments have tooling significance. A prose-only edit may need only direct inspection; state the actual verification and any unexercised behavior. Do not add tests merely to count comments or mirror the cleanup instructions.

For an audit, return concrete candidates and reasons without editing. For requested edits, report the affected files, meaningful removals or corrections, preserved constraints, checks performed, and unresolved refactor proposals. Keep cleanup findings separate from confirmed defects. Do not commit or publish unless requested.
