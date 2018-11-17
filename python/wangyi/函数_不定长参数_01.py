def test2(a,b,*c,**d):
	print(a)
	print(b)
	print(c)
	print(d)

test2(11,22,33,44,55,66,num1=77,num2=88,num3=99,num4=100)
