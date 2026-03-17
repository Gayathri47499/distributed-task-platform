from fastapi import FastAPI
from routes.task_routes import router as task_router
from database import engine
from models.task_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Task Processing Platform")

app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Distributed Task Processing System Running"}