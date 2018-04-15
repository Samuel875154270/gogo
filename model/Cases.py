from .BaseModel import *


class Cases(BaseModel):
    class Meta:
        db_table = "cases"

    # 表字段
    id = AutoField(primary_key=True, null=False)  # 用例id
    name = CharField(null=False)  # 用例名称
    api = CharField(null=False)  # api
    method = CharField(null=False)  # api的请求方式
    headers = CharField(null=True)  # 请求headers
    params_type = CharField(null=True)  # 参数请求方式，json或者form
    params = CharField(null=True)  # 参数
    check_result = CharField(null=True)  # 结果截取点
    result = CharField(null=True)  # 截取的结果
    relation_id = IntegerField(null=True)  # 关联的case_id
    create_time = DateTimeField(null=True)  # 创建时间
    update_time = DateTimeField(null=True)  # 修改时间
