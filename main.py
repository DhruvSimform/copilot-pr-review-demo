from fastapi import FastAPI
from api.v1.routes.todos import router as todos_router

app = FastAPI(
    title="Todo API",
    description="A simple todo API POC with in-memory storage",
    version="0.1.0",
)

# Include v1 routes
app.include_router(todos_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Todo API v1"}


def main():
    import os
    import uvicorn
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
