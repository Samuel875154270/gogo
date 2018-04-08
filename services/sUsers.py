import common, model, error
from common.encode import encode_password
from playhouse.shortcuts import model_to_dict


class sUsers():

    def create_new(self, **kwargs):
        """
        创建用户
        :param kwargs:
        :return:
        """
        # 第1种写法，主键自增的id为None
        # users = model.Users()
        # users.name = kwargs["name"]
        # users.email = kwargs["email"]
        # users.password = encode_password(kwargs["password"])
        # users.create_time = common.get_time_now()
        # result = users.save(force_insert=True)
        # model.database.close()
        #
        # if result:
        #     return model_to_dict(users)
        # else:
        #     return False
        # 第2种写法，主键自增的id为None
        # users = model.Users
        # params = {}
        # params["name"] = kwargs["name"]
        # params["email"] = kwargs["email"]
        # params["password"] = encode_password(kwargs["password"])
        # params["create_time"] = common.get_time_now()
        # result = users.create(**params)
        # model.database.close()
        # if result:
        #     return model_to_dict(result)
        # else:
        #     return False
        # 第3种写法，只返回主键自增的id
        users = model.Users
        params = {}
        params["name"] = kwargs["name"]
        params["email"] = kwargs["email"]
        params["password"] = encode_password(kwargs["password"])
        params["create_time"] = common.get_time_now()
        result = users.insert(**params).execute()
        model.database.close()
        if result:
            return {"id": result}
        else:
            return False

    def get_info(self, **kwargs):
        """
        获取用户信息
        :param kwargs:
        :return:
        """
        users = model.Users
        result = users.select(users.id, users.name, users.email, users.create_time, users.update_time).where(
            (users.id == kwargs["id"])).dicts()
        model.database.close()

        if result:
            return result
        else:
            return False

    def get_list(self, **kwargs):
        """
        获取用户列表
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

        email = kwargs.get("email")
        name = kwargs.get("name")

        users = model.Users
        if email:
            condition1 = (users.email % "%{}%".format(email))
        else:
            condition1 = True
        if name:
            condition2 = (users.name % "%{}%".format(name))
        else:
            condition2 = True
        users_list = []
        for item in users.select(users.id, users.name, users.email, users.create_time, users.update_time).order_by(
                users.create_time.desc()).paginate(page, pagesize).where(condition1 & condition2).dicts():
            users_list.append(item)
            model.database.close()
        total_count = users.select().where(condition1 & condition2).count()
        model.database.close()

        return users_list, total_count

    def update(self, id, **kwargs):
        """
        修改用户信息
        :param id:
        :param kwargs:
        :return:
        """
        kwargs["update_time"] = common.get_time_now()
        print(kwargs)
        try:
            users = model.Users
            users_update = users.update(**kwargs).where((users.id == id)).execute()
            return users_update
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_save_error, error.get_error_message(error.data_save_error))

    def delete(self, id):
        """
        删除用户
        :param id:
        :return:
        """
        try:
            users = model.Users
            result = users.get(users.id == id).delete_instance()

            return result
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_delete_error, error.get_error_message(error.data_delete_error))
