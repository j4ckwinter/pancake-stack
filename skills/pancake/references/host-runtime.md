# Active host boundary

Read this reference before model discovery, preference helpers, or delegated model selection. Keep the shared workflows and review requirements the same on both hosts.

## Preferences and discovery

Direct work uses current conversation settings without reading saved preferences. Setup and explicit preference inspection may use the helpers directly.

For delegated work, resolve saved models only while preparing the delegate, when supported model selection can use them. `preferences.py resolve` returns all three roles and takes no positional role argument. Read the relevant role from its output. An explicit task model bypasses saved role lookup even when effort is omitted. For an omitted or null task model, run `resolve` only when the interface can select the missing model. Merge task model choices over the resolved role model.

Delegates inherit host effort by omitting the effort argument. Saved `reasoningEffort` fields remain stored but are inactive. Resolver output reports only supplied observable host effort or `null`; it is informational and must not become an effort override. Apply an effort only when explicitly requested for this task and supported by the active interface. Effort-only task choices may still need saved model resolution. A resolve command reports inactive non-null saved effort on stderr without changing the file. Retain that disclosure when it affects the user's existing preferences.

For reviewer panels, a task-supplied list replaces the saved list. Otherwise read the saved panel when preparing review; its size matters even without model selection controls. An explicitly empty task list selects the workflow's fallback. Read saved role fields for that fallback only when supported selection needs them. Keep unsupported requested selections as coverage gaps.

Identify the active client from its tools or explicit session context. Do not infer it from PATH or inherited environment variables. Codex uses the existing helper commands without a host flag. Claude Code adds `--host claude` before every helper subcommand, including `show`, `save`, `resolve`, `resolve-challenge`, and `resolve-implementation-review`. An explicit `--config <path>` before the subcommand overrides either host's location. Never read the other host's profile as a fallback or migrate it without a request.

Codex stores preferences under `$CODEX_HOME/pancake-stack/config.json`, defaulting to `~/.codex/pancake-stack/config.json`. Claude Code uses `$CLAUDE_CONFIG_DIR/pancake-stack/config.json`, defaulting to `~/.claude/pancake-stack/config.json`. These are plugin preference files, not host settings. Saving them does not change the current conversation.

On Codex, run the installed Setup `scripts/catalog.py` before asking for model choices. It uses the local Codex app server's `model/list` protocol. If the executable is not on PATH, use an observable host-provided executable with `--codex <path>`. Report actual discovery failures and prefer active host metadata when the local server differs from the current host.

On Claude Code, run the installed Setup `scripts/catalog.py --host claude` before asking for model choices. If the executable is not on PATH, use an observable host-provided executable with `--claude <path>`. It reads initialization metadata without a user message or model turn. It keeps user model settings, excludes project and local settings, disables hooks, and blocks MCP and tools. Returned model values are host choices, not proof of authenticated account access or delegated selection. Missing effort metadata returns no discovered effort choices; never invent levels. Active host metadata takes precedence when the discovery process differs from the current host. On actual failure, report the reason and use observable active-host metadata or picker information, or offer inheritance. Do not run the Codex catalog for Claude or infer IDs from the other host's preferences.

## Delegated settings

Use the host's available delegation interface. Codex collaboration tools and Claude Code's Agent tool have different argument contracts. Pass only settings supported by the actual exposed tool. If selecting a worker model or effort requires a fresh context, use that supported invocation instead of a full-history fork that cannot accept overrides. Use Claude Code's native model selection when available; do not assume a saved full model ID is accepted by a tool expecting aliases. Use effort selection only when the active interface exposes it. Omit inherited settings rather than inventing values. Never combine model and effort into an identifier or change global settings to emulate a missing override.

Distinguish supported choices, resolved requests, and observed application. Record accepted or reported model and effort separately. Unknown or rejected settings cannot prove parity. Ordinary unavailable role overrides use the workflow's disclosed host fallback. Selected panel entries follow their existing coverage rules and remain uncovered when unsupported. Keep one reviewer per selected panel entry, completed per-reviewer verdicts, and bounded concurrency. Direct sequential passes do not establish independent review.

## Invocation and project skills

Codex plugin skills use `$pancake-stack:<skill>`. Claude Code plugin skills use `/pancake-stack:<skill>`. Both load the same installed workflow tree. Resolve helpers and references from their installed skill location rather than the user's workspace.

When a user explicitly requests a project skill, use the active host's authoring guidance. Codex project skills live in `.agents/skills/<name>/SKILL.md`. Claude Code project skills live in `.claude/skills/<name>/SKILL.md`. Preserve the requested destination and invocation policy. Never write into the installed plugin cache to personalize a project.
