from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as ec #
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待

import time

# 开始实现我们的初始化
browser = webdriver.Chrome()

# 发送对我们网页的请求
browser.get("https://www.baidu.com/")

# 获取我们网页中源代码 .page_source
# print(browser.page_source)


# 开始实现寻找我们的点击的行文
find_data = browser.find_element(By.LINK_TEXT, "新闻")
find_data.click()

# 让我们的程序停止
time.sleep(1000)

# 时间到了自动关闭程序
browser.close()