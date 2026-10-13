---
name: how
description: "Use when explicitly requested as how to explain a named subsystem, runtime flow, module ownership, or layering decision from repository evidence."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Explain how the code works

Identify the entry point and the user's concrete question. Start with a bounded interpretation when the scope is unclear.

1. Read applicable repository instructions and the relevant architecture documentation. Use rg to locate entry points, types, callers, and tests; do not read the whole repository by default.
2. Trace one representative operation from input through validation, business logic, storage or external adapters, and output. Follow failure handling as well as success.
3. Name who owns state, the lifetime of that state, and any process or worker boundary. Distinguish persisted status from an in-process assumption.
4. Confirm an uncertain behavior with a safe local fixture or existing test when that materially improves the answer. A walkthrough does not authorize editing code or contacting production.
5. Explain the flow with a few verified file and symbol references. Include gotchas only when they affect the question. Label inferences rather than filling gaps with guesses.

For a single function, answer in a short paragraph. Use a compact flow diagram or ownership table only for a multi-component question. Do not spawn an explainer for a question the current agent can answer. Consult [why](../why/SKILL.md) only if the user also needs motivation or historical context.
