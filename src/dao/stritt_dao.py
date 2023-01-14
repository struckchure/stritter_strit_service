import uuid
from datetime import datetime

from config.db import db
from models.stritt_model import StrittModel
from props.stritt_props import StrittCreateProps, StrittUpdateProps


class StrittDAO:
    @staticmethod
    def create_stritt(stritt_data: StrittCreateProps) -> StrittModel:
        with db.atomic():
            try:
                return StrittModel.create(**stritt_data.dict(exclude_none=True))
            except Exception as e:
                raise Exception(str(e))

    @staticmethod
    def list_stritt() -> list[StrittModel]:
        return StrittModel.filter()

    @staticmethod
    def get_stritt(stritt_id: uuid.UUID) -> StrittModel:
        try:
            return StrittModel.get_by_id(stritt_id)
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def update_stritt(stritt_id: uuid.UUID, stritt_data: StrittUpdateProps) -> int:
        with db.atomic():
            try:
                return (
                    StrittModel.update(
                        **stritt_data.dict(exclude_none=True),
                        updated_at=datetime.now(),
                    )
                    .where(StrittModel.id == stritt_id)
                    .execute()
                )
            except Exception as e:
                raise Exception(str(e))

    @staticmethod
    def delete_stritt(stritt_id: uuid.UUID) -> None:
        try:
            StrittModel.delete_by_id(stritt_id)
        except Exception as e:
            raise Exception(str(e))
