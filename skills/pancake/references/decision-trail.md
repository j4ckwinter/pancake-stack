# Decision trail

Use this during substantial work when consequential choices, failed approaches, or changing assumptions would be hard to recover from the final diff. Use ordinary progress updates for small tasks. Keep one trail in the conversation or existing task planning surface; save a separate artifact only when requested.

## Record what changes the work

Add a short entry when choosing between consequential alternatives, revising the plan, rejecting an approach, completing a material checkpoint, or discovering a blocker. Record the phase, choice, reason, evidence, and observed result. Identify unresolved assumptions and distinguish an expected result from an observed one. Skip routine tool calls and narration of every edit.

Point to evidence that exists and supports the claim, such as a relevant file and line, a check result with the command and conditions, or an actual artifact or commit. Include enough context to distinguish the state checked from later changes. If evidence is unavailable, say so. Do not invent timestamps, identifiers, links, or measurements.

Example entry for a hypothetical migration:

> Caller migration. Keep the old entrypoint until the remaining callers move. The caller search still finds two production uses. Evidence is the search result and the affected paths in this conversation. Migration remains incomplete; the next unit moves those callers and checks their behavior.

## Keep the record usable

Update the trail as decisions occur rather than reconstructing all reasons at the end. If a prior claim was wrong or a choice changes, add a correction that identifies the earlier entry and the new evidence. Preserve the distinction between the original observation and the revised conclusion.

For a requested saved record, follow repository conventions or the user's destination and reuse the existing task record where possible. Markdown is sufficient; no logger or fixed file format is required. Save only relevant decisions and evidence, excluding credentials and unrelated private content. Report the actual path. Saving does not authorize staging, committing, or publishing the record.

For parallel work, have workers return their consequential choices and evidence. The coordinator incorporates checked findings into the single task trail. Avoid concurrent writes to one record. On pickup, read the relevant existing entries, check current state, and distinguish prior evidence from checks performed now.

## Review and hand back

Before finishing, compare the trail with the available task context, diff, and verification evidence. Follow evidence pointers and correct unsupported claims. Include material pivots or gaps that would change a reviewer's understanding. Do not scan unrelated session history or imply unavailable transcripts were audited.

Use an independent read-only review when consequences justify it and delegation is permitted and available. Give the reviewer the relevant trail, artifacts, and evidence. Assess findings before acting. Otherwise review directly and describe it accurately; do not invent model diversity or independent approval.

Summarize consequential choices, verification gaps, and unresolved risks in the final answer, linking a saved trail when one exists. For unfinished work, use [handoff](../../handoff/SKILL.md) and include the trail's location or relevant entries. A decision record helps review the work; it does not prove the resulting behavior.
