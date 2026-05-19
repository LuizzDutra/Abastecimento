from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api_router
from app.core.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
