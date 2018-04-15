from .BaseModel import *


class Users(BaseModel):
    class Meta:
        db_table = "users"
        unique_key = CompositeKey("id", "email")

    # 表字段
    id = AutoField(primary_key=True, null=False)  # 用户id
    name = CharField(null=False)  # 用户名称
    email = CharField(unique=True, null=False)  # 用户邮箱
    password = CharField(null=False)  # 用户密码
    create_time = DateTimeField(null=True)  # 创建时间
    update_time = DateTimeField(null=True)  # 修改时间
