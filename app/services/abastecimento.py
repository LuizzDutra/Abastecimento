from decimal import Decimal

from app.schemas.enums import TipoCombustivel

media_mock = {
        TipoCombustivel.GASOLINA: Decimal(6.00),
        TipoCombustivel.ETANOL: Decimal(4.20),
        TipoCombustivel.DIESEL: Decimal(6.50),
        }

def is_improper_data(preco: Decimal, tipo: TipoCombustivel):
    return preco > (media_mock[tipo] * Decimal(1.25))
