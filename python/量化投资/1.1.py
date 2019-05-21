# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2019-05-18 23:29
# Author:Wangyafei

import pandas as pd
import numpy as n

# 读取CSV文件
data = pd.read_csv('E:\SRCB\Money.csv', encoding='gbk')
# 读取CSV文件的某一列
data = data['m']
# data['today']=pd.to_datetime('2019-05-21')
print(data)
