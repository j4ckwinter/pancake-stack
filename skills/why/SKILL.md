---
name: why
description: Investigate the rationale and history behind existing code or a design decision. Use for why an approach was chosen, historical constraints, or the motivation for a change. Use how for execution flow and fix for defect repair.
---

# Explain why the code is this way

Read [core values](../pancake/references/values.md) and applicable repository instructions. Keep the investigation read-only.

Answer from the record, not the code. Anchor the question in the behavior, symbol, or decision, and state your interpretation of a broad one. Read the change that introduced it and each meaningful later change, following renames; blame shows only the last edit, and a commit title is not a motive. Then read nearby documentation, design records, tests, and any supplied ticket or pull-request discussion. Use accessible remote sources only when relevant and permitted. Do not fetch repository history, install connectors, or sweep unrelated conversations or services. When history is shallow, the trail is thin, or a source is inaccessible, say so and continue with what exists.

Label each reason by its evidence:

- **Recorded**: an inspected source explains the choice. Cite it and attribute the reason to its author.
- **Inferred**: code, changes, or constraints suggest a tradeoff. Say what supports it.
- **Unknown**: the record does not answer. Say so rather than offering the likeliest story as history.

A later explanation may describe the current design rather than the original motive, and an old reason may no longer apply. Lead with the best-supported answer, link the commits, code, or documents next to the claims they support, and stop when the question is answered or the remaining gap is clear. Do not append a redesign or change files unless requested.
