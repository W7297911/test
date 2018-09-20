#coding=utf-8
def fahrenheit_converter(c):
    fahrenheit = c * 9/5 + 32
    return str(fahrenheit) + "℉"
# 请输入需要转换的摄氏度
rename = input("请输入转换的摄氏度：")
C2F = fahrenheit_converter(rename)
print(C2F)
