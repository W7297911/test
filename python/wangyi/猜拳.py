import random
#1.提示用户并获取一个数字
player = int(input("请选择（1：剪刀，2：石头，3：布）："))
#2.让电脑生成一个数字
computer = random.randint(1,3)
print("computer----->>:%d"%computer)
#3.判断输赢，并显示相应结果
if (player==2 and computer ==1) or  (player==3 and computer ==2) or  (player==1 and computer ==3):
	print("您赢了，回家睡觉了-----")
elif player==computer:
	print("平局了，决战到天亮吧-----")
else:
	print("您输了，是否还要继续啊----")
