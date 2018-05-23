glo_a = 100
glo_list = [11,22,32,34]
def A():
	#global glo_a
	glo_a = 202
	print(glo_a)


	glo_list.append(54)
	print(glo_list)

def B():
	print(glo_list)
	print(glo_a)
A()	
B()
