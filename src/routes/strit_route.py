import uuid

from fastapi import APIRouter

from props.strit_props import StritCreateProps, StritObject, StritUpdateProps
from services.strit_service import StritService

router = APIRouter(prefix="/strit", tags=["strit"])


@router.post("/")
def create_strit_api(stritt_data: StritCreateProps) -> StritObject:
    return StritService.create_strit(**stritt_data.dict(exclude_none=True))


@router.get("/")
def list_strit_api() -> list[StritObject]:
    return StritService.list_strit()


@router.get("/{strit_id}/")
def get_strit_api(strit_id: uuid.UUID) -> StritObject:
    return StritService.get_strit(strit_id=strit_id)


@router.put("/{strit_id}/")
def update_strit_api(strit_id: uuid.UUID, stritt_data: StritUpdateProps) -> StritObject:
    return StritService.update_strit(
        strit_id=strit_id, **stritt_data.dict(exclude_none=True)
    )


@router.delete("/{strit_id}/")
def delete_strit_api(strit_id: uuid.UUID):
    return StritService.delete_strit(strit_id=strit_id)
