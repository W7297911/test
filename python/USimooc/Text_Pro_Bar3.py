#coding=utf-8
import time as T
scale = 100
print("执行开始".center(scale//2, "-"))
start = T.perf_counter()
for i in range(scale + 1):
	a = "*" * i
	b = "." * (scale - i)
	c = (i/scale)*100
	dur = T.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end=" ")
	T.sleep(0.05)
print("\n"+"执行结束".center(scale//2, "-"))