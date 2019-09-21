# 章节9.1
# priceSequence为某一股票交易日内开市后的日内成交价格序列
# 求开盘价
# 将股票日内交易一天内第一笔成交的成交价格定义为“开盘价”

import pmath
def OpenPrice(priceSequence):
	Open = priceSequence[0]
	return Open


# 求收盘价
# 将股票日内交易一天内最后一笔成交的成交价格定义为“收盘价”
def ClosePrice(priceSequence):
	Close = priceSequence[-1]
	return Close


# 求最高价
# 将股票日内交易价格序列的最大值定义为“最高价”
"""
def HighPrice(priceSequence):
	High = priceSequence[0]
	for price in priceSequence:
		if price > High:
			High = price
	return High
"""
def HighPrice(priceSequence):
	High = pmath.finMax(priceSequence)
	return High
# 求最低价
# 将股票日内交易价格序列的最小值定义为“最低价”
"""
def LowPrice(priceSequence):
	Low = priceSequence[0]
	for price in priceSequence:
		if price > Low:
			Low = price
	return Low
"""
def LowPrice(priceSequence):
	Low = pmath.finMin(priceSequence)
	return Low