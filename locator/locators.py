from selenium.webdriver.common.by import By


class Locator:

    # 登录页面的元素
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    verifycode = (By.ID, 'verifycode')
    signin = (By.XPATH, '/html/body/div[4]/div/form/div[6]/button')

    # 登录返回
    signin_response = (By.XPATH, '/html/body/div[6]/div/div/div[2]/div')

    # 批次管理元素
    batchname = (By.ID, 'batchname') #批次输入框
    batchfile = (By.ID, 'batchfile')
    upload = (By.XPATH, '/html/body/div[4]/div[1]/form[2]/div/input[1]')

    # 批次查询 元素
    batchnamelist = (By.ID, 'batchnamelist')
    search_btn = (By.XPATH, '/html/body/div[4]/div[1]/form[2]/div/input[2]')

    # 修改商品信息元素
    goodsserial = (By.ID, 'goodsserial')
    goodsname = (By.ID, 'goodsname')
    quantity = (By.ID, 'quantity')
    unitprice = (By.ID, 'unitprice')
    totalprice = (By.ID, 'totalprice')
    costunitprice = (By.ID, 'costunitprice')
    costtotalprice = (By.ID, 'costtotalprice')
    update = (By.XPATH, '//*[@id="editModal"]/div/div/div[3]/button[2]')

    # 销售出库
    barcode = (By.ID, "barcode")    # 条形码
    search_barcode_btn = (By.XPATH, '//button[@onclick=\"queryByBarCode()\"]')
    paymethod = (By.ID, 'paymethod')  # 支付方式
    customerphone = (By.ID, 'customerphone')  # 会员电话
    query_customer_btn = (By.XPATH, '//*[@id="vipsell"]/div[1]/form/div[2]/button')  # 查询会员按钮
    oldcredit = (By.ID, "oldcredit")    # 已有积分
    newcredit = (By.ID, "newcredit")    # 本次新增积分
    creditratio = (By.ID, "creditratio")    # 积分倍数
    tickettype = (By.ID, "tickettype")      # 优惠券编号或原因
    ticketsum = (By.ID, "ticketsum")    # 优惠金额
    payment_submit = (By.ID, "submit")      # 确认收款

    goodssizeList = (By.ID, "goodssizeList")    # 尺码
    discount = (By.XPATH, "//*[@id=\"goodslist\"]/tr/td[6]/input")      # 折扣
    goodnumber = (By.CLASS_NAME, "buycount")    # 数量

    # 商品入库
    inputsize = (By.ID, "inputsize")
    message = (By.ID, "message")
    store = (By.ID, "//*[@onclick=\"confirmStore()\"]")

    # 会员模块
    customerphone = (By.ID, "customerphone")
    customername = (By.ID, "customername")
    childsex = (By.ID, "childsex")
    childdate = (By.ID, "childdate")
    creditkids = (By.ID, "creditkids")
    creditcloth = (By.ID, "creditcloth")

    # 新增按钮
    add_new_customer = (By.XPATH, "/html/body/div[4]/div[1]/form[2]/div[2]/button[1]")

    # 修改按钮
    editBtn = (By.ID, "editBtn")

    # 查询按钮
    query_cusomer = (By.XPATH, "/html/body/div[4]/div[1]/form[2]/div[2]/button[3]")









