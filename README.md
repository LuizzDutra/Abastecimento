# API Abastecimento

> API gateway MVP para desafio técnico VLAB

---

## Requirements

- [Docker](https://www.docker.com/) >= 24.x & [Docker Compose](https://docs.docker.com/compose/) >= 2.x
- [UV](https://docs.astral.sh/uv/) >= 0.4.x *(local development only)*

---

## Variáveis de Ambiente

```bash
cp .env.example .app/.env
```


```env
# .env.example
LOCAL_DB_URL="postgresql+asyncpg://username:password@db:5433/database"
DB_URL="postgresql+asyncpg://username:password@db:5432/database"
VERSION="V1.0.0"
```



# Postgres

```bash
cp docker/postgres/.env.example .docker/postgres/.env
```

```env
# .env.example
POSTGRES_PASSWORD="PASSWORD"
POSTGRES_DB="DATABASE"
POSTGRES_USER="USER"
```
---

## Rodando com Docker

O cwd dever ser o ./docker
```bash
cd /docker 
```

```bash
docker compose up --build        # Build and start
docker compose up --build -d     # Detached mode
docker compose down              # Stop services
docker compose down -v           # Stop and remove volumes
docker compose logs -f api       # View logs
```

---

## Running Locally

```bash
uv sync                                                          # Install dependencies
uv run fastapi dev app/main.py                                   # Development server
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload # Custom host/port
```

---

## API Docs

| Interface  | URL                         |
|------------|-----------------------------|
| Swagger UI | http://localhost:port/docs  |

## Alembic

O Alembic está configurado para criar migrações e as executa automaticamente no docker/entrypoint.sh

## Faker

Ajuste o ambiente em loader/config.py or loader/.env as needed

```
uv run -m loader.load_data
```

## Ruff

Ruff está configurado, comandos relevantes:

```
uv run ruff check
```

```
uv run ruff format
```

## Pytest

Para realizar os teste do pytest execute

```
uv run -m pytest
```


## Decisões e Trade-offs

O projeto foi contruído seguindo um arquitetura em camadas como definido no documento de instruções.

**Como decisão:** <br>
Ao realizar a query get do endpoints /abastecimentos, os resultados sempre são order_by id.<br>
Na root do app o arquivo api.py define a junção de todos os routers de /routers e define o endpoint /health<br>
Para o endpoint /health foi realizada uma query SELECT 1 para definir o status do banco de dados e returna estado 503 caso haja algum problema.<br>
Os valores de preço possuem duas casas decimais e os valores de volume abastecido possuem 3 para contemplar o formato Litros.mililitros<br>

**Como trade-offs:** <br>
Para acelerar o processo de criação os campos Decimais aceitam valores number e não apenas strings numéricas, permitindo perca de precisão em alguns casos antes de chegar ao validador.<br>
A média de preço é definidade de meio "hardcoded" como um dict, ao invés de serem cálculadas no banco e salvas em um cache ou usem de referência valores externos.<br>

