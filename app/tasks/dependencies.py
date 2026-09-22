from app.tasks.dao import TasksDAO
from exceptions import TaskIsNotPresentException


async def get_task(task_id: int) -> int:
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise TaskIsNotPresentException()
    return task
