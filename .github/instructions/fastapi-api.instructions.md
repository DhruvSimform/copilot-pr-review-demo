---
description: "Use when creating or modifying FastAPI APIs, routers, request/response schemas, validation, and endpoint error handling."
name: "FastAPI API Implementation Guidelines"
applyTo: "**/*.py"
---
# FastAPI API Guidelines

- Organize endpoints with `APIRouter` instead of placing all routes in one file.
- Use Pydantic models for request and response bodies; set explicit `response_model`.
- Return correct HTTP status codes and raise `HTTPException` for expected failures.
- Keep business logic outside route handlers; keep handlers thin and focused on HTTP concerns.
- Prefer `async def` for I/O-bound routes and avoid blocking operations in endpoints.
- Validate input constraints in schemas and return consistent error behavior.
- If requirements are unclear, ask clarifying questions before implementation.
- For dependencies, use `uv` commands (`uv add`, `uv remove`, `uv sync`, `uv run`) and avoid `pip` unless explicitly requested.
