class Dog(object):
	def __init__(self, name):
		self.name = name
	def game(self):
		print("{} 蹦蹦跳跳的玩耍".format(self.name))


class XiaoTianDog(Dog):
	def game(self):
		print("{} 飞到天上去玩耍。。。。".format(self.name))


class Persion(object):
	def __init__(self, name):
		self.name = name

	def game_with_dog(self, dog):
		print("{} 和 {} 快乐的玩耍。。。。".format(self.name, dog.name))

		# 让狗玩耍
		dog.game()
# 1.创建一个狗对象
#wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 2.创建一个小明对象
xiaoming = Persion("小明")
# 3.让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)

