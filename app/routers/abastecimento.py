from typing import Optional

from fastapi import APIRouter, Depends

from app.core.db import SessionDep
from app.schemas.enums import TipoCombustivel
from app.schemas.filtro import DataRange, check_date
from app.schemas.paginacao import ParametrosPaginacao

router = APIRouter(prefix="/abastecimentos")



@router.get("/")
def get_abastecimentos(session: SessionDep,
                       data: DataRange = Depends(check_date),
                       paginacao: ParametrosPaginacao = Depends(),
                       tipo_combustivel: Optional[TipoCombustivel] = None

                       ):


    return "ok"


