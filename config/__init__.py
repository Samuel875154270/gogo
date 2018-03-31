# 当前API版本
api_version = 'v1'

mysql = {
    "db": "gogo",
    "info": {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "charset": "utf8"
    }
}

listen = 8888

__all__ = ['api_version', 'mysql']
