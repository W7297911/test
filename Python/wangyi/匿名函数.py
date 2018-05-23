def test(a,b):
	return a+b

#用lambda关键词能创建小型匿名函数，这种函数得名于省略了用def声明函数的标准步骤。语法如下：lambda [arg1[,arg2,arg3,......argn]]:expression
niming = lambda a,b:a+b

print(test(5,9))
print(niming(21,10))
