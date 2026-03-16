from fastapi import FastAPI
from routes.task_routes import router as task_router

app = FastAPI(title="Distributed Task Processing Platform")

app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Distributed Task Processing System Running"}