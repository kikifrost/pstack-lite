---
name: poteto-mode
description: "Use when explicitly requested as poteto-mode or pstack engineering mode to investigate, implement, refactor, or review a concrete task."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Poteto mode for Codex

Work from observed behavior and domain ownership. Choose the smallest change that solves the task and verify the result on the surface the user uses.

Read [Codex execution](references/codex-execution.md) when starting this workflow. It defines tool mapping and authorization without replacing repository rules.

## Choose the amount of process

For a narrow question, inspect the relevant code and answer directly. For a local fix, reproduce, trace the cause, implement, and verify. A typo or spacing adjustment needs no architecture panel or new test.

For multi-step work, maintain a short plan using an available planning tool or a working checklist. Read only the matching section in [Workflows](references/workflows.md). A request for a plan ends with a plan; it does not authorize implementation.

## Optional support

Read another skill only when it resolves an actual uncertainty, using its sibling path.

- [how](../how/SKILL.md) traces runtime behavior and ownership.
- [why](../why/SKILL.md) finds recorded rationale.
- [architect](../architect/SKILL.md) settles a consequential data model or interface.
- [interrogate](../interrogate/SKILL.md) challenges a diff when review is requested or a material concern remains.
- [blast-radius](../blast-radius/SKILL.md) checks consumers and hidden contracts.
- [benchmark-checklist](../benchmark-checklist/SKILL.md) checks measured performance claims.
- [typescript-best-practices](../typescript-best-practices/SKILL.md) supports TypeScript modeling.
- [technical-writing](../technical-writing/SKILL.md) supports requested documentation.
- [show-me-your-work](../show-me-your-work/SKILL.md) records consequential decisions when a long task warrants a trail.

Do not invoke all of these for every task. Apply principles directly instead of loading separate principle skills or naming them in every reply.

## Delivery

Report the changed behavior, the reason for the chosen fix, actual validation, and remaining uncertainty. Separate local results from CI. Do not turn every completed task into a commit, PR, deployment, or merge. Follow the user's request and repository contribution rules for those actions.
