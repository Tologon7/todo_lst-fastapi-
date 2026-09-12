from fastapi import APIRouter, Query
from app.tasks.dao import TasksDAO
from app.tasks.schemas import STasksCreate
from datetime import date
from typing import Optional

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.get("/all_tasks")
async def show_all_tasks():
    return await TasksDAO.find_all()


@router.post("/add_task")
async def add_new_task(tasks: STasksCreate):
    dump = tasks.model_dump()
    task = await TasksDAO.add(**dump)
