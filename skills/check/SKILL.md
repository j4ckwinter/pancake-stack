---
name: check
description: Review a code change for actionable bugs, regressions, and verification gaps. Use when the user asks to check a diff, review changes, or assess what a change could break.
---

# Check a change

Read [core values](../pancake/references/values.md). Review without editing files unless the user separately requests fixes.

Use the supplied diff, commit, or branch range. If none is specified, inspect staged and unstaged changes, including relevant untracked files. If the workspace is clean and no review target can be inferred, ask for the target rather than inventing a comparison.

Read repository instructions and the changed code in context. Follow affected callers and contracts, including persisted data, external interfaces, and failure paths when relevant. Focus on concrete breakage rather than style preferences or hypothetical rewrites.

Look beyond symbol references when a change affects shared contracts. Follow the concrete data or lifecycle path to relevant consumers, including serialized fields, stored records, other languages or packages, configuration, feature flags, and initialization or teardown ordering. Check pinned dependency versions and local patches before relying on library behavior. Search only the boundaries implicated by the change; do not require a full inventory for a local edit.

Identify the consequential assumptions that make the change safe, such as compatibility with older stored data or callers completing before teardown. Seek evidence for those assumptions rather than listing hypothetical risks. A scoped search with no matches describes only the searched scope, not proof that external consumers do not exist. Label inaccessible consumers and missing evidence explicitly.

For each suspected issue, establish its trigger and consequence. Check surrounding code and tests for safeguards before reporting it. Run a focused check when available and safe; distinguish a static finding from a reproduced failure. Prefer an existing focused test or supported interface that exercises the real implementation and relevant dependency version. Do not create scripts or test files merely for a read-only review unless separately authorized. If a decisive assumption cannot be exercised safely, report it as unverified and name the cheapest useful check. Do not install dependencies, change user settings, or invoke live external services just to review a diff.

Lead with actionable findings, ordered by impact. Give each finding an inspected file location, the triggering scenario, and the resulting behavior. Label uncertainty. If there are no findings, say so and report material verification gaps. Mention consequential risks checked and cleared when that explains the verdict, with the evidence that cleared them. Keep unresolved assumptions separate from confirmed findings, and avoid invented probability estimates. Passing checks alone do not establish that the change is correct.
