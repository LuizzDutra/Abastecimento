FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

ENV PATH="/app/.venv/bin:$PATH"

RUN uv sync --frozen --no-cache


COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini ./
COPY docker/entrypoint.sh ./

EXPOSE 80
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
