# -*- coding: utf-8 -*-
# @Date    : 2017-04-05 10:36:25
# @Author  : Alan Lau (rlalan@outlook.com)
import time


# print(now_time)


def log():
    def outer(func):
        def wrapper(*args, **kwargs):
            now_time = str(time.strftime('%Y-%m-%d %X', time.localtime()))
            re = func(*args, **kwargs)
            print('%s called at %s' % (func.__name__, now_time))
            return re
        return wrapper
    return outer()


# @log
# def func(a):
#     print(a)

# func('b')

__all__ = [log]
