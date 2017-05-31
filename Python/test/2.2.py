
#练习2.1
# luc = ['c',1989,05,27]
# lua = ['a',1876,03,23]
# lub = ['b',1776,05,34]
# database = [lua,lub,luc]
# print database

#练习2.2
#根据给定的年月日以数字形式打印出日期
months = ['january','february','march','april','may','june','july','august','september','october','november','december']
#以1~31的数字作为结尾的列表
endings = ['st','nd','rd'] + 17*['th']\
          + ['st','nd','rd'] + 7*['th']\
          + ['st']
year  = raw_input('Year:')
month = raw_input('Month(1-12):')
day   = raw_input('Day(1-31):')
month_number = int(month)
day_mumber   = int(day)
#记得要将月份和天数减1，以获得正确的索引
month_name = months[month_number-1]
ordinal = day + endings[day_mumber-1]
print month_name + '  ' + ordinal + '.  ' + year

