from po.pages import LoginPage
import pytest
from selenium import webdriver

import allure


@allure.feature('登录')
class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome()

    # 测试数据
    data = [
        ('admin', 'admin', '0000', '登录失败'),
        ('adm', 'admin123', '0000', '登录失败'),
        ('', 'admin123', '0000', '登录失败'),
        ('admin', '', '0000', '登录失败'),
        ('admin', 'admin123', '0000', 'admin')
    ]

    @pytest.mark.parametrize('username, password, verifycode, expect', data)
    def test_login(self, username, password, verifycode, expect):
        loginPage = LoginPage(self.driver)
        res = loginPage.sign_in(username, password, verifycode)
        assert expect in res

    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-s', 'login_test.py'])
