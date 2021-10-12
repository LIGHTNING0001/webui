# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     customerpagetest
   Description :
   Author :       lishanjie
   date：          2021/9/7
-------------------------------------------------
   Change Activity:
                   2021/9/7:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/9/7 19:36'

import time
import allure
import pytest
from selenium import webdriver

from po.pages import LoginPage, CustomerPage


@allure.feature('会员管理')
class TestCustomerPage:

    data = {
        ('add', '13498077658', 'li', '男', '2021-09-07', 10, 10)
    }

    query_data = {
        ('query', '13498077658', '', '男', '', 0, 0)
    }

    def setup_class(self):
        self.driver = webdriver.Chrome()
        loginPage = LoginPage(self.driver)
        loginPage.sign_in('admin', 'admin123', '0000')

    @pytest.mark.parametrize('method, customerphone, customername, childsex, childdate, creditkids, creditcloth', data)
    def test_add_customer(self, method, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        """ 增加会员测试用例 """
        customerPage = CustomerPage(self.driver)
        time.sleep(1)
        self.driver.find_element_by_partial_link_text('会员管理').click()
        customerPage.do_customer(method, customerphone, customername, childsex, childdate, creditkids, creditcloth)

    @pytest.mark.parametrize('method, customerphone, customername, childsex, childdate, creditkids, creditcloth', query_data)
    def test_query_customer(self, method, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        """ 查询会员测试用例 """
        customerPage = CustomerPage(self.driver)
        time.sleep(1)
        self.driver.find_element_by_partial_link_text('会员管理').click()
        customerPage.do_customer(method, customerphone, customername, childsex, childdate, creditkids, creditcloth)

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-sv', 'customerpage_test.py'])