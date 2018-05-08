import common, model, error
from common.encode import encode_password
from playhouse.shortcuts import model_to_dict


class sTasks():

    def create_new(self, **kwargs):
        """
        创建task
        :param kwargs:
        :return:
        """
        # 第3种写法，只返回主键自增的id
        tasks = model.Tasks()
        params = {}
        for key in kwargs.keys():
            params[key] = kwargs[key]
        params["create_time"] = common.get_time_now()
        params["update_time"] = common.get_time_now()
        result = tasks.insert(**params).execute()
        model.database.close()
        if result:
            return {"id": result}
        else:
            return False

    def get_info(self, **kwargs):
        """
        获取task信息
        :param kwargs:
        :return:
        """
        tasks = model.Tasks
        result = tasks.get((tasks.id == kwargs["id"]))
        model.database.close()

        if result:
            return result
        else:
            return False

    def get_list(self, **kwargs):
        """
        获取task列表
        :param kwargs:
        :return:
        """
        page = kwargs.get("page")
        if page:
            page = int(page)
        else:
            page = 1
        pagesize = kwargs.get("pagesize")
        if pagesize:
            pagesize = int(pagesize)
        else:
            pagesize = 20

        host_id = kwargs.get("host_id")
        name = kwargs.get("name")

        tasks = model.Tasks
        if host_id:
            condition1 = (tasks.host_id == host_id)
        else:
            condition1 = True
        if name:
            condition2 = (tasks.name % "%{}%".format(name))
        else:
            condition2 = True
        tasks_list = []
        for item in tasks.select().order_by(tasks.create_time.desc()).paginate(page, pagesize).where(
                condition1 & condition2).dicts():
            tasks_list.append(item)
            model.database.close()
        total_count = tasks.select().where(condition1 & condition2).count()
        model.database.close()

        return tasks_list, total_count

    def update(self, id, **kwargs):
        """
        修改task信息
        :param id:
        :param kwargs:
        :return:
        """
        kwargs["update_time"] = common.get_time_now()
        try:
            tasks = model.Tasks
            tasks_update = tasks.update(**kwargs).where((tasks.id == id)).execute()
            return tasks_update
        except Exception as e:
            model.database.rollback()
            raise error.Database(error.data_save_error, error.get_error_message(error.data_save_error))

    def delete(self, id):
        """
        删除task
        :param id:
        :return:
        """
        try:
            tasks = model.Tasks
            result = tasks.get(tasks.id == id).delete_instance()
            return result
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_delete_error, error.get_error_message(error.data_delete_error))
