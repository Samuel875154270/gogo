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

class SymbolHandler(BaseHandler):

    service = sSymbol()

    @tornado.web.asynchronous
    def get(self, symbol_id):
        """
        获取品种
        :return:
        """
        self.arguments['symbol_id'] = symbol_id
        try:
            validate.symbol_get(self.arguments)
            if symbol_id is not None and symbol_id is not '':
                symbol = self.service.get(**self.arguments)
                symbol = model_to_dict(symbol)
                self.echoJson(0, symbol)
            else:
                # 如果没有 symbol_id 的话 就是获取列表
                symbols, counts = self.service.get_list(**self.arguments)
                self.echoJson(0, {"data": symbols, "totalCounts": counts})
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
        创建品种
        :return:
        """
        try:
            validate.symbol_create(self.arguments)
            symbol = self.service.create(**self.arguments)
            if symbol is False or symbol is 0:
                raise exceptions.Database(exceptions.data_save_error, exceptions.get_error_message(exceptions.data_save_error))
            self.echoJson(0, model_to_dict(symbol))
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
    def put(self, symbol_id):
        """
        更新品种
        :return:
        """
        self.arguments['symbol_id'] = symbol_id
        try:
            validate.symbol_update(self.arguments)
            del self.arguments['symbol_id']
            symbol = self.service.update(symbol_id, **self.arguments)
            if symbol is False or symbol is 0:
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
    def delete(self, symbol_id):
        """
        删除品种
        :return:
        """
        self.arguments['symbol_id'] = symbol_id
        try:
            validate.symbol_delete(self.arguments)
            del self.arguments['symbol_id']
            symbol = self.service.delete(symbol_id, **self.arguments)
            if symbol is False or symbol is 0:
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
