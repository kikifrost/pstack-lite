---
name: architect
description: "Use when explicitly requested as architect to design a consequential data model, interface, or module boundary before implementation."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Design from the caller's operation

Read repository architecture rules and the relevant existing modules. For frontend design, read the project's design document first. Recover the current contract from callers and tests; use history only if rationale changes the choice.

1. Show a realistic call site or user operation first. Derive the required inputs, return value, error behavior, state ownership, and lifecycle from it.
2. Sketch the smallest domain model and interface that hide the implementation complexity. In Python, prefer dataclasses for data and functions unless state has a clear owner. Keep I/O at the existing boundaries.
3. Use [Design checks](references/design-checks.md). Compare alternatives only when there is a real tradeoff; do not require two prototypes for a routine local choice.
4. State the chosen shape, relevant alternative, migration impact, and how observable behavior will be verified. Do not add placeholder code to the repository merely to illustrate a sketch.
5. Implement when implementation is part of the request. A design-only request ends with the reviewable sketch. If implementation reveals repeated workarounds or contradictory invariants, revisit the model rather than adding exceptions indefinitely.

Repository approval requirements still apply. A new top-level semantic region, reversed dependency direction, or interaction-flow change must reach the required checkpoint. Routine module-local choices do not need repeated confirmation. Do not weaken a stable public contract to simplify an internal design.
