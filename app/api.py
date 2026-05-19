from fastapi import APIRouter

from app.routers.abastecimento import router as router_abastecimento

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(router_abastecimento)




@api_router.get("/health", status_code=200)
async def health():
    return {"status": "ok"}
