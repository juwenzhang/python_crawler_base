from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 键盘事件
from selenium.webdriver.support import expected_conditions as ec  #
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待

import time

browser = webdriver.Chrome()

browser.get("https://www.baidu.com/")

# 开始实现向我们的搜索框输入内容
by_input_id = browser.find_element(By.XPATH, '//*[@id="kw"]')
by_input_id.send_keys("键盘")

print("稍等一会儿，马上开始搜索内容...")
time.sleep(5)

# 点击键盘 enter
by_input_id.send_keys(Keys.ENTER)


# 开始我们的动态等待,当我们的页面在动态时间内还没有实现加载完毕的话，直接报错即可
wait = WebDriverWait(browser, 10)
wait.until(ec.presence_of_all_elements_located((By.XPATH, '//*[@id="page"]/div/a[10]')))

print(browser.page_source)

time.sleep(30)