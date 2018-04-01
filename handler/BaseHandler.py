import tornado.web
import demjson
import common
import json
import model as model


class BaseHandler(tornado.web.RequestHandler):
    DooSecure = None
    arguments = {}

    def initialize(self):
        """
        重写框架方法
        :return:
        """
        # 这里必须初始化为空，避免连接缓存
        self.arguments = {}
        # 在body中的json数据
        request_json = self.request.body.decode()
        request_dict = {}
        if request_json is not None and request_json is not "":
            request_dict = json.loads(request_json)
        # 获取在请求url中的数据
        for key in self.request.arguments.keys():
            self.arguments[key] = bytes.decode(self.request.arguments[key][0])

        # 结合两者数据，在url中的数据优先级高
        for key in request_dict.keys():
            if self.arguments.get(key) is None:
                self.arguments[key] = request_dict[key]

        # 添加AppID
        self.arguments['appid'] = self.request.headers.get("X-Auth-Appid")

    def echoJson(self, code=0, data=None):
        """
        输出Json内容
        :param arr:
        :return:
        """
        Json = {
            'code': code,
            'data': data
        }
        self.write(demjson.encode(Json))

    def echo_request_data_error(self):
        """
        请求参数错误
        :param:
        :return:
        """
        self.echoJson(2001, "请求参数错误")

    def getParam(self, name):
        """
        获取请参数
        :param name:
        :return:
        """
        return self.arguments.get(name)

    def echoSuccess(self):
        self.echoJson(code=0, data='success')

    def echo_error(self, error_code=20000, error_message="error"):
        """
        输出错误信息
        :param arr:
        :return:
        """
        json = {
            'code': error_code,
            'data': {"info": error_message}
        }
        self.write(demjson.encode(json))

    def close_connect_and_finish(self):
        self.finish()
        model.database.close()
