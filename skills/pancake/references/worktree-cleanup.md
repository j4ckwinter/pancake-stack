# Clean up worktrees

Read this for requested worktree cleanup or separately authorized removal of task-owned worktrees. An inventory or disk-usage question remains read-only. Cleanup scope does not include simulators, package caches, unrelated directories, branch deletion, or user settings unless requested.

## Inspect before choosing

Resolve the relevant repository and enumerate worktrees with `git worktree list --porcelain`. Use paths from that inventory rather than guessing directory names. Record each candidate's path, branch or detached HEAD, revision, and relevant lock or prune state. Identify the current worktree and preserve it.

Inspect each candidate with read-only Git commands for staged and unstaged changes, untracked files, and ignored files that removal could discard. A clean tracked diff does not establish that the directory contains no useful data. Check task evidence and known workers or processes for active use. Age, a merged PR, a branch name, or no visible process alone does not prove abandonment. Do not search unrelated chat history to infer ownership. Keep uncertain or active candidates until their use is resolved.

Determine whether commits are retained by a surviving ref or otherwise need preservation, especially for detached HEAD worktrees. Compare against the intended destination using current available evidence. Squash or rebase merges may not appear as ancestry; do not classify unique commits as disposable merely from an ancestry check or claim remote state is current without observing it.

## Establish the removal set

Summarize the concrete candidates and evidence for removal, including useful local data, active use, or unique commits that require preservation. A cleanup request covers candidates clearly within its scope when inspected evidence establishes they are unused and useful work is retained. Do not ask again for authorization already given. Obtain a required decision before discarding uncommitted work, useful ignored or untracked data, or commits without a retained reference. Complete the inventory and preservation proposal before asking.

Do not create commits, stashes, archives, or pushes just to make a candidate disposable without authorization for that preservation action. Report candidates held back and what would resolve their status. Locks are a signal to investigate, not an obstacle to bypass.

## Remove and confirm

Recheck the selected candidate immediately before removal so intervening edits or worker activity are not missed. Use ordinary `git worktree remove` on the exact authorized path. If Git refuses, inspect why and preserve the candidate rather than escalating to force removal or recursive filesystem deletion. Forced removal or loss of useful data requires explicit authorization covering the concrete loss.

Treat stale administrative records separately from live directories. Use prune inspection or dry-run support before an authorized prune; do not infer that a temporarily unavailable directory has been deleted. Preserve branch refs unless deletion is separately requested.

Read back the worktree inventory and inspect operation results. Report removed and retained candidates, preservation status, and failures. Measure disk use before and after only when space reclamation is part of the task; do not invent reclaimed-byte counts from directory sizes. Cleanup is complete only for the confirmed removal set, not for every worktree found.
