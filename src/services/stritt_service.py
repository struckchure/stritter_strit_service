import uuid

from fastapi import HTTPException

from dao.stritt_dao import StrittDAO
from props.stritt_props import StrittCreateProps, StrittObject, StrittUpdateProps


class StrittService:
    @staticmethod
    def create_stritt(user_id: uuid.UUID, body: str) -> StrittObject:
        try:
            stritt_data = StrittCreateProps(user_id=user_id, body=body)
            stritt = StrittDAO.create_stritt(stritt_data=stritt_data)

            return StrittObject(
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
    def list_stritt() -> list[StrittObject]:
        try:
            return [
                StrittObject(
                    **{
                        "id": stritt.id,
                        "user_id": stritt.user_id,
                        "body": stritt.body,
                        "created_at": stritt.created_at,
                        "updated_at": stritt.updated_at,
                    }
                )
                for stritt in StrittDAO.list_stritt()
            ]
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_stritt(stritt_id: uuid.UUID) -> StrittObject:
        try:
            stritt = StrittDAO.get_stritt(stritt_id=stritt_id)

            return StrittObject(
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
    def update_stritt(stritt_id: uuid.UUID, body: str) -> StrittObject:
        try:
            stritt_data = StrittUpdateProps(body=body)
            StrittDAO.update_stritt(stritt_id=stritt_id, stritt_data=stritt_data)
            stritt = StrittDAO.get_stritt(stritt_id=stritt_id)

            return StrittObject(
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
    def delete_stritt(stritt_id: uuid.UUID):
        StrittDAO.delete_stritt(stritt_id=stritt_id)
