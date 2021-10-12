# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     ReflectDemo
   Description :
   Author :       lishanjie
   date：          2021/9/8
-------------------------------------------------
   Change Activity:
                   2021/9/8:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/9/8 15:11'

import sys
import time

from selenium import webdriver
import po.pages


# driver = webdriver.Chrome()
# module = sys.modules['po.pages']
#
# cls = getattr(module, 'LoginPage')
#
# func = getattr(cls(driver), 'sign_in')
#
# res = func('admin', 'admin123', '0000')
#
# print(res)


def test():

    driver = webdriver.Chrome()

    with open('../data/userdata') as f:
        lst = f.readlines()

    for item in lst:

        tmp = item.strip().split(',')
        module_name = tmp[0]
        class_name = tmp[1]
        func_name = tmp[2]

        __import__(module_name)

        module = sys.modules[module_name]
        cls = getattr(module, class_name)
        func = getattr(cls(driver), func_name)
        res = func(*tmp[3:])
        time.sleep(2.5)
        print(res)


if __name__ == '__main__':
    test()