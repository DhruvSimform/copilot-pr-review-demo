from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter(prefix="/todos", tags=["todos"])

# In-memory storage for POC
todos_db: dict[int, dict] = {}
next_id: int = 1


class TodoCreate(BaseModel):
    """Schema for creating a todo."""
    title: str = Field(..., min_length=1, description="Todo title")
    description: Optional[str] = Field(None, description="Todo description")
    completed: bool = Field(False, description="Completion status")


class TodoUpdate(BaseModel):
    """Schema for updating a todo."""
    title: Optional[str] = Field(None, min_length=1, description="Todo title")
    description: Optional[str] = Field(None, description="Todo description")
    completed: Optional[bool] = Field(None, description="Completion status")


class TodoResponse(BaseModel):
    """Schema for todo response."""
    id: int
    title: str
    description: Optional[str]
    completed: bool


@router.get("/", response_model=list[TodoResponse])
async def get_todos() -> list[TodoResponse]:
    """Get all todos."""
    return [
        TodoResponse(
            id=todo_id,
            title=todo["title"],
            description=todo["description"],
            completed=todo["completed"],
        )
        for todo_id, todo in todos_db.items()
    ]


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate) -> TodoResponse:
    """Create a new todo."""
    global next_id
    todo_id = next_id
    next_id += 1
    
    todos_db[todo_id] = {
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
    }
    
    return TodoResponse(
        id=todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int) -> TodoResponse:
    """Get a specific todo by ID."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )
    
    todo = todos_db[todo_id]
    return TodoResponse(
        id=todo_id,
        title=todo["title"],
        description=todo["description"],
        completed=todo["completed"],
    )


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_update: TodoUpdate) -> TodoResponse:
    """Update a specific todo."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )
    
    todo = todos_db[todo_id]
    
    if todo_update.title is not None:
        todo["title"] = todo_update.title
    if todo_update.description is not None:
        todo["description"] = todo_update.description
    if todo_update.completed is not None:
        todo["completed"] = todo_update.completed
    
    return TodoResponse(
        id=todo_id,
        title=todo["title"],
        description=todo["description"],
        completed=todo["completed"],
    )


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int) -> None:
    """Delete a specific todo."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )
    
    del todos_db[todo_id]
