from typing import Optional, Tuple

from sqlalchemy import Select, func, select

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

def paginate(paginacao: ParametrosPaginacao,
             query: Select[Tuple[Abastecimento]]
             ) -> Select[Tuple[Abastecimento]]:
    return query.limit(paginacao.size).offset((paginacao.page - 1) * paginacao.size)


def filter_combustivel(
    tipo_combustivel: TipoCombustivel, query: Select[Tuple[Abastecimento]]
) -> Select[Tuple[Abastecimento]]:
    return query.where(Abastecimento.tipo_combustivel == tipo_combustivel.value)

def filter_data(
    data_range: DataRange, query: Select[Tuple[Abastecimento]]
) -> Select[Tuple[Abastecimento]]:
    if data_range.data_inicio:
        query = query.where(
                func.date(Abastecimento.data_hora) >= data_range.data_inicio
                )
    if data_range.data_fim:
        query = query.where(
                func.date(Abastecimento.data_hora) <= data_range.data_fim
                )
    return query



async def dados_abastecimentos(session: SessionDep,
                               paginacao: ParametrosPaginacao,
                               tipo_combustivel: Optional[TipoCombustivel],
                               data_range: DataRange
                               ):

    query = base_query()
    query = filter_data(data_range, query)
    if tipo_combustivel:
        query = filter_combustivel(tipo_combustivel, query)

    query = paginate(paginacao, query)

    return (await session.execute(query)).scalars().all()


