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
