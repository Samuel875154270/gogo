import common, model
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
            return result
        else:
            return False

    def get_info(self, email):
        """
        根据email查看用户信息
        :param email:
        :return:
        """
        users = model.Users
        result = users.get(users.email == email)
        model.database.close()

        if result:
            return model_to_dict(result)
        else:
            return False


if __name__ == "__main__":
    params = {
        "name": "小明",
        "email": "xiao@164.com",
        "password": "abc123"
    }
    xx = sUsers().create_new(**params)
    print(xx)
    # yy = sUsers().get_info("xiao@163.com")
    # print(yy)
