# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-23 14:59
# Author:Wangyafei
import websocket
url = "ws://www.qq.com/"
ws = websocket.create_connection(url)
# ws.send("{"request":1111,"service":1001,"name":"qq"}")
new_msg = ws.recv()
print(new_msg)
print(url)
websocket.debug()

