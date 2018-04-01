i=1
while i<=9:
#	print("* "*i, end="")
	j=1
	while j<=i:
		print("%d*%d=%-2d  "%(i,j,i*j), end="")
		j+=1
	print("")
	i+=1
