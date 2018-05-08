from validator import validate, Pattern, InstanceOf, Required
import error
import re
import validate as input_validate


def cases_get(input_dict):
    rules = {
        "page": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "pagesize": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "name": [lambda x: (isinstance(x, str) or re.match("\w+", x))],
        "api": [lambda x: (isinstance(x, str) or re.match("\w+", x))],
        "method": [lambda x: (isinstance(x, str) or re.match("\w+", x))],
    }
    errors = {
        "page": "name is not existed or not int",
        "pagesize": "name is not existed or not int",
        "name": "name is not existed or invalid",
        "api": "name is not existed or invalid",
        "method": "name is not existed or invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def cases_create(input_dict):
    rules = {
        "name": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "api": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "method": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "headers": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "params_type": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "params": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "check_result": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "result": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "relation_id": [lambda x: (isinstance(x, int) or re.match("\d+", x))]
    }
    errors = {
        "name": "name is not existed or invalid",
        "api": "api is not existed or invalid",
        "method": "method is not existed or invalid",
        "headers": "headers is not existed or invalid",
        "params_type": "params_type is not existed or invalid",
        "params": "params is not existed or invalid",
        "check_result": "check_result is not existed or invalid",
        "result": "result is not existed or invalid",
        "relation_id": "relation_id is not existed invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def cases_update(input_dict):
    rules = {
        "id": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "name": [lambda x: (isinstance(x, str) and x is not '')],
        "api": [lambda x: (isinstance(x, str) and x is not '')],
        "method": [lambda x: (isinstance(x, str) and x is not '')],
        "headers": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "params_type": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "params": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "check_result": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "result": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "relation_id": [lambda x: (isinstance(x, int) or re.match("\d+", x))]
    }
    errors = {
        "id": "id is not existed or invalid",
        "name": "name is not existed invalid",
        "api": "api is not existed or invalid",
        "method": "method is not existed or invalid",
        "headers": "headers is not existed or invalid",
        "params_type": "params_type is not existed or invalid",
        "params": "params is not existed or invalid",
        "check_result": "check_result is not existed or invalid",
        "result": "result is not existed or invalid",
        "relation_id": "relation_id is not existed invalid"

    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def cases_delete(input_dict):
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
