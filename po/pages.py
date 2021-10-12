import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from base.base import BasePage
from data.testdata import TestData
from locator.locators import Locator
from time import sleep


class LoginPage(BasePage):
    """ 登录页面类 """

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self, username, password, verifycode):
        """ 登录 """

        self.driver.get(TestData.BASE_URL)

        self.driver.find_element(*Locator.username).send_keys(username)
        self.driver.find_element(*Locator.password).send_keys(password)
        self.driver.find_element(*Locator.verifycode).send_keys(verifycode)

        self.driver.find_element(*Locator.signin).click()

        # # 获取返回信息
        # element = self.wait(Locator.signin_response)
        #
        # return element.text

        sleep(0.2)

        try:
            response = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div')
            return response.text
        except:
            return None


class SellPage(BasePage):
    """
    销售出库页面类
    """

    def __init__(self, driver):
        super().__init__(driver)

    def sell(self, barcode, goodsize, discount, goodnum, paymethod, customerphone, creditratio, tickettype, ticketsum):
        # 输入条形码
        self.driver.find_element(*Locator.barcode).send_keys(barcode)
        self.driver.find_element(*Locator.search_barcode_btn).click()

        # 等待时间
        sleep(1)

        # 尺码
        goodssizeList = self.driver.find_element(*Locator.goodssizeList)
        Select(goodssizeList).select_by_value(goodsize)

        # 折扣
        discount_ele = self.driver.find_element(*Locator.discount)
        ActionChains(self.driver).double_click(discount_ele).perform()
        discount_ele.send_keys(discount)

        # 商品数量
        self.driver.execute_script("document.getElementsByClassName('buycount')[0].removeAttribute('readonly')")
        goodnum_ele = self.driver.find_element(*Locator.goodnumber)
        goodnum_ele.clear()
        goodnum_ele.send_keys(goodnum)

        # 输入付款方式
        paymethod_select = self.driver.find_element(*Locator.paymethod)
        Select(paymethod_select).select_by_visible_text(paymethod)

        # 输入会员电话
        customer_ele = self.driver.find_element(*Locator.customerphone)
        customer_ele.send_keys(customerphone)
        # customer_ele.send_keys(Keys.ENTER)
        self.driver.find_element(*Locator.query_customer_btn).click()

        # 输入积分倍数
        creditratio_ele = self.driver.find_element(*Locator.creditratio)
        creditratio_ele.clear()
        creditratio_ele.send_keys(creditratio)

        # 输入优惠券编号或原因
        tickettype_ele = self.driver.find_element(*Locator.tickettype)
        tickettype_ele.clear()
        tickettype_ele.send_keys(tickettype)

        # 优惠金额
        ticketsum_ele = self.driver.find_element(*Locator.ticketsum)
        ticketsum_ele.clear()
        ticketsum_ele.send_keys(ticketsum)

        # 确认收款
        self.driver.find_element(*Locator.payment_submit).click()

        # 返回结果
        result = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return result

    def clear_goods(self):
        """ 清空所购商品 """
        pass


class CustomerPage(BasePage):
    """会员管理页面类"""

    def __init__(self, driver):
        super().__init__(driver)

    def do_customer(self, method, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        """ 会员管理模块 """

        # 输入会员电话
        self.driver.find_element(*Locator.customerphone).send_keys(customerphone)

        # 输入会员名
        customername_ele = self.driver.find_element(*Locator.customername)
        customername_ele.clear()
        customername_ele.send_keys(customername)

        # 选择会员性别
        childsex_select = self.driver.find_element(*Locator.childsex)
        Select(childsex_select).select_by_visible_text(childsex)

        # 出身日期
        self.driver.execute_script('document.getElementById("childdate").removeAttribute("readonly")')
        childdate_ele = self.driver.find_element(*Locator.childdate)
        childdate_ele.clear()
        childdate_ele.send_keys(childdate)
        childdate_ele.send_keys(Keys.ENTER)

        # 输入母婴积分
        creditkids_ele = self.driver.find_element(*Locator.creditkids)
        creditkids_ele.clear()
        creditkids_ele.send_keys(creditkids)

        # 童装积分
        creditcloth_ele = self.driver.find_element(*Locator.creditcloth)
        creditcloth_ele.clear()
        creditcloth_ele.send_keys(creditcloth)

        if method == 'add':
            # 新增会员
            self.driver.find_element(*Locator.add_new_customer).click()
            time.sleep(2)
            res = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div').text
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button').click()
            return res
        elif method == 'query':
            # 查询会员
            self.driver.find_element(*Locator.query_cusomer).click()
            # 返回结果

    def edit_customer(self, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        """ 编辑会员前，应先查询出会员， 查询出的会员应该只有一条，才能方便定位的到修改按钮"""

        # 查询出要修改的会员
        self.do_customer('query', customerphone, customername, childsex, childdate, creditkids, creditcloth)

        # 定位到修改按钮
        self.driver.find_element(By.XPATH, '//*[@id="customerlist"]/tr[1]/td[11]/a')

        # 输入会员电话
        self.driver.find_element(*Locator.customerphone).send_keys(customerphone)
        # 输入会员名
        self.driver.find_element(*Locator.customername).send_keys(customername)
        # 选择会员性别
        childsex_select = self.driver.find_element(*Locator.childsex)
        Select(childsex_select).select_by_visible_text(childsex)

        self.driver.execute_script("document.getElementById(\"childsex\").removeAtrribute(\"readonly\")")
        self.driver.find_element(*Locator.childdate).send_keys(childdate)

        # 输入母婴积分
        self.driver.find_element(*Locator.creditkids).send_keys(creditkids)
        # 童装积分
        self.driver.find_element(*Locator.creditcloth).send_keys(creditcloth)

        # 点击修改按钮
        self.driver.find_element(*Locator.editBtn).click()


class BatchManager(BasePage):
    """ 批次管理 """

    def __init__(self, driver):
        super().__init__(driver)

    def upload(self, batchname, path):
        """ 上传文件"""
        batchname_ele = self.driver.find_element(*Locator.batchname)
        batchname_ele.clear()
        batchname_ele.send_keys(batchname)
        self.driver.find_element(*Locator.batchfile).send_keys(path)
        self.driver.find_element(*Locator.upload).click()

    def search_goods(self, batchname):
        """ 搜索商品 """
        Select(self.driver.find_element(*Locator.batchnamelist)).select_by_visible_text(batchname)

    def updategoods(self,
                    goodsserial,
                    goodsname,
                    quantity,
                    unitprice,
                    totalprice,
                    costunitprice,
                    costtotalprice):
        """ 商品修改 """

        self.driver.find_element(*Locator.goodsserial).send_keys(goodsserial)
        self.driver.find_element(*Locator.goodsname).send_keys(goodsname)
        self.driver.find_element(*Locator.quantity).send_keys(quantity)
        self.driver.find_element(*Locator.unitprice).send_keys(unitprice)
        self.driver.find_element(*Locator.totalprice).send_keys(totalprice)
        self.driver.find_element(*Locator.costunitprice).send_keys(costunitprice)
        self.driver.find_element(*Locator.costtotalprice).send_keys(costtotalprice)

