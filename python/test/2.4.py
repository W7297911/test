#序列成员资格示例
#检查用户名和PIN码
database = [
    ['albert','12345'],
    ['dilbert','1234'],
    ['smith','3421'],
    ['jones','12312']
]
username = raw_input('user name: ')
pin = raw_input('PIN code: ')

if [username,pin] in database:
    print 'Access granted'