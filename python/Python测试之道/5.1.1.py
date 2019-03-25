# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-23 13:24
# Author:Wangyafei

import requests
# r = requests.方法（url,headers,data,……）
url = "http://www.163.com"
'''
response = requests.get(url)
print(response.status_code)
head = response.headers
for key, value in head.items():
    print(str(key)+":"+str(value))

# print(head)
# print(response.text)
'''

c = {"JSESSIONID-WYTXZDL":"IrFhBU2H%2BSqzd79Yf5JKGvV5k2buhgyDeGX0rYkYBifumi5Okp676DKHtunpgfTGI%2FNGdH8RDGTyZo0Lr0GzalFIQBldEFFOpaHaIyIOcRPPvteLHZBGZxG45x%2F6OZY4967MGBAVa%5Cq3QpDULrlNDDvSLSRvQkQdLWo%2B04Xvm5v%2FAjpj%3A1545545905389"}
h = {"User-Agent":"Android/H60-L01/4.4.2/"}
# response = requests.get(url, headers=h)
response = requests.get(url, cookies=c)
# response = requests.post(url, cert=("/path/client.cert","/path/client.key"))
print(response.status_code)
print(response.headers)
print(response.text)