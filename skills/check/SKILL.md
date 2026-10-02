---
name: check
description: Review a code change for actionable bugs, regressions, and verification gaps. Use when the user asks to check a diff or review changes.
---

# Check a change

Read [core values](../pancake/references/values.md). Review without editing files unless the user separately requests fixes.

Use the supplied diff, commit, or branch range. If none is specified, inspect staged and unstaged changes, including relevant untracked files. If the workspace is clean and no review target can be inferred, ask for the target rather than inventing a comparison.

Read repository instructions and the changed code in context. Follow affected callers and contracts, including persisted data, external interfaces, and failure paths when relevant. Focus on concrete breakage rather than style preferences or hypothetical rewrites.

For each suspected issue, establish its trigger and consequence. Check surrounding code and tests for safeguards before reporting it. Run a focused check when available and safe; distinguish a static finding from a reproduced failure. Do not install dependencies, change user settings, or invoke live external services just to review a diff.

Lead with actionable findings, ordered by impact. Give each finding an inspected file location, the triggering scenario, and the resulting behavior. Label uncertainty. If there are no findings, say so and report material verification gaps. Passing checks alone do not establish that the change is correct.
