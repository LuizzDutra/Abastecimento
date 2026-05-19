from fastapi import APIRouter

from app.routers.abastecimento import router as router_abastecimento
from app.routers.motoristas import router as router_motorista

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(router_abastecimento)
api_router.include_router(router_motorista)



@api_router.get("/health", status_code=200)
async def health():
    return {"status": "ok"}
