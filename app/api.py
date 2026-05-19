from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text

from app.core.config import config
from app.core.db import SessionDep
from app.routers.abastecimento import router as router_abastecimento
from app.routers.motoristas import router as router_motorista
from app.schemas.api import StatusSchema

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(router_abastecimento)
api_router.include_router(router_motorista)


@api_router.get("/health", status_code=200)
async def health(session: SessionDep):
    db_healthy = True
    try:
        await session.execute(text("SELECT 1"))
    except Exception as e:
        db_healthy = False
        print(f"Teste de conexão com Database falhou: {e}")

    if not db_healthy:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=StatusSchema(
                version=config().VERSION,
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
                database=status.HTTP_503_SERVICE_UNAVAILABLE,
            ).model_dump(),
        )

    return StatusSchema(
        version=config().VERSION, status=status.HTTP_200_OK, database=status.HTTP_200_OK
    )
