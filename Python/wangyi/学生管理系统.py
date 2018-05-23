#coding=utf-8

#用来保存学生的所有信息
stuInfos = []
while True:
	#1.打印提示
	print("="*30)
	print("      学生管理系统V1.0")
	print("1.添加学生信息")
	print("2.删除学生信息")
	print("3.修改学生信息")
	print("4.查询学生信息")
	print("5.显示所有学生信息")
	print("0.退出系统")
	print("="*30)
	#2.获取功能的选择
	key = input("请输入功能对应的数字：")
	#3.根据用户的选择，进行相应的操作
	if key == "1":
		#添加学生信息
		#3.1提示并获取学生信息
		newName = input("请输入新学生的姓名：")
		#3.2提示并获取学生性别
		newSex = input("请输入新学生的性别：")
		#3.3提示并获取学生的手机号
		newPhone = input("请输入新学生的手机号：")
		newInfo = {}
		newInfo["name"] = newName
		newInfo["sex"] = newSex
		newInfo["phone"] = newPhone
		stuInfos.append(newInfo)
	elif key == "2":
		print("")
	elif key == "3":
		#修改学生信息
		#3.1提示获取需要修改的学生序号
		stuId = int(input("请输入要修改的学生的序号："))
		#3.2重新输入学生的信息(姓名，性别，手机号)
		#3.2.1提示并获取学生的姓名
		newName = input("请输入新学生的姓名：")
		#3.2提示并获取学生性别
		newSex = input("请输入新学生的性别：")
		#3.3提示并获取学生的手机号
		newPhone = input("请输入新学生的手机号：")
		stuInfos[stuId-1]["name"] = newName
		stuInfos[stuId-1]["sex"] = newSex
		stuInfos[stuId-1]["phone"] = newPhone
	elif key == "4":
		print("")
	elif key == "5":
		print("="*30)
		print("序号     姓名      性别       电话")
		i = 1
		for tempInfo in stuInfos:	
			print("%d        %s        %s         %s"%(i,tempInfo["name"],tempInfo["sex"],tempInfo["phone"]))
			i += 1
		print("="*30)
		#print(stuInfos)
	elif key == "0":
		exit()
