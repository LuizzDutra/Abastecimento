from datetime import datetime, timezone
from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, field_validator

from app.core.validators.cpf import validate as cpf_validator
from app.schemas.enums import TipoCombustivel

CPF = Annotated[str, AfterValidator(cpf_validator)]

class AbastecimentoSchema(BaseModel):
    id_posto: int
    data_hora: datetime
    tipo_combustivel: TipoCombustivel
    preco_por_litro: Decimal = Field(gt=0)
    volume_abastecido: Decimal = Field(gt=0)
    cpf_motorista: CPF

    @field_validator("data_hora")
    @classmethod
    def data_hora_nao_pode_ser_futura(cls, data: datetime) -> datetime:
        if data.tzinfo is None:
            #Sem timezone é aplicado UTC
            data = data.replace(tzinfo=timezone.utc)
        if data > datetime.now(timezone.utc):
            raise ValueError("data_hora não pode ser no futuro")
        return data.astimezone(timezone.utc)


class AbastecimentoModel(AbastecimentoSchema):
    id: int
    improper_data: bool

    model_config = ConfigDict(from_attributes=True)
