from fastapi import FastAPI

from app.tasks.router import router as router_tasks

app = FastAPI()

app.include_router(router_tasks)


@app.get("/")
def say_hello():
    return {"say": "hello"}
