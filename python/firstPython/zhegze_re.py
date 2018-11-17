import re
'''str1 = 'imooc  python'
res = re.compile(r'imooc').match(str1).group()
print(res)'''
result =[]
ma1 = re.match(r'[A-Z][a-z]*', 'Aa').group()
ma2 = re.match(r'[A-Z][a-z]', 'Aa').group()
ma3 = re.match(r'[A-Z][a-z]*', 'A').group()
ma4 = re.match(r'[A-Z][a-z]*', 'AAa').group()
ma5 = re.match(r'[_A-Za-z]+[_A-Za-z]*', '_AAa').group()
ma6 = re.match(r'[1-9]?[0-9]', '99').group()
ma7 = re.match(r'[A-Za-z][0-9A-Za-z]{7}@163.com', 'w7297911@163.com').group()
ma8 = re.match(r'[\w]{4,10}@163.com', 'w7297911@163.com').group()
ma9 = re.match(r'[1-9]?\d$|100', '100').group()
ma10 = re.match(r'[\w]{4,10}@(163|126).com', 'w7297911@126.com').group()
ma11 = re.match(r'<[\w]+>', '<book>').group()
ma12 = re.match(r'<([\w]+>)\1', '<book>book>').group()
ma13 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>').group()
for i in range(13):
    result.append(eval('ma'+str(i+1)))
    print('ma{:<2} =  {}'.format(i+1,result[i]))


#search(pattern, string, flags=0)
#在一个字符串中查找匹配
#findall(pattern, string, flags=0)
#找到匹配，返回所有匹配部分的列表
#sub(pattern,repl,string,count=0,flags=0)
#将字符串中匹配正则表达式的部分替换为其他值
#split(pattern,string,maxsplit=0,flags=0)
#根据匹配分割字符串，返回分割字符串组合成的列表
result1 = []
se1 = re.search(r'\d+', 'imooc python -> 1000, java -> 800').group()
se2 = re.findall(r'\d+', 'imooc python -> 1000, java -> 800, C++ -> 900')
se3 = re.sub(r'\d+','1001', 'imooc python -> 1000')
se4 = re.split(r':| ', 'imooc:python -> 1000')
for i in range(4):
    result1.append(eval('se'+str(i+1)))
    print('se{:<2} =  {}'.format(i+1,result1[i]))
