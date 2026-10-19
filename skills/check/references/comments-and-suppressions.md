# Review comments and suppressions

Compare their claims with the implementation. Preserve useful intent, compatibility constraints, external limitations, and required license or tooling directives. Redundant narration alone is not an actionable bug; avoid turning a change review into a comment-removal exercise.

When a comment claims a requirement, such as ordering, exclusive ownership, or exact wording, trace why it matters and whether code, types, tests, or tooling enforce it. A comment can describe a real constraint even when enforcement is absent. Report a missing safeguard only with a concrete triggering scenario and consequence, separating confirmed breakage from a proposed improvement. Recommend the smallest appropriate enforcement within scope; a review does not authorize implementing it or deleting the constraint's record.

For lint or type-check suppressions, inspect the diagnostic being suppressed, the reason, and the guarded behavior. Distinguish a justified external limitation from a hidden defect or stale workaround. Do not assume that a suppression is wrong or that removing it preserves behavior. When recurring workarounds suggest a faulty design, describe the shared premise and affected callers rather than proposing another exception. Leave optional cleanup separate from correctness findings and include it only when requested or material to the review.
