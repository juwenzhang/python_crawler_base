## 查找元素查找方法

> find_element_by_id 根据id属性来定位
>
> find_element_by_name 根据name元素来定位
>
> find_element_by_xpath 根据xpath语法来定位
>
> find_element_by_tag_name 根据标签名来定位
>
> find_element_by_class_name 根据class的名字来定位
>
> find_element_by_css_selector 根据css选择器来定位
>
> 以下两种方法都是用来的定位超链接的，也就是对应html页面中的a标签，,括号里传入的值就是a标签中的超链接文字
>
> 两者的区别在于一个是完整的超链接文字，一个是可以只写部分超链接文字
>
> find_element_by_link_text 需要完整的超链接文字
>
> find_element_by_partial_link_text 可以只写部分超链接文字
>
> 3.8以后的版本中用法
>
> find_element(By.ID, ‘id’) 根据id属性来定位
> find_element(By.NAME, ‘name’) 根据name元素来定位
> find_element(By.XPATH, ‘xpath语法’) 根据xpath语法来定位
> find_element(By.TAG_NAME, ‘input’) 根据标签名来定位
> find_element(By.CLASS_NAME, ‘classname’) 根据class的名字来定位
> find_element(By.CSS_SELECTOR, ‘#id’) 根据css选择器来定位
> find_element(By.LINK_TEXT, ‘text’) 根据文本s属性来定位
> 单个元素

```python
from selenium import webdriver 
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element(By.LINK_TEXT,"新闻").click()


browser = webdriver.Chrome()

browser.get('https://www.taobao.com')
```

### 通过元素ID查找
```python
by_id = browser.find_element(By.ID, 'q')

by_id.send_keys('食物')

print(by_id)
```

### 通过css选择器查找    快捷方式 在网页中定位到，然后鼠标右键复制selector就是css语法
```python
css_selector = browser.find_element(By.CSS_SELECTOR, '#q')

css_selector.send_keys('食物')

print(css_selector)
```

#### 通过xpath查找
```python
xpath = browser.find_element(By.XPATH,'//*[@id="q"]')  
xpath.send_keys('食物')
print(xpath)

browser.close()
```

### 多个元素查找方法：

> find_elements(By.ID, ‘id’) 根据id属性来定位
> find_elements(By.NAME, ‘name’) 根据name元素来定位
> find_elements(By.XPATH, ‘xpath语法’) 根据xpath语法来定位
> find_elements(By.TAG_NAME, ‘input’) 根据标签名来定位
> find_elements(By.CLASS_NAME, ‘classname’) 根据class的名字来定位
> find_elements(By.CSS_SELECTOR, ‘#id’) 根据css选择器来定位
> find_elements(By.LINK_TEXT, ‘text’) 根据文本s属性来定位
> from selenium import webdriver

```python
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
```

### 找到淘宝中所有的分类
```python
elements = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(elements)  # 以列表形式返回
for i in elements:
    print(i)
browser.close()    
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
```

### 以下两种方法等价（作用相同）  以前版本的
```python
elements = browser.find_element_by_css_selector('.service-bd li')

print(elements)
browser.close()
```

## 元素交互操作

### 对获取的元素调用交互方法

```python
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://www.jd.com/')

text_input = browser.find_element(By.ID, 'key')
text_input.send_keys('iPhone')

time.sleep(1)

text_input.clear() # 清空

text_input.send_keys('iPad')  # 输入内容

button = browser.find_element(By.CLASS_NAME,'button')  #找到点击按钮
button.click()  # 单击
```

更多操作: http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

### 执行JavaScript

> selenium只能操作页面内部的东西，有一些操作必须借助JS实现，比如说实现添加一个页面，比如说滚动下拉条。 execute_script
>
> 滚动页面方法execute_script()  该方法可调用原生JavaScript的api
> 滚动到底部：window.scrollTo(0,document.body.scrollHeight)
> 滚动到顶部：window.scrollTo(0,0)
>
> 说明：
> window：js的window对象
> scrollTo：window的方法，可以滚到页面的任何位置
> scrollHeight：是dom元素的通用属性，document.body.scrollHeight会返回body元素的高度，基本上就是页面的高度
> scrollLeft：获取位于对象左边界和窗口目前可见内容的最左端之间的距离
> scrollTop：获取位于对象最顶端和窗口中课件内容的最顶端之间的距离
> scrollWidth：获取对象滚动的宽度

### execute_script 执行JS代码

```python
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.jd.com/')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 到底部
time.sleep(2)
browser.execute_script('window.scrollTo(0, document.body.scrollTop=0)')  # 到顶部
time.sleep(2)
browser.execute_script('alert("Hello world")')
```

## 获取元素信息获取单个文本和属性:

```python
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

it = browser.find_element(By.CSS_SELECTOR,'#roundtable &gt; div.ExploreHomePage-ContentSection-body &gt; div &gt; div:nth-child(1) &gt; div.ExploreRoundtableCard-questionList &gt; div:nth-child(1) &gt; a')


print(it.text)
print(it.get_attribute('href'))
browser.close()
```

### 获取多个:

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
```

### 找到淘宝中最上面的天猫和聚划算，天猫超市
```python
elements = browser.find_elements(By.CSS_SELECTOR, 'div ul.nav-hd li a')

print(elements)  # 以列表形式返回

for i in elements:
    print(i)
    print(i.text)  #获取文本值
    print(i.get_attribute('href'))  # 提取属性
```

## 等待特定元素出现后做某事

> FAQ：通常用于等待某个网页元素加载完毕后进行后续操作，避免出现异常
>
> 显式等待
> 明确要等待某个元素出现 等不到就一直等， 除非在规定的时间内都没找到 那么报出异常Exception

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')

wait = WebDriverWait(browser, 10)
wait = WebDriverWait(browser, 0.001)
```

  ###      特定元素是否存在于页面
> input = wait.until(EC.presence_of_element_located((By.ID, 'J_Toolkit')))
>
> print(input)
> EC
> EC模块的方法
>
> 导包：from selenium.webdriver.support import expected_conditions as EC
>
> title_is 标题是某内容
> title_contains 标题包含某内容
> presence_of_element_located 元素加载出，传入定位元组，如(By.ID, ‘p’)
> visibility_of_element_located 元素可见，传入定位元组
> visibility_of 可见，传入元素对象
> presence_of_all_elements_located 所有元素加载出
> text_to_be_present_in_element 某个元素文本包含某文字
> text_to_be_present_in_element_value 某个元素值包含某文字
> frame_to_be_available_and_switch_to_it frame加载并切换
> invisibility_of_element_located 元素不可见
> element_to_be_clickable 元素可点击
> staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
> element_to_be_selected 元素可选择，传元素对象
> element_located_to_be_selected 元素可选择，传入定位元组
> element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
> element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
> alert_is_present 是否出现Alert十、前进后退
> 浏览器控制

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.jd.com/')

browser.back() # 后退
time.sleep(1)

browser.forward()  # 前进
time.sleep(3)
browser.close()
```

## 选项卡管理

> 窗口切换 switch_to_window(窗口ID)
>
> 查看所有窗口ID window_handles
>
> FAQ：只有切换到当前窗口时，才能操作当前窗口（比如翻页、获取源代码等等）

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')  # 选项卡0  窗口0
time.sleep(1)
browser.execute_script('window.open()')  # 选项卡1  窗口1
time.sleep(1)
browser.execute_script('window.open()')  # 选项卡2   窗口2

print(browser.window_handles)  # 查看当前浏览器所有窗口ID

browser.switch_to.window(browser.window_handles[1])  # 浏览器对象加载选项卡1 切换到窗口1
browser.get('https://www.taobao.com') # 窗口1 打开淘宝

browser.switch_to.window(browser.window_handles[0])  # 浏览器对象加载选项卡0 切换到窗口0
browser.get('https://www.mi.com/')  # 窗口0 打开小米官网

browser.switch_to.window(browser.window_handles[2])   # 浏览器对象加载选项卡2 切换到窗口2
browser.get('https://jd.com')

browser.page_source

browser.switch_to.window(browser.window_handles[1])
browser.page_source
```

## Cookies

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
```

### 获取cookie
```python
cookies = browser.get_cookies()  # 获取服务器设置在本地的cookie
print(cookies)
```

### 设置 cookies  请求站点时携带的cookie信息
```python
browser.add_cookie({'name': 'zhangsan', 'domain': 'abcd123', 'value': 'hellozhang'})

print(browser.get_cookies())  # 查看设置成功的cookies信息
```
### 清除cookies
```python
browser.delete_all_cookies()  # 删除所有cookie

print(browser.get_cookies())
```

## 异常处理

知识点：异常处理模块所在位置

```python
from selenium.common.exceptions import TimeoutException, NoSuchElementException

In [65]:

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.find_element(By.ID, 'hello')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
```

