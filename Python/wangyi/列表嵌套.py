import random
#1.定义一个列表，嵌套的列表
rooms = [[],[],[]]
#2.有一个列表，保存了8位老师的名字
teachers = ["A","B","C","D","E","F","G","H"]

#3.随机把8名老师的名字添加到 第一个列表中
for name in teachers:
	randomNum = random.randint(0,2)
	rooms[randomNum].append(name)

#print(rooms)
i = 1
for room in rooms:
	#print(room)
	print("办公室%d里面的老师姓名是："%i)
	for name in room:
		print(name,end="  ")
	print(" ")
	i =+ 1
