from fastapi import FastAPI
import uuid

app = FastAPI()

tasks = []

@app.post("/tasks")
def create_task():
    task_id = str(uuid.uuid4())
    tasks.append(task_id)
    return {"task_id": task_id, "status": "queued"}

@app.get("/tasks")
def list_tasks():
    return {"tasks": tasks}
