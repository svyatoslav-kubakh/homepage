Title: AI coding agents in daily backend work
Date: 2026-04-10
Slug: ai-assisted-workflows-in-action
Summary: Practical experience integrating tools like Claude Code and Antigravity into real engineering routines.

There is a lot of hype and skepticism around AI in software development. In practice, modern AI agents like Claude Code and Antigravity are powerful productivity multipliers when used deliberately.

Here is how I integrate them into my actual engineering workflow:

- **Spec-driven development:** Instead of asking an agent to write code from scratch with vague prompts, I write a short markdown specification first. Clarifying requirements, edge cases, and module interfaces upfront produces significantly cleaner code.
- **Test coverage and boilerplate:** Agents are exceptionally good at writing repetitive unit tests, test fixtures, mocks, and data transfer objects. Defining the interface and asking the agent to generate comprehensive test suites saves hours of routine typing.
- **Codebase exploration and refactoring:** When exploring a new library or refactoring legacy modules, agents help trace data flow, find usages, and verify edge cases across multiple files quickly.

The key is treating AI agents like capable junior engineers: always review the output, enforce architecture rules, and verify everything with tests.
