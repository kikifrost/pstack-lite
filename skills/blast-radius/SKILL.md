---
name: blast-radius
description: "Use when explicitly requested as blast-radius or to analyze downstream breakage and prove a change's safety assumptions."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Check what a change can break

A caller list is a starting point. Hidden contracts often cross serializers, persistence, runtime ordering, or a language boundary.

1. Read the change and identify which observable behavior or assumption changed.
2. Trace direct consumers, serialized API shapes, database readers, configuration, worker lifecycle, and frontend behavior where relevant. Check the pinned version or local source of a library whose semantics determine safety.
3. Identify the one or two facts the change's safety relies on. Distinguish a source-code argument from executed evidence.
4. Prove the material fact with a cheap local test, temporary SQLite database, fixture, or running development flow. Prefer existing checks. If the target cannot be reached safely, report the fact as unproven with the missing evidence.
5. Report confirmed breakage first, then the proved safety fact, material remaining risk, and relevant cleared cases. Do not invent likelihood percentages or a long list of hypothetical failures.

Do not edit public contracts or product behavior merely to make the analysis pass. Preserve the project's approval boundaries. Use [interrogate](../interrogate/SKILL.md) only when a requested broader review would add value.
