from enum import Enum


class TipoCombustivel(str, Enum):
    GASOLINA = "gasolina"
    DIESEL = "diesel"
    ETANOL = "etanol"
