# Active host boundary

Read this reference before model discovery, preference helpers, or delegated model selection. Keep the shared workflows and review requirements the same on both hosts.

## Preferences and discovery

Identify the active client from its tools or explicit session context. Do not infer it from PATH or inherited environment variables. Codex uses the existing helper commands without a host flag. Claude Code adds `--host claude` before every helper subcommand, including `show`, `save`, `resolve`, `resolve-challenge`, and `resolve-implementation-review`. An explicit `--config <path>` before the subcommand overrides either host's location. Never read the other host's profile as a fallback or migrate it without a request.

Codex stores preferences under `$CODEX_HOME/pancake-stack/config.json`, defaulting to `~/.codex/pancake-stack/config.json`. Claude Code uses `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, defaulting to `~/.claude/pancake-stack/config.json`. These are plugin preference files, not host settings. Saving them does not change the current conversation.

On Codex, run the installed Setup `scripts/catalog.py` before asking for model choices. It uses the local Codex app server's `model/list` protocol. If the executable is not on PATH, use an observable host-provided executable with `--codex <path>`. Report actual discovery failures and prefer active host metadata when the local server differs from the current host.

On Claude Code, run the installed Setup `scripts/catalog.py --host claude` before asking for model choices. If the executable is not on PATH, use an observable host-provided executable with `--claude <path>`. It reads initialization metadata without a user message or model turn. It keeps user model settings, excludes project and local settings, disables hooks, and blocks MCP and tools. Returned model values are host choices, not proof of authenticated account access or delegated selection. Missing effort metadata returns no discovered effort choices; never invent levels. Active host metadata takes precedence when the discovery process differs from the current host. On actual failure, report the reason and use observable active-host metadata or picker information, or offer inheritance. Do not run the Codex catalog for Claude or infer IDs from the other host's preferences.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. Use Claude Code's native model selection when available; do not assume a saved full model ID is accepted by a tool expecting aliases. Use effort selection only when the active interface exposes it. Omit inherited settings rather than inventing values. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Distinguish supported choices, resolved requests, and observed application. Record accepted or reported model and effort separately. Unknown or rejected settings cannot prove parity. Ordinary unavailable role overrides use the workflow's disclosed host fallback. Selected panel entries follow their existing coverage rules and remain uncovered when unsupported. Keep one reviewer per selected panel entry, completed per-reviewer verdicts, and bounded concurrency. Direct sequential passes do not establish independent review.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. Both load the same installed workflow tree. Resolve helpers and references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
