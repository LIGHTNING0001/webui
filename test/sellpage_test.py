# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     sellpagetest
   Description :
   Author :       lishanjie
   date：          2021/9/7
-------------------------------------------------
   Change Activity:
                   2021/9/7:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/9/7 18:04'

import time

import pytest
from selenium import webdriver

from po.pages import LoginPage, SellPage
import allure


@allure.feature('销售出库')
class TestSellPage:
    """ 销售出库测试类 """

    # 测试数据
    data = [
        ('6955203664471', '110', '80', 2, '刷卡', '18091230219', '2.0', '无', 10)
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        loginPage = LoginPage(self.driver)
        loginPage.sign_in('admin', 'admin123', '0000')

    @pytest.mark.parametrize('barcode, goodsize, discount, goodnum, paymethod, customerphone, creditratio, '
                             'tickettype, ticketsum', data)
    def test_sell(self, barcode, goodsize, discount, goodnum, paymethod, customerphone, creditratio, tickettype, ticketsum):
        """ 销售出库测试用例 """
        sellPage = SellPage(self.driver)
        time.sleep(1)
        result = sellPage.sell(barcode, goodsize, discount, goodnum, paymethod, customerphone, creditratio, tickettype, ticketsum)
        print(result)

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-sv', 'sellpage_test.py'])