from fastapi import APIRouter, Depends

from app.tasks.dao import TasksDAO
from app.tasks.schemas import STasksCreate, STasksShowAll, STasksDetailShow
from app.tasks.models import Tasks
from app.tasks.dependencies import get_task

from app.users.models import Users
from app.users.dependencies import get_current_user

from app.exceptions import TaskIsNotPresentException

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.get("/all_tasks")
async def show_all_tasks(user: Users = Depends(get_current_user)) -> list[STasksShowAll]:
    result = await TasksDAO.find_all()
    if not result:
        raise TaskIsNotPresentException()
    return result


@router.get("/detail_show/{task_id}")
async def detail_show_by_id(user: Users = Depends(get_current_user), task: Tasks = Depends(get_task)) -> STasksDetailShow:
    return task


@router.post("/add_task")
async def add_new_task(tasks: STasksCreate):
    dump = tasks.model_dump()
    await TasksDAO.add(**dump)


@router.delete("/task_delete/{task_id}")
async def task_delete(task: Tasks = Depends(get_task)):
    await TasksDAO.delete_by_id(task.id)
