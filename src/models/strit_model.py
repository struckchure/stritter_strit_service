import peewee

from config.db import BaseModel


class StritModel(BaseModel):

    user_id = peewee.UUIDField()
    body = peewee.TextField()

    class Meta:
        table_name = "strits"
