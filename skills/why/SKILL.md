---
name: why
description: Investigate the rationale and history behind existing code or a design decision. Use for why an approach was chosen, historical constraints, or the motivation for a change. Use how for execution flow and fix for defect repair.
---

# Explain why the code is this way

Read [core values](../pancake/references/values.md) and applicable repository instructions. Keep the investigation read-only.

Anchor the question in the relevant behavior, symbol, or design decision. Inspect the implementation and its callers to establish what exists now. Narrow a broad question using the available context and state that interpretation. Ask only if no useful target can be identified.

Trace relevant local history with scoped git log, blame, and commit patches. Follow renames when appropriate. Blame identifies the last edit, not necessarily the original decision. Read the introducing change and meaningful revisions rather than treating commit titles or dates as proof of motivation. Distinguish the rationale at the time from constraints that still apply today.

Look for explicit rationale in nearby documentation, design records, tests, and supplied ticket or pull-request discussions. Tests establish intended behavior, not necessarily why it was chosen. Follow concrete references when they help answer the question. Use accessible remote sources only when relevant and permitted by the request and host permissions. Do not search unrelated team conversations, fetch repository history, install connectors, or require a sweep of every available service. If history is shallow or a source is inaccessible, state the resulting limit and continue with local evidence.

Separate conclusions by their evidence.

- A recorded reason comes from an inspected source that explicitly explains the choice. Cite that source and attribute the reason to its author or record.
- An inferred reason comes from code, changes, or constraints that suggest a tradeoff. Label it as inference and explain what supports it.
- An unknown reason lacks enough evidence. Say so instead of inventing intent or presenting the most plausible explanation as established history.

Reconcile conflicting sources by describing their scope and timing. A later explanation may describe the current design rather than its original motivation. Do not assume the original reason remains valid or that missing documentation means a choice was accidental.

Lead with the best-supported answer. Explain the decisive constraints and tradeoffs in plain language. Link inspected code locations, commits, or documents next to the claims they support. Preserve uncertainty when simplifying the explanation. Stop once the question is answered or the remaining evidence gap is clear. Do not append a redesign or change files unless requested.
