import handler
import config


# 请求路由
routers = [
    # users 用户设置
    (r"/{}/users/??(\w*-*\w*-*\w*-*\w*-*\w*)".format(config.api_version), handler.UsersHandler),

    # password 设置
    (r"/{}/check/??(\w*-*\w*-*\w*-*\w*-*\w*)".format(config.api_version), handler.PasswordHandler),
]
