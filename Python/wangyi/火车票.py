chepiao = 0 #0表示没有购票，1表示已购票
changdu = 11#单位为cm，表示的是刀子的长度，超过10cm禁止携带
if chepiao == 1:
	print("您已购票，可进站进行安检")
	if changdu > 10:
		print("请上交您的刀具，否则无法通过安检")
	else:
		print("请带好车票去指定候车室")
else:
	print("请先购票，然后再过安检")
