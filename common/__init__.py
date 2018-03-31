import time
import datetime


def get_date():
    return time.strftime("%Y%m%d", time.localtime(time.time()))


def get_time_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_real_page(page_from_request):
    """
    获取数据库中真正页码，前端传的页码从1开始，所以需要减1
    :param page_from_request:
    :return:
    """
    if is_number(page_from_request):
        if int(page_from_request) >= 1:
            return int(page_from_request) - 1
        else:
            return 0
    else:
        return 0


def is_number(param):
    try:
        float(param)
        return True
    except (ValueError, TypeError):
        pass
    return False


def to_json(code=0, data=None):
    return {
        "code": code,
        "data": data
    }
