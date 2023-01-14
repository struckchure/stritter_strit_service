import typing
import uuid
from datetime import datetime

import pydantic


class StrittObject(typing.TypedDict):

    id: uuid.UUID
    user_id: uuid.UUID
    body: str
    created_at: datetime
    updated_at: datetime


class StrittProps(pydantic.BaseModel):

    user_id: uuid.UUID
    body: str


class StrittCreateProps(StrittProps):
    pass


class StrittUpdateProps(pydantic.BaseModel):

    body: typing.Optional[str]
