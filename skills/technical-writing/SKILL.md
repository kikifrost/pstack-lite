---
name: technical-writing
description: "Use when explicitly requested as technical-writing to draft or revise repository documentation, ADRs, PR descriptions, or commit prose."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Write technical prose for its reader

Identify the reader's task and use the repository's established format and language.

- Tutorials teach by doing and give an observable result at each important step.
- How-to guides provide steps toward a concrete goal and link background separately.
- References describe actual options, inputs, outputs, limits, and errors.
- Explanations connect a bounded topic to its reasons, constraints, and alternatives.

Use these distinctions to organize content, not to demand new documents or a rigid template for a small edit. Prefer concrete mechanisms, real command and symbol names, active voice, and ordinary words. Put conditions before the steps they guard. Keep terminology consistent and pronouns unambiguous. Preserve technical qualifications while cutting filler.

Check each command, file link, and factual claim against the current repository. Do not invent flags or successful results. Follow CONTRIBUTING.md for commit and PR format, identity, and governance. A PR description leads with the concrete problem and resulting behavior, then relevant validation.

Update current facts alongside implementation when required. Record a changed accepted decision in a new ADR and link the superseded decision; do not rewrite its historical reasons or prohibit unexamined alternatives.

Use [unslop](../unslop/SKILL.md) for a focused editing pass only when it adds value. Product strings follow the project's design rules. Do not force English-only sentence limits, tab indentation, or a fixed response structure on Chinese prose or existing repository formats.
