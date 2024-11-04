from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as ec #
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待
import time


browser = webdriver.Chrome()

browser.get("https://www.taobao.com/")

# 实现我们的窗口最大化
browser.maximize_window()

# 开始实现向我们的搜索框输入内容
by_input_id = browser.find_element(By.ID, "q")
by_input_id.send_keys("键盘")

print("稍等一会儿，马上开始搜索内容...")
time.sleep(5)

# 开始实现搜索内容
by_className = browser.find_element(By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")
by_className.click()

time.sleep(30)