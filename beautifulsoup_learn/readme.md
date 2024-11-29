## BeautifulSoup Basic Use

### introduce this module

* 这个模块是一个 python 中的一个高效的的网页解析库，可以从 `HTML` `XML`(一种存储数据的文档) 文件中提取数据
* 可以实现的是使用我们的不同的解析器，实现对 `HTML XML HTML5` 实现解析，从而实现获取我们网页中的数据
* 可以换言之： 这个模块就是我们实现爬虫的一个 `爬虫利器` (使用过正则表达式来爬取网页的，就知道这个的便捷了)
* 支持使用多种 `解析器`
* 安装命令: `pip install BeautifulSoup4` (`bs4`)
* 然后本次使用的解析器就是: `lxml HTML 解析器`
  * 安装命令: `pip install lxml`


### touch tags selectors

* 通过标签选择器来获取我们的数据
  * `.string` 实现获取文本内容
  * `.name` 实现获取标签本身名称
  * `.attrs[]` 获取标签中属性的值


### normal selector
* 通过标准选择器实现查找内容
  * `find_all(tagname, attrs, recursive, text, **kwargs)`
  * 可以根据我们的`标签名， 属性， 内容`实现查找文档
  * 但是需要注意的是，这个方法实现查询到的结果是一个数组


### CSS selector
* 通过CSS选择器实现查找内容
  * 就是使用的是我们的 `soup.select(selectorName)`
  * 最后实现返回的是我们的列表 list
  * CSS 选择器
    * 标签选择器 ： 直接书写标签名就行了
    * 类选择器  ： .类名
    * id选择器  ： 