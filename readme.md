## 该仓库的本分支主要目的
该分支主要是为了讲解一些关于如何使用 python 来实现爬取网页的方法的仓库分支

* 第一步: 了解 python requests module 的使用
  * 普通的 `get` 请求如何实现
  * 普通的 `post` 请求如何实现
  * 携带请求参数的 `get` 请求
  * 携带请求参数的 `post` 请求
  * 如何获取不同格式的响应数据: `text content json status_code`
  * 设置请求头伪装自己的方法: `headers`
  * 前后端交互重要知识点: 会话维持 `session` `cookie`


* 第二步: 了解 python jsonpath module 的使用
  * 理解前端的异步加载和同步加载
  * 了解开发一个项目的总的开发流程
  * 使用新的处理数组方法
  * 爬取网页的时候的递归以及异常捕获的处理
  * 拓展使用 openpyxl 实现操作 excel 表


* 第三步： learn bs4
  * 知道如何通过标签选择器获取我们的数据
  * 了解 `find_all` 的使用
  * 了解 `.selet()` 的使用


* 第四步： learn xpath
  * 首先我们实现使用这个模块的时候
  * 我们首先需要做的就是我们的进行
  * 学习其中的语法即可
  * 然后这个的使用就是直接从我们的 lxml 解析器中实现获取


* 推荐使用 fiddler 工具
  * fiddler 就是位于我们的客户端和服务端之间的一种代理
    * 也是当前最常见的抓包工具
  * 该工具可以实现我们的记录客户端和服务端之间的所有的请求
    * 可以实现针对特定的请求实现分析数据，请求数据，设置断点，调试web应用
      * 修改请求的数据，甚至是实现修改服务器返回的数据，是我们的 web 调试的利器

![image01](/images/image01.png)
* 没有使用 fiddler 的时候，
  
  * 直接是 客户端给服务端发送请求，然后服务端给客户端响应
* 使用了 fiddler 之后
  * 客户端先把请求发给 fiddler,然后把请求发送给服务端
  
  * 服务端实现响应数据也是先把响应给 fiddler,然后给客户端
  
  * 想用就用，不用就不用，没强制要求（个人感觉不好用）
  
    

***

***



# 爬虫所需模块使用

| python_module |                             desc                             |                          learn_link                          |
| :-----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|   requests    | 这个模块就是实现的是我们对网页发送请求的模块，爬虫的首先的任务就是先发送请求 | https://blog.csdn.net/maiya_yayaya/article/details/131608297 |
| beautifulsoup | 这个模块就是实现的是将我们请求回来的 HTML 数据实现解析的一个模块，主要是用来实现的是解析数据使用的 | https://blog.csdn.net/m0_62283350/article/details/139795111  |
|   jsonpath    | 这个模块就是实现的是将我们的请求回来 Json 数据进行解析的一个模块 | https://blog.csdn.net/powerbiubiu/article/details/137792234  |
|     lxml      | 这个模块既是我们的 beautifulsoup 的解析的解析器，同时话可以实现解析我们的 XML 数据 | https://blog.csdn.net/2401_83617404/article/details/141726851 |
|      re       | 这个模块就是实现的是我们的每种语言中都具有的一种进行匹配数据的语言规则，正则表达式 | https://blog.csdn.net/weixin_40134371/article/details/136187262 |
|    pymysql    | 这个模块就是实现的是讲我们的数据进行保存到数据库中的一个模块，就是一些数据库的操作 | https://blog.csdn.net/Gherbirthday0916/article/details/123524627 |
|      sys      | 这个模块就是实现的是对我们的操作系统进行的一些操作模式，在爬虫中我们是可以通过这个模块来进行设置我们的递归深度的 | https://blog.csdn.net/qq_56262770/article/details/140957405  |
|     json      | 这个模块就是实现的是将 python 中的数据实现 和 json 数据之间的转换的模块，在爬虫也是十分常见以及使用的 | https://blog.csdn.net/weixin_44799217/article/details/112256220 |
|     time      | 这个模块就是实现的是我们的关于操作时间的模块，我们是可以通过这个模块来实现判断我们的爬取数据的快慢的，然后实现优化代码 | https://blog.csdn.net/weixin_54546190/article/details/120897108 |
|   openpyxl    | 这个模块可以实现的是将我们的数据实现保存到我们的 excel 表中  | https://blog.csdn.net/weixin_41238626/article/details/140671730 |



***

***



# 文件目录分类

|       DirName       |                             Desc                             |                             Link                             |
| :-----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| beautifulsoup_learn |        用来记录的是关于 beautifulsoup 模块的基本使用         | https://github.com/juwenzhang/python_crawler_base/tree/python_crawler_base/beautifulsoup_learn |
|   requeats_learn    |         用来实现记录的是关于 requests 模块的基本使用         | https://github.com/juwenzhang/python_crawler_base/tree/python_crawler_base/requests_learn |
|   jsonpath_learn    |         用来实现记录的是关于 jsonpath 模块的基本使用         | https://github.com/juwenzhang/python_crawler_base/tree/python_crawler_base/jsonpath_learn |
|     Xpath_learn     |    用来实现的是记录关于使用 lxml 解析 XML 数据的基本使用     | https://github.com/juwenzhang/python_crawler_base/tree/python_crawler_base/Xpath_learn |
|    demo_project     | 用来实现的是记录关于写一些爬取小的网站的数据的脚本项目的目录 | https://github.com/juwenzhang/python_crawler_base/tree/python_crawler_base/demo_project |

