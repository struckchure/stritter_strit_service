from fastapi import APIRouter

from routes import strit_route

router = APIRouter(prefix="/api/v1")

router.include_router(strit_route.router)
