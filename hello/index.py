a = 'bob said \"I\'m ok\"'
print a
b = r'''bob said "I'm ok"'''
print b
c = ['a','b','c']
print c[1]
c.append('d')
print c
c.insert(0,'e')
print c
print c[1]
c.pop(0)
print c
c[0] = 'f'
print c
a
age = 18
if age >= 20:
    print 'you age is', age
    print 'adult'
elif age >= 15:
    print 'yi cheng nian'
else:
    print 'fales'
d = ['li','wang','zhao','qin','su','han']
for name in d:
    print name
    