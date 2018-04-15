import tornado.httpclient
import peewee
import exceptions
import validate, error
from playhouse.shortcuts import model_to_dict
from .BaseHandler import BaseHandler
from services.sCases import sCases


class IndexHandler(BaseHandler):
    def get(self):
        self.echoSuccess()

class CasesHandler(BaseHandler):

    service = sCases()

    @tornado.web.asynchronous
    def get(self, id):
        """
        获取host信息
        :param id:
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.cases_get(self.arguments)
            if id:
                cases = self.service.get_info(**self.arguments)
                cases = model_to_dict(cases)
                self.echoJson(0, {"info": cases})
            else:
                # 如果没有id,  则获取列表
                cases_list, counts = self.service.get_list(**self.arguments)
                self.echoJson(0, {"info": cases_list, "totalCounts": counts})
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
        创建host
        :param param:
        :return:
        """
        try:
            validate.cases_create(self.arguments)
            cases = self.service.create_new(**self.arguments)
            if cases is False or cases is 0:
                raise exceptions.Database(exceptions.data_save_error, exceptions.get_error_message(exceptions.data_save_error))
            self.echoJson(0, cases)
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
        更新host
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.cases_update(self.arguments)
            del self.arguments['id']
            cases = self.service.update(id, **self.arguments)
            if cases is False or cases is 0:
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
        删除host
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.cases_delete(self.arguments)
            cases = self.service.delete(self.arguments['id'])
            if cases is False or cases is 0:
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
        except error.Database as e:
            self.echoJson(e.code, e.message)
        self.close_connect_and_finish()
