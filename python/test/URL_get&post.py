from urllib import request
from urllib.request import urlopen

# 1.不加表头
# req = urlopen("http://www.baidu.com")
# resurt = req.read().decode("utf-8")
# print(resurt)

# 2.加表头

# req = request.Request("http://ww.baidu.com")
# req.add_header("User-Agent",
#                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
# resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))

# 3.POST请求
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
    ("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("DepartueSearchDate", "018/11/26"),
    ("DepartueSearchTime", "13:30"),
    ("StartStationName", "南港站"),
    ("EndStationName", "台北站"),
    ("SearchType", "S")
])
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")

resp = urlopen(req, data=postData.encode("utf-8"))
print(resp.read().decode("utf-8"))
