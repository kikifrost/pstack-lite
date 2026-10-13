---
name: poteto-help
description: "Use when explicitly asked for poteto-help, pstack usage help, or choosing one of the locally installed pstack workflows."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Pstack help in Codex

This installation is a curated Codex adaptation, not the complete Cursor plugin. Find the requested outcome in the table, then give one usable prompt. Read the target SKILL.md if explaining its detailed behavior.

| Goal | Skill | Example |
|---|---|---|
| Complete a development task with verification | [poteto-mode](../poteto-mode/SKILL.md) | 用 $poteto-mode 排查抓取任务卡住的问题 |
| Understand runtime flow or ownership | [how](../how/SKILL.md) | 用 $how 解释手动抓取从 API 到 worker 的流程 |
| Find recorded design rationale | [why](../why/SKILL.md) | 用 $why 查清配置为什么迁入数据库 |
| Design a data model or interface | [architect](../architect/SKILL.md) | 用 $architect 设计任务重试的状态模型 |
| Challenge a change | [interrogate](../interrogate/SKILL.md) | 用 $interrogate 审查当前 diff |
| Check downstream effects | [blast-radius](../blast-radius/SKILL.md) | 用 $blast-radius 分析这个响应字段变化的影响 |
| Verify a performance comparison | [benchmark-checklist](../benchmark-checklist/SKILL.md) | 用 $benchmark-checklist 核查查询提速结果 |
| Write technical documentation | [technical-writing](../technical-writing/SKILL.md) | 用 $technical-writing 更新这次修复的文档 |
| Remove filler from existing prose | [unslop](../unslop/SKILL.md) | 用 $unslop 精简这段 PR 描述 |
| Keep a decision trail | [show-me-your-work](../show-me-your-work/SKILL.md) | 用 $show-me-your-work 记录这次迁移的关键决策 |
| Improve TypeScript modeling | [typescript-best-practices](../typescript-best-practices/SKILL.md) | 用 $typescript-best-practices 检查前端任务状态类型 |

All 12 pstack skills, including this help skill, preserve the upstream explicit-invocation intent through Codex's agents/openai.yaml. The user can name a skill in natural language or invoke it with $skill-name. Poteto mode may read a relevant companion after it is explicitly invoked. Installation alone does not activate a persistent mode.

Do not recommend Cursor /loop, custom-mode shortcuts, setup-pstack, or removed skills. Models and reasoning settings are controlled by the current Codex session. Do not promise untested runtime integration.
