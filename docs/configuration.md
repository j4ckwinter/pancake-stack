# Task settings

Pancake Stack 0.20.0 has no persistent preference store or runtime configuration scripts. Direct work uses the current conversation settings. Delegates inherit the active host's model and effort unless the user explicitly supplies choices for the task or names an [economy model for gathering delegates](#use-an-economy-model-for-gathering-work).

## Choose reviewers

A nonempty task-supplied panel requests one independent reviewer per entry. Specify whether it applies to Challenge, standalone Check, or consequential implementation review. Omitted model or effort choices inherit host settings. An absent or explicitly empty implementation panel retains one independent reviewer for consequential changes unless multi-model review was explicitly requested. Challenge chooses independent review according to the consequences and available capabilities when no panel is supplied. Explicit task limits on delegation take precedence.

Each selected reviewer needs an identified, completed verdict. Unsupported choices and incomplete reviewers remain coverage gaps. A requested model is not proof of the model actually selected. Workflows report accepted or observed settings when available and do not invent values for inheritance.

Example task wording:

> For this implementation, use two independent reviewers with inherited host settings. Report each completed verdict and any missing review coverage.

An explicit multi-model request without a nonempty model list selects two distinct models from the active host's exposed choices, or the requested count. A reviewer count alone inherits host settings. When distinct choices cannot be established, the workflow reports the diversity gap and completes permitted review. It does not silently replace unsupported requested models.

To request particular models, supply their host-supported names in the task. Model and effort are separate choices. Setup can help phrase the request without running discovery scripts or saving a profile. Choices adopted in a conversation apply to the specified task, not future chats. The one standing choice is an economy model for gathering delegates, which lives in your own instruction file.

## Use an economy model for gathering work

Gathering delegates are read-only and return located facts for the lead to check. Their work is bulk reading, searching, inventories, fetching pages, and tracing existing behavior to explain it. They can run on a cheaper model than the conversation. Every other delegate keeps its inherited or task-chosen settings, and so does the lead. That includes reviewers, candidates and judges, implementation workers, and any delegate that writes, runs checks, investigates a defect, or recommends an approach. [Host guidance](../skills/pancake/references/host-runtime.md#gathering-delegates) owns the full rule.

Pancake Stack never picks the cheaper model itself. Name it in the task, using a name the host's delegation tool accepts:

> Use ECONOMY_MODEL as the economy model for gathering delegates. Report each delegate's requested and observed model.

To make it standing, put a host-specific line in your own user or repository instruction file. Pancake Stack reads what the host has loaded and writes nothing, so this is your instruction, not a saved Pancake preference:

> For Pancake Stack gathering delegates on Claude Code, use sonnet as the economy model. Apply this only as the "Gathering delegates" section of Pancake Stack's `skills/pancake/references/host-runtime.md` defines. Where that guidance is not loaded, and for every other delegate, keep inherited or task-chosen settings.

Without a named economy model, gathering delegates inherit like every other delegate. If the host rejects the named model, the delegate inherits and the fallback is reported.

The lead inspects the decisive source locations behind a gathering result and treats it as covering only the scope it reports. A result that fails inspection is rerun once with inherited settings, and the rerun is reported. A requested model is still not proof of the model applied.

## Migration from 0.19.x

Older versions used JSON preferences and Python helpers. Version 0.20.0 does not read, migrate, overwrite, or delete those files. Existing saved model choices and reviewer panels no longer apply. Restate any desired choices in the current task.

Old Codex profiles may remain under `$CODEX_HOME/pancake-stack/config.json`, defaulting to `~/.codex/pancake-stack/config.json`. Claude profiles may remain under `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, defaulting to `~/.claude/pancake-stack/config.json`. They are inert for this version. No manual deletion is required to use the library.

Update the installed package and start a fresh chat to use new instructions. A version bump in the source repository does not update an existing installation. Installation remains a separate host action. The [Codex installation and refresh recipe](codex-installation.md) includes a check of the cached manifest version.
