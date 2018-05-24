#coding:utf-8
import requests
'''keyword = 'python'
try:
	kv = {'q':keyword}
	r = requests.get("http://www.so.com/s",params=kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print("爬去数据失败")
'''
import os
'''url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
root = 'd://pics//'
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			r.close()
			print('文件保存成功')
	else:
		print('文件已存在')
except:
	print('爬去失败')
'''
'''r = requests.get('http://python123.io/ws/demo.html')
print(r.text)
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())'''

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simhei']
plt.rcParams['axes.unicode_minus']=False
y1=[10,13,25,40,30,50,40,38,40,35,29,34,38,21,34,35,42,12,34,45]
x1=range(0,20)
x2=range(0,20)
y2=[5,8,10,30,20,40,30,31,38,30,28,23,34,12,32,22,32,12,23,34]
plt.plot(x1,y1,label='Frist line',linewidth=3,color='r',marker='o',
markerfacecolor='blue',markersize=5)
plt.plot(x2,y2,label='second line')
plt.xlabel('日期')
plt.ylabel('销量')
plt.title('中国香港公司\n销售数据')
plt.legend()
plt.show()
