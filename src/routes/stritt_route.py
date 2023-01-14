import uuid

from fastapi import APIRouter

from props.stritt_props import StrittCreateProps, StrittObject, StrittUpdateProps
from services.stritt_service import StrittService

router = APIRouter(prefix="/stritt", tags=["stritt"])


@router.post("/")
def create_stritt_api(stritt_data: StrittCreateProps) -> StrittObject:
    return StrittService.create_stritt(**stritt_data.dict(exclude_none=True))


@router.get("/")
def list_stritt_api() -> list[StrittObject]:
    return StrittService.list_stritt()


@router.get("/{stritt_id}/")
def get_stritt_api(stritt_id: uuid.UUID) -> StrittObject:
    return StrittService.get_stritt(stritt_id=stritt_id)


@router.put("/{stritt_id}/")
def update_stritt_api(
    stritt_id: uuid.UUID, stritt_data: StrittUpdateProps
) -> StrittObject:
    return StrittService.update_stritt(
        stritt_id=stritt_id, **stritt_data.dict(exclude_none=True)
    )


@router.delete("/{stritt_id}/")
def delete_stritt_api(stritt_id: uuid.UUID):
    return StrittService.delete_stritt(stritt_id=stritt_id)
