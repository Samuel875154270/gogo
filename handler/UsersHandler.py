import tornado.httpclient
import peewee
import exceptions
import validate, error
from playhouse.shortcuts import model_to_dict
from .BaseHandler import BaseHandler
from services.sUsers import sUsers


class IndexHandler(BaseHandler):
    def get(self):
        self.echoSuccess()

class UsersHandler(BaseHandler):

    service = sUsers()

    @tornado.web.asynchronous
    def get(self, id):
        """
        获取用户信息
        :param id:
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.users_get(self.arguments)
            if id:
                users = self.service.get_info(**self.arguments)
                users = model_to_dict(users)
                self.echoJson(0, users)
            else:
                # 如果没有id,  则获取列表
                users_list, counts = self.service.get_list(**self.arguments)
                self.echoJson(0, {"data": users_list, "totalCounts": counts})
        except error.RequestData as e:
            self.echo_error(e.code, e.message)
        except exceptions.RequestData as e:
            self.echoJson(e.code, e.message)
        except peewee.DoesNotExist:
            self.echoJson()
        except Exception as e:
            self.echoJson(exceptions.exception, str(e))
        self.close_connect_and_finish()

    @tornado.web.asynchronous
    def post(self, param):
        """
        创建用户
        :param param:
        :return:
        """
        try:
            validate.users_create(self.arguments)
            users = self.service.create_new(**self.arguments)
            if users is False or users is 0:
                raise exceptions.Database(exceptions.data_save_error, exceptions.get_error_message(exceptions.data_save_error))
            self.echoJson(0, users)
        except error.RequestData as e:
            self.echo_error(e.code, e.message)
        except exceptions.RequestData as e:
            self.echoJson(e.code, e.message)
        except peewee.IntegrityError as e:
            self.echoJson(exceptions.data_integrity_error, str(e))
        except exceptions.Database as e:
            self.echoJson(e.code, e.message)
        except Exception as e:
            self.echoJson(exceptions.exception, str(e))
        self.close_connect_and_finish()

    @tornado.web.asynchronous
    def put(self, id):
        """
        更新用户
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.users_update(self.arguments)
            del self.arguments['id']
            users = self.service.update(id, **self.arguments)
            if users is False or users is 0:
                raise peewee.DoesNotExist(exceptions.data_not_existed, exceptions.get_error_message(exceptions.data_not_existed))
            self.echoJson(0, {"info": "success"})
        except error.RequestData as e:
            self.echo_error(e.code, e.message)
        except peewee.DoesNotExist:
            self.echoJson(exceptions.data_not_existed, exceptions.get_error_message(exceptions.data_not_existed))
        except exceptions.Database as e:
            self.echoJson(e.code, e.message)
        except Exception as e:
            self.echoJson(exceptions.exception, str(e))
        self.close_connect_and_finish()

    @tornado.web.asynchronous
    def delete(self, id):
        """
        删除品种
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.users_delete(self.arguments)
            users = self.service.delete(self.arguments['id'])
            if users is False or users is 0:
                raise peewee.DoesNotExist(exceptions.data_not_existed, exceptions.get_error_message(exceptions.data_not_existed))
            self.echoJson(0, {"info": "success"})
        except error.RequestData as e:
            self.echo_error(e.code, e.message)
        except peewee.DoesNotExist:
            self.echoJson(exceptions.data_not_existed, exceptions.get_error_message(exceptions.data_not_existed))
        except exceptions.Database as e:
            self.echoJson(e.code, e.message)
        except Exception as e:
            self.echoJson(exceptions.exception, str(e))
        self.close_connect_and_finish()
