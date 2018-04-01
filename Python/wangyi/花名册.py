#coding=utf-8
#1.定义一个列表，里面有一些名字
names=['xiaoming','xiaohua','xioageng','xiaoleng']
#2.获取一个要查找的名字
insertname=input("请输入您的名字：")
#3.判断是否存在，并显示相应的提示
findflag=0
for name in names:
	if name == insertname:
		findflag=1
		break#如果在前面已经找到了需要的名字，那么就结束循环，因为剩下的不会再进行判断，所以提升了程序的运行效率

	#else:
	#	findfalg=0
if findflag==1:
	print("找到了")
else:
	print("没有找到")
	names.append(insertname)
print("-"*30)
print(names)
