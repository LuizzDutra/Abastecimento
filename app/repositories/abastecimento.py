from app.core.db import SessionDep
from app.models.abastecimento import Abastecimento


async def add_db(session: SessionDep, instance: Abastecimento) -> Abastecimento:
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance
