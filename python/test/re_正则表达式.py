# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-18 13:51
# Author:Wangyafei

# 这是一个Python正则表达式的练习文件
import re

info = re.match(r'python', 'Python test', re.I)  # re.I 不区分大小写
ds = info.group()
print(ds)

ma = re.match(r'.', 'a')  # . 匹配任意字符
print(ma.group())

ma1 = re.match(r'{.}', '{a}')
print(ma1.group())

ma2 = re.match(r'{[abc]}', '{a}')
print(ma2.group())

ma3 = re.match(r'{[a-z]}', '{b}')
print(ma3.group())

ma4 = re.match(r'{[a-zA-Z]}', '{C}')
print(ma4.group())

ma5 = re.match(r'{\w}', '{4}')  # \w:匹配单词字符[a-zA-Z0-9]; \W:非单词字符
print(ma5.group())

ma6 = re.match(r'{\W}', '{ }')
print(ma6.group())

ma7 = re.match(r'\[[\w]\]', '[a]')  # 外部[]需要用\转义
print(ma7.group())

ma8 = re.match(r'[A-Z][a-z]*', 'Aaaaaaa')
print('ma8:' + ma8.group())

ma9 = re.match(r'[1-9]?[0-9]', '10')
print('ma9:' + ma9.group())

ma10 = re.match(r'[a-zA-Z0-9]{6}@163.com', 'abc123@163.com')
print('ma10:' + ma10.group())

ma11 = re.match(r'[a-zA-Z0-9]{6,10}@163.com', 'abcd1234@163.com')
print('ma11:' + ma11.group())

ma12 = re.match(r'[0-9][a-z]*?', '1abc')
print('ma12:' + ma12.group())

ma13 = re.match(r'[0-9][a-z]+?', '1abc')
print('ma13:' + ma13.group())

ma14 = re.match(r'[0-9][a-z]??', '1abc')
print('ma14:' + ma14.group())

ma15 = re.match(r'^[\w]{4,10}@163.com$', 'abcd1234@163.com')
print('ma15:' + ma15.group())

ma16 = re.match(r'\Apython[\w]*@163.com$', 'python1234@163.com')
print('ma16:' + ma16.group())

# |  匹配左右任意一个表达式
ma17 = re.match(r'[1-9]?\d$|100', '99')
print('ma17:' + ma17.group())

# (ab) 括号内表达式作为一个分组
ma18 = re.match(r'^[\w]{4,10}@(163|126|139).com$', 'abcd1234@126.com')
print('ma18:' + ma18.group())

# \<number>   引用编号为num的分组匹配到的字符串
ma19 = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print('ma19:' + ma19.group())

# (?P<name>)  分组起一个别名
# (?P=name)   引用别名为name的分组匹配字符串
ma20 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
print('ma20:' + ma20.group())

'''

.           匹配任意字符（除\n）
[...]       匹配字符集   
\d          匹配数字
\D          匹配非数字
\s          匹配空白
\S          匹配非空白字符
\w          匹配单词字符[a-zA-Z0-9]
\W          匹配非单词字符
*           匹配前一个字符0次或者无限次
+           匹配前一个字符1次或者无限次
?           匹配前一个字符0次或者1次
{m}         匹配前一个字符m次
{m,n}       匹配前一个字符m-n次
*?/+?/??    匹配模式变为非贪婪（尽可能少匹配字符）
^           匹配字符串开头
$           匹配字符串结尾
\A          指定的字符串必须出现在开头
\Z          指定的字符串必须出现在结尾
|           匹配左右任意一个表达式
(ab)        括号内表达式作为一个分组
\<number>   引用编号为num的分组匹配到的字符串
(?P<name>)  分组起一个别名
(?P=name)   引用别名为name的分组匹配字符串

'''

# search  在一个字符串中查找匹配


# 查找1000
str1 = 'python is my first = 1000'
sh1 = re.search(r'\d+', str1)
print('sh1=' + sh1.group())

# findall  找到匹配，返回所有匹配部分的列表
str2 = 'python is my first，c++=1000, java=2000, python=1500'
sh2 = re.findall(r'\d+', str2)
print(sh2)
print(sum([int(x) for x in sh2]))




# sub  将字符串中匹配正则表达式的部分替换为其他值
str3 = 'python is my first = 999'
# 定义自增函数
def add1(add):
    val = add.group()
    num = int(val)+1
    return str(num)
sb = re.sub(r'\d+', add1, str3)
print(sb)

# split   根据匹配分割字符串，返回分割字符串组成的列表
str4 = 'let:C C++ Java Python, C##'
sp = re.split(r':| |, ', str4)
print(sp)