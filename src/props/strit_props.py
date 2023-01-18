import typing
import uuid
from datetime import datetime

import pydantic


class StritObject(typing.TypedDict):

    id: uuid.UUID
    user_id: uuid.UUID
    body: str
    created_at: datetime
    updated_at: datetime


class StritProps(pydantic.BaseModel):

    user_id: uuid.UUID
    body: str


class StritCreateProps(StritProps):
    pass


class StritUpdateProps(pydantic.BaseModel):

    body: typing.Optional[str]
