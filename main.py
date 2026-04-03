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
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
