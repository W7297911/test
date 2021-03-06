#coding=utf-8

#用来保存学生的所有信息
stuInfos = []

#全局变量
newName = ""
newSex = ""
newPhone = ""
#1.打印提示
def printMenu():
    print("="*30)
    print("      学生管理系统V1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.显示所有学生信息")
    print("0.退出系统")
    print("="*30)

#获取一个学生信息
def getInfo():
	#global newName
	#global newSex
	#global newPhone
    #3.1提示并获取学生信息
	newName = input("请输入新学生的姓名：")
	#3.2提示并获取学生性别
	newSex = input("请输入新学生的性别：")
	#3.3提示并获取学生的手机号
	newPhone = input("请输入新学生的手机号：")
	return [newName,newSex,newPhone]

#添加一个新同学的信息
def addStuInfo():
	result = getInfo()
	newInfo = {}
	newInfo["name"] = result[0]
	newInfo["sex"] = result[1]
	newInfo["phone"] = result[2]

	stuInfos.append(newInfo)

#用来修改一个学生的信息
def modifyStuInfo():
	#3.1提示获取需要修改的学生序号
	stuId = int(input("请输入要修改的学生的序号："))
	#3.2重新输入学生的信息(姓名，性别，手机号)
	result = getInfo()
	stuInfos[stuId-1]["name"] = result[0]
	stuInfos[stuId-1]["sex"] = result[1]
	stuInfos[stuId-1]["phone"] = result[2]


while True:
	#1.打印提示
	printMenu()
	#2.获取功能的选择
	key = input("请输入功能对应的数字：")
	#3.根据用户的选择，进行相应的操作

	if key == "1":
		#添加学生信息
		addStuInfo()

	elif key == "2":
		print("")

	elif key == "3":
		#修改学生信息
		modifyStuInfo()

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
