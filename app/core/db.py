from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from server.core.config import config


db_url = config().DB_URL

engine = create_async_engine(db_url, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
