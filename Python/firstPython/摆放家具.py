class HouseItem:
	def __init__(self, name, area):
		self.name = name
		self.area = area
	def __str__(self):
		return '[{}] 占地 {:.2f}'.format(self.name, self.area)

	#1.创建家具

class House:
	def __init__(self, house_type, area):
		self.house_type = house_type
		self.area = area
		#剩余面积
		self.free_area = area
		#家具名称列表
		self.item_list = []
	def __str__(self):
		return ('户型：{}\n总面积：{:.2f}[剩余面积：{:.2f}]\n家具：{}'.format(
			self.house_type, self.area, self.free_area, self.item_list))
	def add_item(self, item):
		print('要添加{}'.format(item))
		#1.判断家具的面积
		if item.area > self.free_area:
			print('{}的面积太大了，无法添加'.format(item.name))
			return
		#2.将家具的名称添加到列表中
		self.item_list.append(item.name)

		#3.计算剩余面积
		self.free_area -= item.area
bed = HouseItem('席梦思', 40)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 20)
print(bed)
print(chest)
print(table)
my_house = House('两室一厅', 60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)