# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-21 0:17
# Author:Wangyafei

import pymysql.cursors

# 获取链接
connection = pymysql.Connect(host='localhost',
                             user='root',
                             password='123456',
                             db='wikiurl',
                             charset='utf8mb4')
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql = 'select `urlname`,`urlhref` from `urls` where `id` IS not NULL '
        # 执行sql语句
        count = cursor.execute(sql)
        print(count)
        # 询前三条
        # result = cursor.fetchmany(size=3)
        # 查询全部
        result = cursor.fetchall()
        for res in result:
            print(res)
finally:
    connection.close()
