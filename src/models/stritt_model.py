import peewee

from config.db import BaseModel


class StrittModel(BaseModel):

    user_id = peewee.UUIDField()
    body = peewee.TextField()

    class Meta:
        table_name = "stritts"
