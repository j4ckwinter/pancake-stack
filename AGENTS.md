# Contributor instructions

Keep this project focused on Codex plugin foundations until the user requests skills.

- Do not add `SKILL.md` files, runnable skills, commands, or hooks yet.
- Use the current official portable plugin contract for `plugin.json` and the documented Codex marketplace format.
- Keep preference examples and their proposed contract consistent.
- Preserve the absence of global side effects. Do not write user preferences or register a marketplace as part of repository checks.
- Distinguish proposed commands from host commands. Do not claim an alias or installation flow works without testing it on the named host.
- Do not select a license, publish, or commit without authorization.

Validate JSON parsing, marketplace source resolution, and the absence of `SKILL.md` files after foundation changes. Installation remains a separate host check.
