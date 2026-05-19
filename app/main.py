from contextlib import asynccontextmanager

from api import api_router
from fastapi import FastAPI

from server.core.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI()
app.include_router(api_router)
