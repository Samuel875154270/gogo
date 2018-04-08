import common, model, error
from common.encode import encode_password
from playhouse.shortcuts import model_to_dict


class sHosts():

    def create_new(self, **kwargs):
        """
        创建host
        :param kwargs:
        :return:
        """
        # 第3种写法，只返回主键自增的id
        hosts = model.Hosts()
        params = {}
        for key in kwargs.keys():
            params[key] = kwargs[key]
        params["create_time"] = common.get_time_now()
        params["update_time"] = common.get_time_now()
        result = hosts.insert(**params).execute()
        model.database.close()
        if result:
            return {"id": result}
        else:
            return False

    def get_info(self, **kwargs):
        """
        获取host信息
        :param kwargs:
        :return:
        """
        hosts = model.Hosts
        result = hosts.get((hosts.id == kwargs["id"]))
        model.database.close()

        if result:
            return result
        else:
            return False

    def get_list(self, **kwargs):
        """
        获取host列表
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

        host = kwargs.get("host")
        name = kwargs.get("name")
        app_id = kwargs.get("app_id")

        hosts = model.Hosts
        if host:
            condition1 = (hosts.host % "%{}%".format(host))
        else:
            condition1 = True
        if name:
            condition2 = (hosts.name % "%{}%".format(name))
        else:
            condition2 = True
        if app_id:
            condition3 = (hosts.app_id == app_id)
        else:
            condition3 = True
        hosts_list = []
        for item in hosts.select().order_by(hosts.create_time.desc()).paginate(page, pagesize).where(
                condition1 & condition2  & condition3).dicts():
            hosts_list.append(item)
            model.database.close()
        total_count = hosts.select().where(condition1 & condition2 & condition3).count()
        model.database.close()

        return hosts_list, total_count

    def update(self, id, **kwargs):
        """
        修改host信息
        :param id:
        :param kwargs:
        :return:
        """
        kwargs["update_time"] = common.get_time_now()
        try:
            hosts = model.Hosts
            hosts_update = hosts.update(**kwargs).where((hosts.id == id)).execute()
            return hosts_update
        except Exception as e:
            model.database.rollback()
            raise error.Database(error.data_save_error, error.get_error_message(error.data_save_error))

    def delete(self, id):
        """
        删除host
        :param id:
        :return:
        """
        try:
            hosts = model.Hosts
            result = hosts.get(hosts.id == id).delete_instance()
            return result
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_delete_error, error.get_error_message(error.data_delete_error))
