from functools import wraps

import config


def empty_wrapper(func):
    @wraps(func)
    def inner(value):
        if not value:
            return ''
        return func(value)
    return inner


@empty_wrapper
def checkbox(value):
    return 'checked'


@empty_wrapper
def format_time(datetime_obj):
    return datetime_obj.strftime(config.DEFAULT_TIME_FORMAT)


@empty_wrapper
def format_datetime(datetime_obj):
    return datetime_obj.strftime(config.DEFAULT_DATETIME_FORMAT)
