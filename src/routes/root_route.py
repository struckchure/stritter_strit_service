from fastapi import APIRouter

from routes import stritt_route

router = APIRouter(prefix="/api/v1")

router.include_router(stritt_route.router)
