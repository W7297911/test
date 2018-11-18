# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-18 18:33
# Author:Wangyafei

import re
import urllib.request as ur2
req = ur2.urlopen('http://www.imooc.com/course/list')
buf = req.read()
replacesrc = re.sub(r'src="','http:', buf.decode('utf-8'))
listurl = re.findall(r'http:.+\.jpg', replacesrc)
print(listurl)

i = 0
for url in listurl:
    f = open(str(i)+'.jpg', 'wb+')
    req = ur2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1
