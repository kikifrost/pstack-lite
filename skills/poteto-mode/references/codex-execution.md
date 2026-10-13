# Codex execution

Use tools exposed in the current session. Read and edit files through the available shell and patch tools. Search repository content with rg. Discover connected tools through the exposed tool metadata when their data is relevant; do not assume Cursor MCP directories exist.

Do not use Cursor Task, AskQuestion, TodoWrite, /loop, subagent_type, pstack-models.mdc, or fixed model slugs. Ask an optional text question through the available user-input tool when the missing answer matters, and continue independent work. Use normal commentary for progress and keep the final answer self-contained.

Work inline by default. Delegation requires an explicit user request or applicable higher-priority instruction. If it is authorized, use the session's Codex collaboration tools, read the mixed-agents skill where applicable, assign distinct scopes, and inspect actual artifacts. Inherit the parent model unless a user or applicable instruction explicitly specifies another available model. Do not create sidebar chats for internal subtasks.

Follow current user instructions, applicable AGENTS.md, and contribution rules. A skill grants no additional permission to send messages, publish, push, deploy, merge, delete data, or change unrelated settings. Continue actions already authorized without repeatedly asking.

Consult the current repository's own rules rather than maintaining duplicate rules in this skill. Read applicable AGENTS.md first, then relevant architecture, contribution, and frontend design documents if present. Document locations and required checkpoints belong to the repository; do not assume every project uses the same names or layers.

Use existing checks at the affected scope. Shared infrastructure, cross-module work, or unclear impact requires the repository's full gate. Prefer offline fixtures and disposable storage appropriate to the project. Follow the repository's development and test-ordering convention. Add necessary regression tests and register new tests with its existing test runner where required.

Protect unrelated changes, credentials, real databases, and login sessions. Use the documented deployment pipeline if deployment is authorized. Do not hand-edit generated frontend output.
