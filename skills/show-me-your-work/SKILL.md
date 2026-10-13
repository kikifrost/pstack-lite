---
name: show-me-your-work
description: "Use when explicitly requested as show-me-your-work to keep an evidence-backed decision trail for a migration or long development task."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Keep a reviewable decision trail

Record consequential decisions and checkpoints, not every command. Use one TSV per task with columns ts, phase, decision, why, evidence, and result. Evidence is a verified file, artifact, commit, or URL pointer; results distinguish measured success, failure, open work, and inconclusive checks.

Use [scripts/log.sh](scripts/log.sh) with six arguments: log path, phase, decision, reason, evidence, and result. It timestamps in UTC, keeps cells on one line, and protects leading spreadsheet formula characters. The [header template](references/decision-log-template.tsv) documents the column order.

Keep the log outside tracked project files by default, in a task-specific temporary or app artifact directory. Report its absolute path when handing it back. Put it in the repository only when requested or needed by the agreed deliverable. Do not log credentials, session data, sensitive exports, or unrelated chat history.

Use one writer per log. Parallel workers get separate logs; the coordinator may merge their evidence sequentially. The helper is not a concurrent logging service. Append a correction that identifies the prior row rather than changing history.

On resumption, read existing rows and add a start row naming the current run and the scope being continued. Before delivery, check this run's entries against the actual actions and artifacts available in the current conversation. Do not search other chats' local transcripts or invent a transcript path. State missing evidence plainly.

Independent review is optional when explicitly requested; it does not require a different model family or authorize filing backlog issues. Summarize only meaningful outstanding concerns from the trail.
