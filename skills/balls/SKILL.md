---
name: balls
description: Draft a short spoken standup update covering blockers, aims, and lessons learned for technical and nontechnical colleagues. Use for balls or a standup update in this format.
---

# Prepare a standup update

Turn the current ticket and its working branch into an update the user can say aloud. BALLS means blockers, aims, and lessons learned.

Start with the ticket details supplied by the user or already available in the conversation. Inspect the current branch name, git status, staged diff, and unstaged diff with read-only commands. Read relevant changed files when needed, including untracked files identified by status. If there are no local changes, inspect recent commits relevant to the ticket, using a known base branch when available. Do not assume that all branch history or workspace changes belong to this ticket.

Use branch names and changes to understand progress, not as proof of the ticket's acceptance criteria, blockers, or intentions. If the ticket cannot be identified and the changes do not provide enough context, ask for the ticket summary. Do not fetch remote history or retrieve tickets from external services unless requested. Do not edit files, stage changes, switch branches, run application code, or send the update.

Use the requested reporting period. Otherwise, describe the ticket's current status without assuming when work happened. Distinguish local implementation from tested, merged, or released work. A next step inferred from the changes is a suggested aim, not a confirmed commitment.

Write three short bullets in this order, usually one sentence each and about 30 seconds aloud overall.

- **Blockers.** State what is preventing progress, its effect, and any known help needed. Say there are no blockers only when the context confirms that. If none are mentioned, say that no blockers were reported.
- **Aims.** State the next intended outcome and why it matters. Keep plans separate from completed work and commitments. Do not invent deadlines or promise delivery.
- **Lessons learned.** State a concrete takeaway supported by the context and its practical effect. If no lesson is available, say that no specific lesson was captured rather than inventing one.

Use first-person language the user can read aloud. Translate implementation details into what changes for people using or maintaining the product. Keep essential technical terms only when the audience needs them, with a brief plain explanation. Avoid file paths, model IDs, acronyms, and internal process details unless they are central to the update.

Return only the update. Do not add a preamble, a status report, or an explanation of the technique. Keep uncertainties and unresolved work clear. Keep repository inspection focused on the current ticket. Do not expand the standup into a code review or a new investigation.
