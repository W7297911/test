#a = 2
#b = range(6)
#for i in b:
#print(a**0,a**1,a**2,a**3,a**4,a**5)


Tempstr = input()
if  Tempstr[0:3] in ['RMB']:
    C = eval(Tempstr[3:])/6.78
    print('USD{:.2f}'.format(C))
elif Tempstr[0:3] in ['USD']:
    F = 6.78*eval(Tempstr[3:])
    print('RMB{:.2f}'.format(F))
else:
    print()