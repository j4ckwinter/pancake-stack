---
name: pr
description: Draft a pull request title and description grounded in the ticket and actual branch diff. Use for PR wording, or preparing a requested PR creation or update.
---

# Prepare a pull request

Read [core values](../pancake/references/values.md) and applicable repository instructions. Draft in chat by default. Creating or updating a remote PR requires an explicit request covering that action.

## Establish the change

Use the supplied ticket, conversation, and requested review scope. Inspect the current branch, git status, and relevant commits with read-only commands. Identify the base from the user's request, existing PR metadata when accessible, or clear repository evidence. An upstream tracking branch is not necessarily the PR base. Do not assume main or include the entire repository history. If the base cannot be established, ask for it before claiming a complete branch comparison.

Review the merge-base-to-head diff for committed changes. Inspect staged, unstaged, and relevant untracked changes separately. State when a draft includes local work that would not yet appear in a remote PR. Exclude unrelated work where the scope is clear, and flag mixed scope when it cannot be separated. Do not stage, commit, push, or change branches merely to draft a description.

Read changed code and relevant callers only as needed to explain the resulting behavior. Check applicable PR templates and contribution requirements. Use supplied ticket details without inventing acceptance criteria, links, or closing references.

## Write for the reviewer

Lead with the concrete problem and the resulting behavior. Use a before-and-after example when it clarifies the change. Choose a title that describes the final scope, rather than the conversation history or an abandoned approach.

Keep a small PR brief. Include implementation details only when they explain a consequential decision or help assess the change. Follow the applicable repository template. Otherwise, include a concise description, relevant verification, and material risks or remaining work without empty boilerplate sections.

Report checks actually run and their observed results. Attribute checks reported in the conversation and do not imply they were rerun or cover later changes. Mark planned or missing verification explicitly. Do not run tests, start a review, or repair code merely to produce wording unless separately requested. A passing build does not prove all behavior works.

Return a copyable title and Markdown body without a preamble. Add a short scope note outside the body when the draft includes uncommitted work or an unresolved base. Preserve uncertainty and limitations that matter to approval. Do not claim that a PR exists or has been updated when only a draft was produced.

## When remote publication is requested

Confirm the repository, source branch, base, and intended PR from available evidence. Finish preparing the title and body before the remote write. If the source branch is not published, report that prerequisite and obtain authorization to push unless already covered by the request. Do not include local-only changes as though they are on the remote branch.

Use an available supported tool. Pass multiline content as a structured argument or an exact temporary body file, such as gh's --body-file, rather than interpolating text into shell code. Update only the requested PR fields. After creation or update, read back the title, body, and branch targets. Report the actual PR link and any failed operation. Do not merge, deploy, message reviewers, or change PR state unless requested.
