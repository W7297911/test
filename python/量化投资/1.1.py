# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2019-05-18 23:29
# Author:Wangyafei

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock_data = pd.read_csv('d:\\tams\\qq.csv', encoding='gbk')
print(stock_data)
exit()
# print(stock_data['Open'])

# 排序
stock_data = stock_data.sort_values(by=['Open', 'Volume'])

stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# 排序
stock_data.sort_values(by=['Date', 'Volume'])

# 筛选交易日期
stock_data = stock_data[stock_data['Date'] > pd.to_datetime('20120828')]

# 去除
stock_data=stock_data[stock_data['High'] != 6.5]

# 计算平均值
output=pd.DataFrame()
output['汇总']=stock_data.groupby('Open')['High'].mean()
#output.to_csv('d:\\tams\\baiyun1.csv',encoding='gbk')
print(output)

