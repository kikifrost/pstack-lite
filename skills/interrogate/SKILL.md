---
name: interrogate
description: "Use when explicitly requested as interrogate or adversarial review to find concrete correctness, boundary, and verification problems in a specified change."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Challenge a change with evidence

Review is read-only unless the user also authorizes fixing findings.

1. Establish scope from the requested diff, PR, or files. Inspect git status first to distinguish uncommitted edits from branch changes. Determine the actual base instead of assuming main. For a PR, attach it to the current task through the app artifact tool when available.
2. State the intended behavior in one short paragraph based on the request and available PR context. Use a bounded assumption when possible; ask only if missing intent blocks meaningful review.
3. Read the diff, callers, data types, and the tests that establish its contracts. Apply the relevant lenses in [Review checks](references/review-checks.md).
4. Trace each potential defect to a reachable trigger and a user-visible consequence. Run a safe local repro or relevant test when it settles a material concern. Reject speculative null warnings, style preferences, and unrelated rewrites.
5. Prioritize actionable findings. For each, give severity, the tightest verified file location, trigger, effect, and suggested correction. Deduplicate repeated symptoms of the same cause. State no actionable findings when that is the actual result, plus material unverified behavior.

Work inline by default. If the user explicitly asks for parallel review, use available Codex collaboration tools and the mixed-agents skill where applicable. Give reviewers independent scopes, use parent-model inheritance unless an authorized configuration says otherwise, and verify their findings yourself. Do not claim model diversity without different models actually running.

Use native inline code comments for actionable findings when the app supports them. Do not post GitHub comments, open a follow-up PR, merge, or deploy merely because a review completed; follow existing authorization and contribution rules.
