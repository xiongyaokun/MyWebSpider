# MyWebSpider
学习Web爬虫的心得体会
***
## 2018-08-08 dingdian
- 爬取顶点小说网，获取小说名称、作者、类别、id
- 简单了解了一下Scrapy框架的运行机制
- 期间，安装Twisted库出现问题，使用pip在线安装容易出现错误，所以先下载.whl包进行安装
- cd到Twisted包所在目录下，然后pip install “包全名”
### 运行方法
- 复制dingdian文件夹
- 进入dingdian/
- 方法一：python entrypoints.py
- 方法二：scrapy crawl dingdian
