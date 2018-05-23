#while循环
print("+="*20)
'''i = 0
while i<=10:
	print("韩欢欢，我爱你*******")
	i+=1
'''
i = 1
suma = 0
while i <=100:
	print("当前是第%d次执行循环"%(i+1))
	print("i=%d"%i)
	print("+"*20)
	if i%2 == 0:
		suma =suma + i
	i += 1
print("1-100的偶数和为：%d"%suma)

