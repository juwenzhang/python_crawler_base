## Xpath module basic use

* 介绍 Xpath
  * 我们是可以先实现将我们的HTML文档转化为我们的 XML 文档后
  * 然后通过 Xpath 来实现查找 HTML 节点或者元素的操作
  * 这个的出现也是弥补了我们对于re正则表达式利用不熟练而产生的


* 理解XML
  * XML指的是可扩展的标记语言
  * XML是一门标记语言，和HTML类似
  * XML的出现是一种用来实现传递数据，并非显示数据的
  * XML的标签是需要我们自己定义的

* 将爬取的数据传入数据库的操作
  * 使用到的模块就是我们的 pymysql 
  * `pip install pymysql`

* XML 和 HTML 的区别
  * XML `Extensible Markup Language`
  * HTML `HyperText Markup Language`
  * XML 用来实现的是传递数据
  * HTML 用来的是显示数据
  * HTML DOM
    * 是我们的文档对象模型，浏览器提供给javascript的一种API


* Xpath的使用
  * Xpath 就是一门用来实现在一个HTML文档中实现查找信息的一门编程
    * 语言，可以实现对XML文档中的元素或者属性进行遍历

* [Xpath详解](https://blog.csdn.net/Hudas/article/details/141760272)
  * / 就是表示的是下一个层级
  * // 表示的就是忽略层级进行选择标签
  * 最终就是使用的是我们的 lxml 解析器
