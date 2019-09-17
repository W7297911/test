# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2019-05-18 23:29
# Author:Wangyafei

grade = 95
if grade > 90:
	print("Excellent  job")
elif all([grade > 70, grade < 90]):
	print("Good  job")
else:
	print("It's uncommon")


def my_abs(x):
	if x > 0:
		return x
	else:
		return -x


a = 3
b = 5
print(my_abs(a - b))



