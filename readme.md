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