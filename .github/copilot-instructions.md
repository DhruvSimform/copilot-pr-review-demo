# Project Guidelines

## Code Style
- Follow PEP 8 for all Python code.
- Prefer clear function and variable names, type hints, and small focused functions.
- Keep comments concise and only for non-obvious logic.

## Dependency Management
- Use `uv` as the dependency and environment manager.
- Use `uv add <package>` to add dependencies.
- Use `uv remove <package>` to remove dependencies.
- Use `uv sync` to install from the lockfile.
- Use `uv run <command>` to run project commands.
- Do not use `pip`, `pipenv`, or `poetry` unless the user explicitly asks.

## FastAPI Best Practices
- Use FastAPI patterns such as `APIRouter`, dependency injection with `Depends`, and Pydantic models for request and response schemas.
- Define explicit response models and proper HTTP status codes.
- Raise `HTTPException` for expected API errors.
- Keep business logic outside route handlers when possible.
- Prefer `async` endpoints for I/O-bound operations and avoid blocking calls.
- Validate inputs and return consistent error structures.

## Clarify Before Development
- If requirements are ambiguous, ask clarifying questions before writing or modifying code.
- Confirm assumptions when acceptance criteria, API behavior, or data models are unclear.
- Start implementation only after open questions are resolved.
