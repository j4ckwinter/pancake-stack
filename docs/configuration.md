# Task settings

Pancake Stack 0.20.0 has no persistent preference store or runtime configuration scripts. Direct work uses the current conversation settings. Delegates inherit the active host's model and effort unless the user explicitly supplies choices for the task.

## Choose reviewers

A nonempty task-supplied panel requests one independent reviewer per entry. Specify whether it applies to Challenge or consequential implementation review. Omitted model or effort choices inherit host settings. An absent or explicitly empty implementation panel retains one independent reviewer for consequential changes. Challenge chooses independent review according to the consequences and available capabilities when no panel is supplied. Explicit task limits on delegation take precedence.

Each selected reviewer needs an identified, completed verdict. Unsupported choices and incomplete reviewers remain coverage gaps. A requested model is not proof of the model actually selected. Workflows report accepted or observed settings when available and do not invent values for inheritance.

Example task wording:

> For this implementation, use two independent reviewers with inherited host settings. Report each completed verdict and any missing review coverage.

To request particular models, supply their host-supported names in the task. Model and effort are separate choices. Setup can help phrase the request without running discovery scripts or saving a profile. Choices adopted in a conversation apply to the specified task, not future chats.

## Migration from 0.19.x

Older versions used JSON preferences and Python helpers. Version 0.20.0 does not read, migrate, overwrite, or delete those files. Existing saved model choices and reviewer panels no longer apply. Restate any desired choices in the current task.

Old Codex profiles may remain under `$CODEX_HOME/pancake-stack/config.json`, defaulting to `~/.codex/pancake-stack/config.json`. Claude profiles may remain under `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, defaulting to `~/.claude/pancake-stack/config.json`. They are inert for this version. No manual deletion is required to use the library.

Update the installed package and start a fresh chat to use new instructions. A version bump in the source repository does not update an existing installation. Installation remains a separate host action.
