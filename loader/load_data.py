import asyncio
from time import perf_counter

import aiohttp
from faker import Faker

from loader.config import Config

fake = Faker("pt-BR")

API_URL = Config().API_URL

headers = {"Content-Type": "application/json"}

valores_combustivel = ["gasolina", "etanol", "diesel"]


def gerar_payload():
    return {
        "id_posto": fake.random_int(0, 999),
        "data_hora": fake.date_time_this_decade(after_now=False).isoformat(),
        "tipo_combustivel": fake.random_choices(valores_combustivel, 1)[0],
        "preco_por_litro": str(fake.pydecimal(
            left_digits=1,
            right_digits=2,
            min_value=1,
            max_value=10)),
        "volume_abastecido": str(fake.pydecimal(
            left_digits=5,
            right_digits=3,
            min_value=15000,
            max_value=25000
            )),
        "cpf_motorista": fake.ssn(),
    }


async def enviar_payload(session, payload: dict, do_print: bool):
    # Realiza os requests com a sessão e printa status e erros
    try:
        async with session.post(API_URL, headers=headers, json=payload) as response:
            if do_print:
                if response.status in [200, 201]:
                    print("Success. Server response:")
                    print(await response.text())
                if response.status == 422:
                    print("Validation Error. Server Response")
                    print(await response.text())
                if response.status == 501:
                    print("Internal Server Error")
    except Exception as e:
        print(f"An error ocurred: {e}")


async def main():
    r = Config().REQUEST_QTT
    do_print = Config().PRINT
    async with aiohttp.ClientSession() as session:
        # Criação das requests de forma assíncrona
        tasks = []
        for _ in range(r):
            tasks.append(enviar_payload(session, gerar_payload(), do_print))

        start = perf_counter()
        await asyncio.gather(*tasks)
        end = perf_counter()

        print(
            f"O gather de requests durou {end - start} segundos para {r} requisições",
            flush=True
            )

if __name__ == "__main__":
   asyncio.run(main()) 
