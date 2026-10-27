# Clean up comments

Use this reference before implementation review when the changed code contains comments or suppressions, and for explicitly requested comment cleanup or audits. Follow repository conventions and keep the work within the requested files or diff. If no scope can be established from the request or task context, ask for it rather than assuming the whole repository or a base branch.

When cleanup accompanies an implementation task, limit edits to comments attached to the code changed for that task, including adjacent comments whose claims the change affects. Reading a file or editing one function does not authorize cleaning up other functions or the whole file. Preserve unrelated working-tree changes. A standalone cleanup request may explicitly name a broader file, directory, or diff scope; use that scope only when requested. Inspect outside the edit scope when needed to understand a comment, without expanding cleanup to the inspected code.

## Delegate the comment review

The lead schedules one comment pass for the scoped diff. When agents are available and permitted, follow the [review context and settings protocol](host-runtime.md) and assign an independent read-only reviewer the scoped diff and this reference. An assigned Comment Critic applies the policy directly and must not delegate another comment pass. Use the Comment Critic role: challenge every comment against the exceptions below, identify code that needs clearer structure, and report findings without editing application code. This is a review brief, not a required host agent type. The lead inspects each finding and applies authorized corrections. If delegation is unavailable, perform the same inspection directly and report that limit. Skip the pass when the diff has no code comments or suppressions.

Require the reviewer to identify each location, recommend removal or an evidenced exception, and name any underlying code problem. Mark concrete code problems as refactor targets with the symbol and reason; the label is a finding, not permission to expand scope. Reject invented defects, scope escapes, and removals that violate an exception. Keep comment findings distinct from correctness findings.

## Inspect before removing

Read each candidate with the code it describes. Remove redundant narration, stale banners, misleading claims, and commented-out dead code when their purpose is established and editing is authorized. Remove narration and test-phase commentary even when accurate. Assertions, test names, and code structure should explain the steps. For confusing code under our control, identify the smallest useful rename, type, or structural correction rather than polishing an explanatory comment.

Keep legal and license headers, public API contracts, required tooling directives, and evidenced non-obvious constraints imposed by external dependencies, platforms, or protocols. Keep issue or RFC links that explain a constraint code cannot express. Do not retain banners or implementation narration merely because they use documentation syntax. A comment-like token inside a string, fixture, or generated output may be program data; inspect its consumers before treating it as removable prose. Follow the source generator's ownership rather than editing generated files directly.

For an ambiguous comment, trace the relevant behavior, callers, tests, and available rationale. Use [how](../../how/SKILL.md) or [why](../../why/SKILL.md) when needed. Do not accept an unexplained warning as a keep exception. Trace its claim and report an unresolved constraint explicitly. Preserve a potentially necessary directive or constraint record until its removal is justified; uncertainty is not proof that deletion is safe. Do not use a deletion quota or assume that fewer comments means clearer code.

## Separate cleanup from repairs

When a comment explains confusing names, synchronized flags, hidden sequencing, or a workaround, identify the exact code and the burden it creates. Propose a rename, type, extraction, or design change only when it addresses that problem. Comment cleanup alone does not authorize application-code refactoring. For an authorized repair, follow [the implementation sequence](implementation.md) and check the affected behavior.

Inspect lint and type-check suppressions against the diagnostic, its reason, and the actual implementation. A suppression may protect a necessary external workaround. Remove one only when evidence and an appropriate check establish that it is obsolete or its underlying problem has been fixed within scope. Report an unresolved correctness issue separately from optional cleanup; do not silence a diagnostic elsewhere to make removal pass.

When a comment records an invariant, preserve it until any proposed replacement safeguard is implemented and verified. Choose a type, boundary validation, test, or lint rule that owns the actual constraint. Check that it rejects the relevant invalid case and permits a valid case before deleting documentation made redundant by that enforcement. Keep rationale or exceptions the safeguard does not express. If encoding is outside scope or remains unverified, retain the comment and report the proposed safeguard.

## Verify and report

Inspect each comment edit against the task's changed code or explicitly requested cleanup scope. Revert any task-owned cleanup outside that boundary while preserving unrelated user edits. Inspect the diff for accidental code, directive, or data changes. Run the existing checks relevant to the affected files, including generation, documentation, lint, or behavioral checks where comments have tooling significance. A prose-only edit may need only direct inspection; state the actual verification and any unexercised behavior. Do not add tests merely to count comments or mirror the cleanup instructions.

For an audit, return concrete candidates and reasons without editing. For requested edits, report the affected files, meaningful removals or corrections, preserved constraints, checks performed, and unresolved refactor proposals. Keep cleanup findings separate from confirmed defects. Do not commit or publish unless requested.
