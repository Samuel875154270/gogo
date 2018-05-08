from validator import validate, Pattern, InstanceOf, Required
import error
import re
import validate as input_validate


def hosts_get(input_dict):
    rules = {
        "page": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "pagesize": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "host": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "name": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "page": "page is not invalid int",
        "pagesize": "pagesize is invalid int",
        "host": "host is not existed or invalid",
        "name": "name is not existed or invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def hosts_create(input_dict):
    rules = {
        "name": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "host": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "app_id": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "app_secret": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "remark": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "name": "name is not existed or invalid",
        "host": "host is not existed or invalid",
        "app_id": "app_id is not existed or invalid",
        "app_secret": "app_secret is not existed or invalid",
        "remark": "remark is not existed or invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def hosts_update(input_dict):
    rules = {
        "id": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "host": [lambda x: (isinstance(x, str) and x is not '')],
        "name": [lambda x: (isinstance(x, str) and x is not '')],
        "app_id": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "app_secret": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "remark": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "id": "id is not existed or invalid",
        "host": "host is not existed invalid",
        "name": "name is not existed invalid",
        "app_id": "app_id is not existed or invalid",
        "app_secret": "app_secret is not existed or invalid",
        "remark": "remark is not existed or invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def hosts_delete(input_dict):
    rules = {
        "id": [Required, lambda x: (isinstance(x, str) and x is not '')],
    }
    errors = {
        "id": "id is not existed or invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))
