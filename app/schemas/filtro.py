

from datetime import date
from typing import Optional

from fastapi import HTTPException, Query


class DataRange:
    def __init__(self,
        data_inicio: Optional[date] = Query(None),
        data_fim: Optional[date] = Query(None)
                 ):
        self.data_inicio = data_inicio
        self.data_fim = data_fim


def check_date(data_inicio: Optional[date] = Query(None),
        data_fim: Optional[date] = Query(None)) -> DataRange:

    if (data_inicio and not data_fim) or (data_fim and not data_inicio):
        raise HTTPException(
                status_code=422,
                detail="É necessário data_inicio e data_fim juntos"
                )

    if (data_inicio and data_fim) and data_inicio > data_fim:
         raise HTTPException(
                status_code=422,
                detail="data_inicio não pode ser maior que data_fim"
                )




    return DataRange(data_inicio, data_fim)

