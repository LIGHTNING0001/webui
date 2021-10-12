from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class ExcelTools:

    def __init__(self, name):
        self.name = name


class DriverInstance:

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = webdriver.Chrome()

        return cls.instance


class Singleton:

    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, name):
        self.name = name


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 设置显示等待时间，有问题
    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    # 判断元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True

