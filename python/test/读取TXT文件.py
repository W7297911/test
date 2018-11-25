# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-25 15:37
# Author:Wangyafei
from urllib.request import urlopen
import pdfminer

html = urlopen('https://en.wikipedia.org/wiki/Wikipedia')
print(html.read().decode('utf-8'))
