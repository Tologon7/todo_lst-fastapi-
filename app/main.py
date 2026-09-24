from fastapi import FastAPI

from app.tasks.router import router as router_tasks
from app.users.router import router as router_users
from app.users.roles.router import router as router_roles

app = FastAPI()

app.include_router(router_tasks)
app.include_router(router_users)
app.include_router(router_roles)
