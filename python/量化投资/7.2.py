def weighted_sum(x1, x2, *y):
	sum = 0
	size = len(y)
	weight = 0.3 / size
	for i in y:
		sum = sum + weight * i
	sum = sum + 0.4 * x1 + 0.3 * x2
	return sum


print(weighted_sum(6, 7, 8, 9, 10))
