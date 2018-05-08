from .BaseModel import *


class Tasks(BaseModel):
    class Meta:
        db_table = "tasks"

    # 表字段
    id = AutoField(primary_key=True, null=False)  # 用例id
    name = CharField(null=False)  # 任务名称
    host_id = CharField(null=False)  # host的id
    case_ids = CharField(null=False)  # case的id列表
    create_time = DateTimeField(null=True)  # 创建时间
    update_time = DateTimeField(null=True)  # 修改时间
