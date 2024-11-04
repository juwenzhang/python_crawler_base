from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as ec #
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待
import time

browser = webdriver.Chrome()

browser.get("https://www.taobao.com/")

# 开始实现我们的窗口最大化
browser.maximize_window()

# 开始实现设置我们的动态的加载时间
time.sleep(3)

# 开始实现获取我们的数据
text_datas = browser.find_elements(By.CSS_SELECTOR, '.service-bd--LdDnWwA9 .J_Cat a')

for i in text_datas:
    if i.text == "":
        break
    print(i.text)
    print(i.get_attribute('href'))

time.sleep(20)
browser.close()

