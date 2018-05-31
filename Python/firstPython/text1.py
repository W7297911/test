
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
print(soup.prettify())
'''
'''class Cat:
	def eat(self):
		#哪一个对象调用的方法，self就是哪一个对象的引用
		print('{}爱吃鱼'.format(self.name))
	def drink(self):
		print('{}要喝水'.format(self.name))
#创建猫对象

Tom = Cat()
#可以使用 .属性名  利用赋值语句就可以了
Tom.name = '小小猫'
Tom.eat()
Tom.drink()'''
'''class Cat:
	def __init__(self, new_name):
		print('第一个初始化方法')
		#self.属性名 = 属性的初始值
		self.name = new_name
	def eat(self):
		print('{}爱吃鱼'.format(self.name))
#使用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat('Tom')
print(tom.name)
lazy_cat = Cat('大懒猫')
lazy_cat.eat()'''


'''
class Cat2:
	def __init__(self, new_name):
		self.name = new_name
		print('{}来了'.format(self.name))
	def __del__(self):
		print('{}去了'.format(self.name))
	def __str__(self):
		return '我是小猫[{}]'.format(self.name)
tom = Cat2('Tom')
print(tom)
print('*'*50)

'''


#1.小明体重75.0公斤
#2.小明每次跑步会减肥0.5公斤
#3.小明每次吃东西体重增加1公斤
class Person:
	def __init__(self, name, weight):
		#self.属性 = 形参
		self.name = name
		self.weight = weight
	def __str__(self):
		return '我的名字叫{}，体重是{:.2f}公斤。'.format(self.name, self.weight)
	def run(self):
		print('{}爱跑步，跑步锻炼身体。'.format(self.name))
		self.weight -= 0.5
	def eat(self):
		print('{}是吃货，吃完这顿再减肥。'.format(self.name))
		self.weight += 1
xiaoming = Person('小明', 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
xiaomei = Person('小美', 45)
xiaomei.run()
xiaomei.eat()
print(xiaomei)
print(xiaoming)







