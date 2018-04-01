#coding=utf-8
#定义一个列表，用来存储所有的名字
name = []
while True:
	#1.打印提示
	print("="*35)
	print("       欢迎使用数据管理系统 V6.8")
	print(" 1: 添加新名字")
	print(" 2: 删除一个名字")
	print(" 3: 修改一个名字")
	print(" 4: 查询一个名字")
	print(" 5: 遍历所有的名字")
	print(" 0: 退出系统")
	print("="*35)
	#2.获取要操作的数字
	key = input("请输入您要的数字：")
	#3.根据选择，来做相应的事情
	if key == "1":
		#3.1 提示用户输入一个新名字
		insertName = input("请输入要添加的名字：")
		#3.2 把用户输入的名字添加到列表中
		name.append(insertName)

	elif key == "2":
		remove = input("请输入您要删除的名字：")
		name.remove(remove)
	elif key == "3":
		xiugai = input("请输入您要修改的名字：")
		xiugaihou =input("请输入修改后的名字：")
		name[name.index(xiugai)] = xiugaihou
	elif key == "4":
		findx = input("请输入要查找的内容：")
		if findx in name:
			print("您查找的名字在列表中**%s**"%findx)
			print("列表中有:", end='')
			print(name.count(findx))
		else:
			print("列表中没有您要找的名字")
	elif key == "5":
		print(name)
	elif key == "0":
		exit()
