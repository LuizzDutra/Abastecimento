from typing import Tuple

from sqlalchemy import Select, select

from app.core.db import SessionDep
from app.models.abastecimento import Abastecimento
from app.schemas.abastecimento import CPF


def filter_motorista(
    cpf_motorista: CPF, query: Select[Tuple[Abastecimento]]
) -> Select[Tuple[Abastecimento]]:
    return query.where(Abastecimento.cpf_motorista == cpf_motorista)


async def get_abastecimentos_motorista(session: SessionDep, cpf: CPF):
    query = select(Abastecimento).order_by(Abastecimento.id)
    query = filter_motorista(cpf, query)

    return (await session.execute(query)).scalars().all()
