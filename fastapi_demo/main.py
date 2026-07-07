from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Pydantic Models
class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


# In-memory storage
tasks = []
next_id = 1


# Create Task
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id

    new_task = Task(
        id=next_id,
        title=task.title,
        completed=task.completed
    )

    tasks.append(new_task)
    next_id += 1

    return new_task


# Get All Tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


# Get One Task
@app.get("/tasks/{id}", response_model=Task)
def get_task(id: int):
    for task in tasks:
        if task.id == id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# Update Task
@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == id:
            task = Task(
                id=id,
                title=updated_task.title,
                completed=updated_task.completed
            )
            tasks[index] = task
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# Delete Task
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    for index, task in enumerate(tasks):
        if task.id == id:
            tasks.pop(index)
            return

    raise HTTPException(status_code=404, detail="Task not found")