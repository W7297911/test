# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-23 16:34
# Author:Wangyafei

import unittest
import requests


class logintest(unittest.TestCase):
    def testlogin1(self):
        url = "https://mail.163.com"
        form = {"email": 18239949680, "password": 123456}
        r = requests.post(url, data=form)
        self.assertEqual(r.text, "登录成功")

    def testlogin2(self):
        url = "https://mail.163.com"
        form = {"email": "", "password": 123456}
        r = requests.post(url, data=form)
        self.assertEqual(r.text, "用户名不能为空")