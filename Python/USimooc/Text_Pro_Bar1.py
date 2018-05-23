#coding=utf-8
import time as T
scale = 10
print("----------执行开始----------")
for i in range(scale + 1):
	a = "*" * i
	b = "." * (scale - i)
	c = (i/scale)*100
	print("{:^3.0f}%[{}->{}]".format(c,a,b))
	T.sleep(0.1)
print("----------执行结束----------")