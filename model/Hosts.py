from .BaseModel import *


class Hosts(BaseModel):
    class Meta:
        db_table = "hosts"
        unique_key = CompositeKey("id")

    # 表字段
    id = AutoField(primary_key=True, null=False)  # id
    host = CharField(null=False)  # host地址
    name = CharField(null=False)  # 名称
    app_id = CharField(null=True)  # app_id
    app_secret = CharField(null=True)  # app_secret
    create_time = DateTimeField(null=True)  # 创建时间
    update_time = DateTimeField(null=True)  # 修改时间
    remark = CharField(null=True)  # 备注
