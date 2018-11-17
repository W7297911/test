#coding=utf-8
#daydayup02.py
dayfactor = 0.005
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("向上：{:.4f},向下：{:.4f}".format(dayup, daydown))
