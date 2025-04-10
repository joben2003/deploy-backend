from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Routes for application for users to add their daily task updates by our team which will have crud operations

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/tasks")
def read_tasks():
    return {"tasks": ["task1", "task2", "task3"]}

@app.post("/tasks")
def create_task(task: str):
    return {"task": task, "status": "created"}

@app.post("/tasks/{task_id}")
def update_task(task_id: int, task: str):
    return {"task_id": task_id, "task": task, "status": "updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return {"task_id": task_id, "status": "deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)