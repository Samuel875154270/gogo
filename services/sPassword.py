import common, model, error
from common.encode import decode_password, encode_password
from playhouse.shortcuts import model_to_dict


class sPassword():

    def check(self, **kwargs):
        """
        获取用户密码
        :param kwargs:
        :return:
        """
        users = model.Users
        result = users.select(users.password).where((users.email == kwargs["email"])).dicts()
        for item in result:
            password = item["password"]
        model.database.close()

        if password:
            return decode_password(password)
        else:
            return False


    def update_password(self, **kwargs):
        """
        修改用户密码
        :param id:
        :param kwargs:
        :return:
        """
        kwargs["update_time"] = common.get_time_now()
        kwargs["password"] = encode_password(kwargs["password"])
        email = kwargs["email"]
        del kwargs["email"]
        try:
            users = model.Users
            result = users.update(**kwargs).where((users.email == email)).execute()
            return result
        except Exception:
            model.database.rollback()
            raise error.Database(error.data_save_error, error.get_error_message(error.data_save_error))
