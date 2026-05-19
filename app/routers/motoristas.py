from fastapi import APIRouter, status

from app.core.db import SessionDep
from app.repositories.motoristas import get_abastecimentos_motorista
from app.schemas.abastecimento import CPF, AbastecimentoModel

router = APIRouter(prefix="/motoristas")


@router.get("/{cpf}/historico", status_code=status.HTTP_200_OK)
async def get_motorista_cpf(cpf: CPF, session: SessionDep) -> list[AbastecimentoModel]:

    result = await get_abastecimentos_motorista(session, cpf)
    result = [AbastecimentoModel.model_validate(m) for m in result]

    return result
