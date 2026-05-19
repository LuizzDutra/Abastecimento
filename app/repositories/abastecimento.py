from typing import Optional

from sqlalchemy import select

from app.core.db import SessionDep
from app.models.abastecimento import Abastecimento
from app.schemas.enums import TipoCombustivel
from app.schemas.filtro import DataRange
from app.schemas.paginacao import ParametrosPaginacao


async def add_db(session: SessionDep, instance: Abastecimento) -> Abastecimento:
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


def base_query():
    return select(Abastecimento).order_by(Abastecimento.id)


async def dados_abastecimentos(session: SessionDep,
                               paginacao: ParametrosPaginacao,
                               tipo_combustivel: Optional[TipoCombustivel],
                               data_range: DataRange
                               ):

    query = base_query()

    return (await session.execute(query)).scalars().all()


