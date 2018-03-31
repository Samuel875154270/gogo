from .BaseModel import *
class Users(BaseModel):
    class Meta:
        db_table = "users"
        unique_key = CompositeKey("user_id")

        uid = CharField