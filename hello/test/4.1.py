#coding: utf-8
people = {
    'Alice':{
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth':{
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil':{
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
#针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
lables = {
    'phone': 'phone number',
    'addr': 'address'
}
name = raw_input('Name: ')
#查找电话号码还是地址?
request = raw_input('Phone number (p) or address(a)?')
#使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#如果名字是字典中的有效键才打印细信息:
if name in people: print "%s's %s is %s." %\
                         (name,lables[key],people[name][key])