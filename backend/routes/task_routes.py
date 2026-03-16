from fastapi import APIRouter

router = APIRouter(prefix="/tasks")

tasks = []

@router.post("/")
def create_task(task_type: str):
    task = {
        "id": len(tasks) + 1,
        "task_type": task_type,
        "status": "pending"
    }

    tasks.append(task)

    return {"message": "Task created", "task": task}


@router.get("/")
def get_tasks():
    return {"tasks": tasks}