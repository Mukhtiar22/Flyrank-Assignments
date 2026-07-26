from fastapi import FastAPI, status, HTTPException
from app.models import TaskCreate, TaskUpdate


app = FastAPI()


tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete FlyRank Assignment",
        "done": False
    },
    {
        "id": 3,
        "title": "Push code to GitHub",
        "done": True
    }
]



@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }



@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")



@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    # Find the next available ID
    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1

    # Create a dictionary
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    # Add it to the tasks list
    tasks.append(new_task)

    # Return the new task
    return new_task


@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
    for t in tasks:
        if t["id"] == id:
            t["title"] = task.title
            t["done"] = task.done
            return t
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")



@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found") 

