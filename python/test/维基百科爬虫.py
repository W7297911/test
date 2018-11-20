# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-19 23:48
# Author:Wangyafei

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors

# 请求URL并把结果用UTF-8编码
req = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')

# 使用BeautifulSoup去解析
soap = bs(req, 'html.parser')

# 获取所有以/wiki/开头的a标签的href属性
listUrls = soap.findAll('a', href=re.compile(r'^/wiki/'))

# 输出所有词条对应的名称和URL
for url in listUrls:

    # 过滤以.jpg和.JPG结尾的URL
    if not re.search(r'\.(jpg|JPG)$', url['href']):

        # 输出URL的文字和对应的链接
        # string只能获取一个， get_text()获取标签下所有的文字
        print(url.get_text(), '<------->', 'https://en.wikipedia.org' + url['href'])
        # 获取数据库链接
        connection = pymysql.Connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     db='wikiurl',
                                     charset='utf8mb4')
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = 'insert into `urls`(`urlname`,`urlhref`) VALUE (%s,%s)'
                # 执行sql语句
                cursor.execute(sql, (url.get_text(), 'https://en.wikipedia.org' + url['href']))
                # 提交
                connection.commit()
        finally:
            connection.close()
