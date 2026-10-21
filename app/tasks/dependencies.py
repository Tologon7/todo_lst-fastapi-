from app.tasks.dao import TasksDAO
from app.exceptions import TaskIsNotPresentException
from app.tasks.models import Tasks


async def get_task(task_id: int) -> Tasks:
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise TaskIsNotPresentException()
    return task
