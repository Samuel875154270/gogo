import common, model, error
from common.encode import encode_password
from playhouse.shortcuts import model_to_dict


class sCases():

    def create_new(self, **kwargs):
        """
        创建case
        :param kwargs:
        :return:
        """
        cases = model.Cases
        kwargs["create_time"] = common.get_time_now()
        kwargs["update_time"] = common.get_time_now()
        result = cases.create(**kwargs)
        model.database.close()
        print(model_to_dict(result))
        if result:
             return model_to_dict(result)
        else:
            return False


    def get_info(self, **kwargs):
        """
        获取case信息
        :param kwargs:
        :return:
        """
        cases = model.Cases
        result = cases.get((cases.id == kwargs["id"]))
        model.database.close()

        if result:
            return result
        else:
            return False

    def get_list(self, **kwargs):
        """
        获取case列表
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

        method = kwargs.get("method")
        name = kwargs.get("name")
        api = kwargs.get("api")

        cases = model.Cases
        if method:
            condition1 = (cases.method % "%{}%".format(method))
        else:
            condition1 = True
        if name:
            condition2 = (cases.name % "%{}%".format(name))
        else:
            condition2 = True
        if api:
            condition3 = (cases.api % "%{}%".format(api))
        else:
            condition3 = True
        cases_list = []
        for item in cases.select().order_by(cases.create_time.desc()).paginate(page, pagesize).where(
                condition1 & condition2  & condition3).dicts():
            cases_list.append(item)
            model.database.close()
        total_count = cases.select().where(condition1 & condition2 & condition3).count()
        model.database.close()

        return cases_list, total_count

    def update(self, id, **kwargs):
        """
        修改case信息
        :param id:
        :param kwargs:
        :return:
        """
        kwargs["update_time"] = common.get_time_now()
        try:
            cases = model.Cases
            cases_update = cases.update(**kwargs).where((cases.id == id)).execute()
            return cases_update
        except Exception as e:
            model.database.rollback()
            raise error.Database(error.data_save_error, error.get_error_message(error.data_save_error))

    def delete(self, id):
        """
        删除case
        :param id:
        :return:
        """
        try:
            cases = model.Cases
            result = cases.get(cases.id == id).delete_instance()
            return result
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_delete_error, error.get_error_message(error.data_delete_error))
