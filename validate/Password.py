from validator import validate, Pattern, InstanceOf, Required
import error
import re
import validate as input_validate


def check_password(input_dict):
    rules = {
        "email": [Required, lambda x: (isinstance(x, str) and
                                       re.match("\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}", x))],
        "password": [Required, lambda x: (isinstance(x, str) and x is not '')]
    }
    errors = {
        "email": "email is not existed or invalid",
        "password": "password is not existed invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))


def update_password(input_dict):
    rules = {
        "email": [Required, lambda x: (isinstance(x, str) and
                                       re.match("\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}", x))],
        "password": [Required, lambda x: (isinstance(x, str) and x is not '')]
    }
    errors = {
        "email": "email is not existed or invalid",
        "password": "password is not existed invalid"
    }
    default_error = "Params Invalid!"
    res = validate(rules, input_dict)
    if res.valid is False:
        # 抛出第一个参数验证的错误
        for key in res.errors:
            raise error.RequestData(error.request_data_error, errors.get(key, default_error))
