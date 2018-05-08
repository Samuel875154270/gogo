from validator import validate, Pattern, InstanceOf, Required
import error
import re
import validate as input_validate


def tasks_get(input_dict):
    rules = {
        "page": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "pagesize": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "host_id": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "name": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "page": "page is not invalid int",
        "pagesize": "pagesize is invalid int",
        "host_id": "host_id is not existed or invalid",
        "name": "name is not existed or invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def tasks_create(input_dict):
    rules = {
        "name": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "host_id": [Required, lambda x: (isinstance(x, int) and x is not ''and re.match("\d+", x))],
        "case_ids": [Required, lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "name": "name is not existed or invalid",
        "host_id": "host_id is not existed or invalid",
        "case_ids": "case_ids is not existed or invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def tasks_update(input_dict):
    rules = {
        "id": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "host_id": [lambda x: (isinstance(x, str) and x is not '')],
        "name": [lambda x: (isinstance(x, str) and x is not '')],
    }
    errors = {
        "id": "id is not existed or invalid",
        "host_id": "host is not existed invalid",
        "name": "name is not existed invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def tasks_delete(input_dict):
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
