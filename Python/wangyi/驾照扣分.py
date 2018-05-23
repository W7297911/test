#1.请输入您但前的分数
source=int(input("请输入您当前的分数："))
#2.请输入您违反的交通规则（1：闯红灯，2：违章停车）
guize=input("请输入您违反的交通规则（1：闯红灯，2：违章停车）：")
#3.扣分
if guize == "1":
	source -= 6

if guize == "2":
	source -= 3
#4.显示当前的分数，以及是否需要参加学习
print("您当前的分数是：%d"%source)
if source <= 0:
	print("您当前的分数是：%d,请您去车管所学习"%source)
else:
	print("您当前的分数是：%d"%source)
