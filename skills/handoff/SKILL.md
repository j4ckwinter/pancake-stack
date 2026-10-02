---
name: handoff
description: Prepare a concise continuation note for a new chat or colleague from the current task, conversation, and repository state. Use for handing off work, summarizing where to resume, or requested task pickup and pause.
---

# Hand off the work

Read [core values](../pancake/references/values.md). Prepare a self-contained note for someone who has not read the conversation. Summarize the active objective and latest user constraints, not the entire chat history.

Use the current conversation and supplied task or ticket as the primary context. In a repository, inspect the current branch, HEAD, git status, staged diff, and unstaged diff with read-only commands. Read relevant changed or untracked files only when needed to clarify the work. Distinguish changes belonging to this task from unrelated workspace changes. If repository access is unavailable, state that the workspace state could not be checked. Do not invent a branch, ticket, or completed action.

Include the information needed to resume, usually in these short sections.

- **Objective.** The requested outcome and important scope limits.
- **Current state.** Completed and unfinished work, relevant files, and the observed branch and commit when applicable. Distinguish local, staged, committed, and confirmed published work. A clean working tree does not prove a push or deployment.
- **Decisions.** Choices that constrain the next step and their known reasons. Separate accepted decisions from proposals and assumptions.
- **Verification.** Checks actually run, their results, and material coverage gaps. Name the tested revision or state when known. Preserve results from the conversation as previously reported, without implying that they were rerun or cover later changes.
- **Blockers and next steps.** Known blockers, pending decisions or approvals, and the first concrete action to take. State when no blocker was reported rather than assuming none exists.

Include exact commands, paths, and artifact links only when useful for continuation and supported by inspected files or the conversation. Report active processes or temporary resources when known, along with any remaining cleanup. Do not inspect unrelated sessions or external services to fill gaps. Omit credentials and unrelated personal information.

Keep the note proportional to the task. Omit empty sections and repetitive chronology. Preserve uncertainties that could affect the next action. Reference applicable repository instructions so the recipient reads them before acting. A handoff records authorization boundaries; it does not grant the recipient additional permission.

Return the note in the response. Save it to a file only when requested, using the requested destination and preserving unrelated content. Do not stage, commit, publish, send messages, stop processes, or continue implementation merely to make the handoff look complete.

For requested pickup or an explicit pause, read [continuation guidance](references/continuation.md). A pickup summary stays read-only; continuation follows only when requested.
