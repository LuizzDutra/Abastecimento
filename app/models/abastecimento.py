from datetime import datetime

from sqlalchemy import DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.schemas.enums import TipoCombustivel


class Abastecimento(Base):
    __tablename__ = "abastecimento"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_posto: Mapped[int] = mapped_column(nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    tipo_combustivel: Mapped[TipoCombustivel] = mapped_column(nullable=False)
    preco_por_litro: Mapped[Numeric] = mapped_column(Numeric(scale=2),nullable=False)
    volume_abastecido: Mapped[Numeric] = mapped_column(Numeric(scale=3),nullable=False)
    cpf_motorista: Mapped[str] = mapped_column(nullable=False)

    improper_data: Mapped[bool] = mapped_column(nullable=False)



