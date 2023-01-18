import uuid

from fastapi import HTTPException

from dao.strit_dao import StritDAO
from props.strit_props import StritCreateProps, StritObject, StritUpdateProps


class StritService:
    @staticmethod
    def create_strit(user_id: uuid.UUID, body: str) -> StritObject:
        try:
            stritt_data = StritCreateProps(user_id=user_id, body=body)
            stritt = StritDAO.create_strit(strit_data=stritt_data)

            return StritObject(
                **{
                    "id": stritt.id,
                    "user_id": stritt.user_id,
                    "body": stritt.body,
                    "created_at": stritt.created_at,
                    "updated_at": stritt.updated_at,
                }
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def list_strit() -> list[StritObject]:
        try:
            return [
                StritObject(
                    **{
                        "id": stritt.id,
                        "user_id": stritt.user_id,
                        "body": stritt.body,
                        "created_at": stritt.created_at,
                        "updated_at": stritt.updated_at,
                    }
                )
                for stritt in StritDAO.list_strit()
            ]
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_strit(strit_id: uuid.UUID) -> StritObject:
        try:
            stritt = StritDAO.get_strit(strit_id=strit_id)

            return StritObject(
                **{
                    "id": stritt.id,
                    "user_id": stritt.user_id,
                    "body": stritt.body,
                    "created_at": stritt.created_at,
                    "updated_at": stritt.updated_at,
                }
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_strit(strit_id: uuid.UUID, body: str) -> StritObject:
        try:
            strit_data = StritUpdateProps(body=body)
            StritDAO.update_strit(strit_id=strit_id, strit_data=strit_data)
            strit = StritDAO.get_strit(strit_id=strit_id)

            return StritObject(
                **{
                    "id": strit.id,
                    "user_id": strit.user_id,
                    "body": strit.body,
                    "created_at": strit.created_at,
                    "updated_at": strit.updated_at,
                }
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_strit(strit_id: uuid.UUID):
        StritDAO.delete_strit(strit_id=strit_id)
