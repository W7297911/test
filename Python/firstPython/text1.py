
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
r = requests.get('http://python123.io/ws/demo.html')
print(r.text)
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())