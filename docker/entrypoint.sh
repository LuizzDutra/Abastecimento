#!/bin/sh

echo "Running database migrations..."
alembic upgrade head

echo "Running FastAPI"
uvicorn app.main:app --host 0.0.0.0 --port 80
