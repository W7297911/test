# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-16 20:53
# Author:Wangyafei

import cx_Oracle as oracle

db = oracle.connect('scott','123456','127.0.0.1:1521/orcl')

# create cursor
cursor = db.cursor()

# execute sql
cursor.execute('select sysdate from dual')

# fetch data
data = cursor.fetchone()

print('Database time:%s' % data)

# close cursor and oracle
cursor.close()
db.close()