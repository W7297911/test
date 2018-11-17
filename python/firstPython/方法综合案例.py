class Game(object):
	# 历史最高分
	top_score = 0

	def __init__(self, player_game):
		self.player_name = player_game

	@staticmethod
	def show_help():
		print("游戏帮助信息: 让僵尸进入大门")

	@classmethod
	def show_top_score(cls):
		print("历史记录 {}".format(cls.top_score))

	def start_game(self):
		print("{} 开始游戏了。。。。".format(self.player_name))


# 1.查看游戏的帮助信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
game.start_game()


# 注意：如果方法内部，既需要访问实例属性，又要访问类属性，应该定义成实例方法
