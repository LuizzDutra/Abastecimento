from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
