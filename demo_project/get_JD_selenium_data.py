from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as ec # 设置时间等待的东西
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待
import time

class GetJDSelenium(object):

    def __init__(self, content):
        """
        构造函数
        :param content:
        """
        self.url = "https://www.jd.com/"
        self.browser = webdriver.Chrome()
        self.content = content

    def __del__(self):
        """
        析构函数
        :return:
        """
        print("自动化测试任务完毕...")

    def get_jd(self):
        self.browser.get(self.url)
        # 直接先实现满屏操作
        self.browser.maximize_window()
        # 添加动态时间
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.presence_of_element_located((By.ID, 'key')))
        # 等待我们的搜索框加载完毕后在实现获取搜索框
        text_input = self.browser.find_element(By.ID, 'key')
        text_input.send_keys(self.content)
        text_input.send_keys(Keys.ENTER)

    def get_data(self):
        # 等待页面的加载完毕
        pass


    def run(self):
        self.get_jd()
        time.sleep(20)
        self.browser.close()

if __name__ == "__main__":
    getJDSelenium = GetJDSelenium("零食")
    getJDSelenium.run()