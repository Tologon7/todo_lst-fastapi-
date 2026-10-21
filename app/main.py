from fastapi import FastAPI
import uvicorn

from app.tasks.router import router as router_tasks
from app.users.router import router as router_users
from app.users.roles.router import router as router_roles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_tasks)
app.include_router(router_users)
app.include_router(router_roles)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True, workers=3)
