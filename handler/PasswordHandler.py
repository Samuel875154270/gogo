import tornado.httpclient
import peewee
import exceptions
import validate, error
from playhouse.shortcuts import model_to_dict
from .BaseHandler import BaseHandler
from services.sPassword import sPassword
from common.encode import sha1_password


class IndexHandler(BaseHandler):
    def get(self):
        self.echoSuccess()


class PasswordHandler(BaseHandler):
    service = sPassword()

    @tornado.web.asynchronous
    def get(self, email):
        """
        验证用户密码
        :param param:
        :return:
        """
        try:
            validate.check_password(self.arguments)
            password = self.service.check(**self.arguments)
            if password == sha1_password(self.arguments["password"]):
                self.echoJson(0, {"info": "success"})
            else:
                self.echo_error(error.password_error, error.get_error_message(error.password_error))
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
    def put(self, email):
        """
        修改用户密码
        :param email:
        :return:
        """
        try:
            validate.users_update(self.arguments)
            password = self.service.update_password(**self.arguments)
            if password is False or password is 0:
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

