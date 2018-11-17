class Tool(object):
	# 使用赋值语句定义类属性，记录所有工具对象
	count = 0
	def __init__(self, name):
		self.name = name
		# 让类属性的值+1
		Tool.count += 1

# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("砍刀")
tool3 = Tool("钳子")
tool4 = Tool("榔头")
# print(Tool.count)
# print("工具对象总数：{}".format(tool1.count))
print("工具对象总数：{}".format(tool1.count))