# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2019-05-13 8:44
# Author:Wangyafei
import numpy as np
import pandas as pd

#vdf = pd.DataFrame(pd.read_csv('name.csv', header=1))
# df = pd.DataFrame(pd.read_Excel('name.xlsx'))

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age',
                           'price'])
