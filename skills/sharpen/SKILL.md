---
name: sharpen
description: Make a task deeper rather than bigger, then rewrite its prompt. Use when the user asks to sharpen a task or prompt before work starts.
---

# Sharpen the task

Read [core values](../pancake/references/values.md) and [sift](../sift/SKILL.md). Sharpening rewrites a prompt; it does not start the task, change files, or run checks.

Take the task from the user's message, or from the most recent request if they point at it. When it concerns a repository, inspect only enough of it to ground the answers below in its real code, data, and checks. Ask only when no task can be identified.

Aim for a deeper version of the same task, not a bigger one. Keep its outcome and scope, and answer briefly:

1. What would a strong practitioner in this field do here that the prompt does not ask for?
2. What raw material would they start from, instead of a summary or secondhand description?
3. Which methods and tools would they use?
4. What evidence, other than the agent's or the user's opinion, would show the result is right?

Drop an answer that would add work without changing the outcome or how it is proven.

Then rewrite the prompt so it asks for exactly that. Have it name the raw sources to read, the method, and the observable check that decides success. Have it ask the agent to settle any choice an experiment can settle by prototyping it and recommending an option from what it observed. Leave product and preference choices that no experiment can settle open for the user, and list them.

Return the four short answers and the rewritten prompt, ready to paste. Do not run the rewritten prompt unless the user asks.
