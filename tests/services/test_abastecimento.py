
from decimal import Decimal, getcontext

from app.schemas.enums import TipoCombustivel
from app.services.abastecimento import is_improper_data as anomalia
from app.services.abastecimento import media_mock

getcontext().prec = 3 #Igual utilizado pelo server

#Um valor abaixo na precisão
def decimal_abaixo(dec: Decimal):
    return dec - Decimal("0.01")


def test_regra_improper_data():

    perc: Decimal = Decimal("1.25")


    #Listagem por resultado esperado

    #Testa valores superiores e iguais a 125%
    test_improper_data: list[bool] = [
            anomalia(Decimal(10.00), TipoCombustivel.GASOLINA),
            anomalia(
                media_mock[TipoCombustivel.GASOLINA] * perc,
                TipoCombustivel.GASOLINA
                ),

            anomalia(Decimal(15.00), TipoCombustivel.DIESEL),
            anomalia(
                media_mock[TipoCombustivel.DIESEL] * perc,
                TipoCombustivel.DIESEL
                ),

            anomalia(Decimal(12.00), TipoCombustivel.ETANOL),
            anomalia(
                media_mock[TipoCombustivel.ETANOL] * perc,
                TipoCombustivel.ETANOL
                ),

            ]

    #Testa valores menores que 125%
    #Testa valores da precisão 2 mais próximos de 125%
    test_not_improper_data: list[bool] = [
            anomalia(Decimal(6.00), TipoCombustivel.GASOLINA),
            anomalia(
                decimal_abaixo(media_mock[TipoCombustivel.GASOLINA] * perc),
                TipoCombustivel.GASOLINA
                ),

            anomalia(Decimal(6.50), TipoCombustivel.DIESEL),
            anomalia(
                decimal_abaixo(media_mock[TipoCombustivel.DIESEL] * perc),
                TipoCombustivel.DIESEL
                ),

            anomalia(Decimal(4.20), TipoCombustivel.ETANOL),
            anomalia(
                decimal_abaixo(media_mock[TipoCombustivel.ETANOL] * perc),
                TipoCombustivel.ETANOL
                ),

            ]

    #Checkagem dos resultados dos testes
    for t in test_improper_data:
        assert (t)

    for t in test_not_improper_data:
        assert (not t)




