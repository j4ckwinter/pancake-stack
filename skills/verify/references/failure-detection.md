# Check the check

Use this when creating or changing a consequential harness or safeguard. A passing check is useful only if it can reject the failure it claims to catch. Prefer an existing known failing revision or fixture before introducing a deliberate break.

Name the guarded behavior and a representative failure grounded in its contract. Choose a small change that violates that behavior, such as omitting a persisted write or allowing a duplicate operation. A syntax error or failed startup does not demonstrate detection of a behavioral defect. Keep a relevant valid case so an implementation that rejects everything cannot pass.

Run the check against the unmodified artifact first. If it fails, distinguish a product defect from a harness or environment problem before interpreting a negative control. Do not weaken the expected result to obtain a baseline pass.

Create a broken variant only when the task authorizes the necessary isolated edits. Use a disposable copy or worktree with separate state; preserve the user's working tree. Run the same check against that variant and confirm the failure is caused by the guarded behavior. An unrelated exception is inconclusive. If the check still passes, improve it within authorized scope and repeat both the broken and valid cases.

Restore or discard only the task-owned break, rerun the valid case, and retain the relevant result before cleanup. Report the source revision or state, deliberate change or failing fixture, command, observed failure, restored result, and limits. A single detected break demonstrates that case, not comprehensive test quality.

If isolation, edit permission, or a runnable baseline is unavailable, explain what remains untested. Do not modify product code during a read-only verification request merely to demonstrate detection.
