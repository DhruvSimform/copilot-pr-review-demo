---
description: "Restructure a Python file or selected Python code to follow PEP 8 and project conventions without changing behavior."
name: "Restructure Python File"
argument-hint: "Target file, selected code, or refactoring goal"
agent: "agent"
---
Restructure the provided Python file or selected Python code to follow PEP 8 and the project instructions in [copilot-instructions.md](../copilot-instructions.md).

Requirements:
- Preserve existing behavior unless the user explicitly asks for functional changes.
- Improve readability with clear names, smaller focused functions, and consistent formatting.
- Add or improve type hints when they clarify the code.
- Keep comments concise and only where logic is not obvious.
- Avoid unnecessary abstraction or large-scale rewrites.
- If the request is ambiguous, ask clarifying questions before modifying code.
- If dependencies are needed, use `uv` commands and do not use `pip` unless explicitly requested.

Expected outcome:
- The file is easier to read and maintain.
- The code follows PEP 8 and project conventions.
- Any behavior-preserving refactor is minimal and focused.
