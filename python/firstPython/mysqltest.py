#coding='utf-8'
import pymysql
con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',db='zhaiquan', charset='utf8mb4')
cur = con.cursor()
sql = 'select F1, ZZ_fang, ZZ_hang, ZZ_zhu from zz_meesager'
cur.execute(sql)
res = cur.fetchmany(10)
for data in res:
	print('-------------------------------------------------------')
	print('代码：{0}   发行人：{1}   所属行业：{2}   主体评级：{3}'.format(*data))
con.commit()
cur.close()
con.close()