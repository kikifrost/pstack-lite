---
name: why
description: "Use when explicitly requested as why to trace a design decision, regression history, or unexplained constant to recorded rationale."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Investigate why a decision was made

Code establishes behavior; code alone does not establish the author's intent.

1. Anchor the question to a symbol, file, contract, or decision. Read the relevant current docs and accepted ADRs before reconstructing history.
2. Inspect bounded history. Use git blame for the relevant lines, git log --follow for renamed files, or git log -S for the introduction of a symbol or constant. Read substantive commit messages and diffs, rather than assuming the most recent edit made the decision.
3. Follow linked PRs or issues through available GitHub tools or an authenticated gh command when that would answer the question. Search another connected source only when the question or evidence points there. Do not scan all accounts, chats, or observability systems by default.
4. Separate explicit rationale, conclusions supported by several sources, inference, and unknowns. Cite the actual source next to each claim. If sources disagree, show the disagreement.
5. If the answer will inform a change, identify the constraints to preserve and which reasons might no longer apply. An ADR records an accepted decision within its scope, not a prohibition on all alternatives.

Use [Evidence confidence](references/evidence-confidence.md) when the record is incomplete or contradictory. State material sources unavailable or searched without success; do not produce a seven-category coverage report for a narrow question. This is read-only work unless the user also requests a change.
