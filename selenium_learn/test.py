from selenium import webdriver
import time

a = webdriver.Chrome()

a.get("https://www.baidu.com/")
time.sleep(20)