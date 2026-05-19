from typing import Optional

from fastapi import APIRouter, Depends, status

from app.core.db import SessionDep
from app.models.abastecimento import Abastecimento
from app.repositories.abastecimento import add_db, dados_abastecimentos
from app.schemas.abastecimento import AbastecimentoModel, AbastecimentoSchema
from app.schemas.enums import TipoCombustivel
from app.schemas.filtro import DataRange, check_date
from app.schemas.paginacao import ParametrosPaginacao, ResultadoPaginado
from app.services.abastecimento import is_improper_data

router = APIRouter(prefix="/abastecimentos")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_abastecimentos(session: SessionDep, dados: AbastecimentoSchema):

    improper_data = is_improper_data(dados.preco_por_litro, dados.tipo_combustivel)

    dados_instance = Abastecimento(**dados.model_dump(), improper_data=improper_data)
    dados_instance = await add_db(session, dados_instance)

    return AbastecimentoModel.model_validate(dados_instance)


@router.get("/")
async def get_abastecimentos(
    session: SessionDep,
    data: DataRange = Depends(check_date),
    paginacao: ParametrosPaginacao = Depends(),
    tipo_combustivel: Optional[TipoCombustivel] = None,
) -> ResultadoPaginado[AbastecimentoModel]:

    result = await dados_abastecimentos(session, paginacao, tipo_combustivel, data)
    result = [AbastecimentoModel.model_validate(m) for m in result]

    return ResultadoPaginado(
        total=len(result), page=paginacao.page, size=paginacao.size, data=result
    )
