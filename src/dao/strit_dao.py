import uuid
from datetime import datetime

from config.db import db
from models.strit_model import StritModel
from props.strit_props import StritCreateProps, StritUpdateProps


class StritDAO:
    @staticmethod
    def create_strit(strit_data: StritCreateProps) -> StritModel:
        with db.atomic():
            try:
                return StritModel.create(**strit_data.dict(exclude_none=True))
            except Exception as e:
                raise Exception(str(e))

    @staticmethod
    def list_strit() -> list[StritModel]:
        return StritModel.filter().order_by(StritModel.created_at.desc())

    @staticmethod
    def get_strit(strit_id: uuid.UUID) -> StritModel:
        try:
            return StritModel.get_by_id(strit_id)
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def update_strit(strit_id: uuid.UUID, strit_data: StritUpdateProps) -> int:
        with db.atomic():
            try:
                return (
                    StritModel.update(
                        **strit_data.dict(exclude_none=True),
                        updated_at=datetime.now(),
                    )
                    .where(StritModel.id == strit_id)
                    .execute()
                )
            except Exception as e:
                raise Exception(str(e))

    @staticmethod
    def delete_strit(strit_id: uuid.UUID) -> None:
        try:
            StritModel.delete_by_id(strit_id)
        except Exception as e:
            raise Exception(str(e))
