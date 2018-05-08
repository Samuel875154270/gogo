import tornado.httpclient
import peewee
import exceptions
import validate, error
from playhouse.shortcuts import model_to_dict
from .BaseHandler import BaseHandler
from services.sTasks import sTasks


class IndexHandler(BaseHandler):
    def get(self):
        self.echoSuccess()


class TasksHandler(BaseHandler):
    service = sTasks()

    @tornado.web.asynchronous
    def get(self, id):
        """
        获取task信息
        :param id:
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.tasks_get(self.arguments)
            if id:
                tasks = self.service.get_info(**self.arguments)
                tasks = model_to_dict(tasks)
                self.echoJson(0, {"info": tasks})
            else:
                # 如果没有id,  则获取列表
                tasks_list, counts = self.service.get_list(**self.arguments)
                self.echoJson(0, {"info": tasks_list, "totalCounts": counts})
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
        创建tasks
        :param param:
        :return:
        """
        try:
            validate.tasks_create(self.arguments)
            tasks = self.service.create_new(**self.arguments)
            if tasks is False or tasks is 0:
                raise exceptions.Database(exceptions.data_save_error,
                                          exceptions.get_error_message(exceptions.data_save_error))
            self.echoJson(0, tasks)
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
        更新task
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.tasks_update(self.arguments)
            del self.arguments['id']
            tasks = self.service.update(id, **self.arguments)
            if tasks is False or tasks is 0:
                raise peewee.DoesNotExist(exceptions.data_not_existed,
                                          exceptions.get_error_message(exceptions.data_not_existed))
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
        删除task
        :return:
        """
        self.arguments['id'] = id
        try:
            validate.tasks_delete(self.arguments)
            tasks = self.service.delete(self.arguments['id'])
            if tasks is False or tasks is 0:
                raise peewee.DoesNotExist(exceptions.data_not_existed,
                                          exceptions.get_error_message(exceptions.data_not_existed))
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
