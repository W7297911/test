x = { 'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print x
print y