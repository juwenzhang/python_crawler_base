from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链对象
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as ec # 设置时间等待的东西
from selenium.webdriver.support.wait import WebDriverWait  # 控制时间等待
from selenium.webdriver.support.expected_conditions import alert_is_present
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

    def selenium_search(self):
        """
        用来实现搜索东西的自动化测试函数
        :return:
        """
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

    def selenium_login(self):
        """
        用来解决登录问题的函数
        :return:
        """
        # 等待页面的加载完毕
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 到底部
        try:
            login_btn = self.browser.find_element(By.XPATH, '//*[@id="J_main"]/div[4]/div/div[2]')
            login_btn.click()
            # =================================================
            time.sleep(10)
            use_weixin_login = self.browser.find_element(By.XPATH, '//*[@id="kbCoagent"]/ul/li[2]/a/span')
            use_weixin_login.click()
            # =================================================
            time.sleep(10)
            weixin_btn = self.browser.find_element(By.XPATH, '//*[@id="tpl_for_page"]/span[1]/div[1]/div[5]/div/button')
            weixin_btn.click()
            # 解决微信登录后的弹窗问题==============================
            WebDriverWait(self.browser, 5).until(alert_is_present())  # 等待弹出窗口出现
            alert = self.browser.switch_to.alert
            alert.accept()  # 确认
            time.sleep(2)
        except Exception as e:
            print(f"error: {e}")


    def run(self):
        """
        运行函数
        :return:
        """
        self.selenium_search()
        time.sleep(10)
        # self.selenium_login()
        # time.sleep(10)
        self.browser.close()

if __name__ == "__main__":
    getJDSelenium = GetJDSelenium("零食")
    getJDSelenium.run()