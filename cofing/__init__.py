# 当前API版本
api_version = 'v1'

# mysql 配置文件
mysql = {
    'db': 'doo_rebate_center_demo',
    'info': {
        'host': '119.147.37.56',
        'port': 13317,
        'user': 'root',
        'password': 'abc123',
        'charset': 'utf8'
    }
}

listen = 8888

__all__ = ['api_version', 'mysql']
