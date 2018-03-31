from peewee import *
from .DbConnection import database


class BaseModel(Model):
    class Meta:
        database = database
