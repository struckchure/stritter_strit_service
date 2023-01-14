import uuid
from datetime import datetime

import peewee

from config import env

db = peewee.PostgresqlDatabase(
    env.DB_NAME,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    host=env.DB_HOST,
    port=env.DB_PORT,
)


class BaseModel(peewee.Model):

    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = peewee.DateTimeField(default=datetime.now)
    updated_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db
