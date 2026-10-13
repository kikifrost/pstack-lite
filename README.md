# Pstack Lite

从 [pstack](https://github.com/cursor/plugins/tree/main/pstack) 精选的 12 个工程技能，面向 Codex 做了精简和适配。适合日常开发、排障、代码审查、性能验证与技术文档工作。

默认需要点名调用。不会因为安装而自动开启完整模式，也不强制多代理、固定模型、提交、PR 或部署。

## 技能

| 技能 | 用途 |
|---|---|
| `poteto-mode` | 按任务规模完成调查、实现和验证 |
| `poteto-help` | 选择技能和了解调用方式 |
| `how` | 追踪运行流程、状态归属和模块边界 |
| `why` | 从文档、ADR、提交和 PR 追溯决策原因 |
| `architect` | 从调用方操作设计数据模型与接口 |
| `interrogate` | 查找 diff 中有证据的缺陷和验证缺口 |
| `blast-radius` | 分析下游影响并证明关键安全前提 |
| `benchmark-checklist` | 核查性能比较是否测到了正确工作 |
| `technical-writing` | 编写文档、ADR、PR 描述和提交说明 |
| `unslop` | 精简空话，保留技术含义和不确定性 |
| `show-me-your-work` | 记录有证据的关键决策与检查点 |
| `typescript-best-practices` | 改善 TypeScript 建模与边界验证 |

## 安装

需要 Python 3.10 或更高版本；安装本身不需要第三方 Python 包。

```bash
git clone https://github.com/kikifrost/pstack-lite.git
cd pstack-lite
python3 scripts/install.py
```

默认安装到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时安装到 `~/.codex/skills`。可以指定目录，也可以只安装部分技能。

```bash
python3 scripts/install.py --dest /path/to/codex/skills how why interrogate
```

安装前会检查所有目标目录。发现同名技能时整次安装退出，不覆盖现有文件。先比较已有版本，并自行备份或移动后再安装。已经安装本精简版的用户不需要重复安装。

## 使用

在 Codex 中用 `$skill-name`，或直接用自然语言点名。例如：

```text
用 poteto-mode 排查任务卡住的问题，修复后验证原来的触发条件。
用 how 解释 API 入队到 worker 执行之间的状态流转。
用 interrogate 审查当前 diff，重点检查多 worker 下的共享状态。
```

`poteto-mode` 可以按任务需要读取辅助技能。普通小改动不要求设计面板或新的测试。只要求方案或审查时，不自动转成实现。

Codex 通过每个技能的 `agents/openai.yaml` 读取 `allow_implicit_invocation: false`。技能安装后若未显示，可重启 Codex。加载机制见 [官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## Codex 适配与边界

- 去除了 Cursor 的 `Task`、`AskQuestion`、`/loop`、固定模型路由和自定义模式配置。
- 使用当前环境可用的文件、终端、提问和协作工具；默认由当前 agent 完成任务。
- 并行代理只在用户或适用的更高优先级指令授权时使用，不承诺不存在的模型或工具。
- 以所在项目的 `AGENTS.md`、贡献规范、架构和设计文档为准；技能不额外授予发布、部署、对外发消息或数据删除权限。
- 不捆绑项目代码、数据库、登录会话、个人路径或模型凭证。来源项目的规则文件名称只作为如何读取本地规范的例子。

工程方法可用于其他 agent，但这份安装方式、调用策略和工具映射针对 Codex。其他环境可能忽略 `agents/openai.yaml`，需要自行适配加载和权限机制；本仓库不声称已验证跨环境运行。

## 验证

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/check.py
```

检查技能结构、YAML、内部链接和点名调用配置，并使用临时目录验证安装冲突保护及 TSV 日志行为。GitHub Actions 执行同一检查。

这些检查验证分发包和脚本，不证明每个 agent 在真实任务中都会遵循流程，也不代表完整开发工作流已经通过实测。

## 来源和许可

上游作者是 Lauren Tan（poteto）。保留 [MIT 许可证](LICENSE)，改写范围和来源记录见 [NOTICE.md](NOTICE.md)。这是独立适配项目。
