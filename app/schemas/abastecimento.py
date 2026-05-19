from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field

from app.core.validators.cpf import validate as cpf_validator
from app.schemas.enums import TipoCombustivel

CPF = Annotated[str, AfterValidator(cpf_validator)]

class AbastecimentoSchema(BaseModel):
    id_post: int
    data_hora: datetime = Field(le=datetime.now())
    tipo_combustivel: TipoCombustivel
    preco_por_litro: Decimal = Field(gt=0)
    volume_abastecido: Decimal = Field(gt=0)
    cpf_motorista: CPF


