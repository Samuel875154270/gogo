from validator import validate, Pattern, InstanceOf, Required
import error
import re
import validate as input_validate


def users_get(input_dict):
    rules = {
        "page": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "pagesize": [lambda x: (isinstance(x, int) or re.match("\d+", x))],
        "name": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
    }
    errors = {
        "page": "page is not invalid int",
        "pagesize": "pagesize is invalid int",
        "name": "name is not existed invalid",
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def users_create(input_dict):
    rules = {
        "name": [Required, lambda x: (isinstance(x, str) and x is not '')],
        "email": [Required, lambda x: (isinstance(x, str) and
                                       re.match("\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}", x))],
        "password": [Required, lambda x: (isinstance(x, str) and x is not '')]
    }
    errors = {
        "name": "name is not existed or invalid",
        "email": "email is not existed or invalid",
        "password": "password is not existed invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def users_update(input_dict):
    rules = {
        "id": [lambda x: (isinstance(x, str) and re.match("\w+", x))],
        "name": [lambda x: (isinstance(x, str) and re.match("\w+", x))]
    }
    errors = {
        "id": "id is not existed or invalid",
        "name": "name is not existed invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def users_delete(input_dict):
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
