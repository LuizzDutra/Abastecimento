from typing import Generic, TypeVar

from fastapi import Query
from pydantic import BaseModel


class ParametrosPaginacao:
    def __init__(
        self, size: int = Query(20, gt=0, le=100), page: int = Query(1, gt=0)
    ):
        self.size = size
        self.page = page


T = TypeVar("T")


class ResultadoPaginado(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    data: list[T]
