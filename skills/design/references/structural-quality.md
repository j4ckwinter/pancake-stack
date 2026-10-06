# Assess structural quality

Use this reference for structural simplification and maintainability choices during design, or for an explicitly requested structural or code-quality review. Follow [core values](../../pancake/references/values.md) and repository conventions. Assess the requested design, files, or diff; read relevant callers and contracts for context without turning the task into a repository-wide audit. A proposal or review remains read-only unless implementation is requested.

## Trace the burden

Start with a concrete user or caller scenario. Trace where its data comes from, which decisions it crosses, and what can change its state. Identify the layers a reader must follow and the hidden state or sequencing they must remember. Ground concerns in inspected locations and actual usage rather than names, line counts, or a preferred architecture.

Look for opportunities to eliminate complexity while preserving the required behavior:

- Duplicated domain decisions, scattered feature checks, and special cases that could have one coherent owner.
- Pass-through wrappers, speculative extension points, and adapters that add another vocabulary without hiding useful complexity.
- Synchronized flags or optional fields that admit contradictory states, repeated casts, and guards compensating for an unclear boundary. Use [TypeScript guidance](typescript.md) when applicable.
- Mutable state with unclear ownership, unnecessary coordination, and updates that can leave a required invariant half-applied.
- Callers that depend on internal representations, hidden initialization order, or repeated conversions.
- Obsolete branches and compatibility paths whose consumers or retirement conditions need checking.

Treat these as questions to investigate, not automatic defects. A wrapper can own a real boundary, a guard can protect mutable or untrusted state, and duplication can keep independently changing concerns separate. Large files and many branches are signals to trace responsibility; they are not failures by themselves. Do not impose a line-count threshold, extraction quota, or universal signature style.

## Compare a concrete simplification

For each supported concern, describe the current caller path and the smallest plausible alternative. Prefer deleting an unnecessary decision, state value, or layer over spreading the same complexity across more files. Keep a direct local implementation when a new abstraction would cost more than it saves. Reuse established owners and helpers when their contracts actually fit.

Explain what becomes easier to understand or change and what the alternative costs. Identify affected callers, compatibility, persistence, lifecycle, and failure behavior where relevant. A smaller diff or fewer lines does not establish better structure. Reject a simplification that removes a necessary contract, obscures ownership, or makes the central user flow harder to use.

Separate confirmed structural regressions introduced by the change from existing debt, optional improvements, and subjective preferences. A maintainability recommendation is not a correctness bug or an automatic merge blocker. Tie any blocking recommendation to a demonstrated contract violation or the project's explicit acceptance criteria. Report uncertainty when inaccessible callers or missing evidence prevent assessing an alternative.

## Verify and return

For a review, return the inspected location, concrete burden, proposed simplification, decisive tradeoff, and cheapest useful verification for each material recommendation. Report actual checks separately from proposed checks. If no worthwhile improvement is supported, say so rather than manufacturing refactors.

For a design, incorporate supported improvements into the existing usage sketch and recommendation instead of creating a second competing plan. Include migration and verification needs only where relevant. For authorized implementation, follow [the implementation sequence](../../pancake/references/implementation.md), keep edits within task scope, and exercise the affected behavior and contracts after restructuring. Passing static checks alone does not prove behavioral equivalence. Comment cleanup follows its own [requested-cleanup scope](../../pancake/references/comment-cleanup.md).
