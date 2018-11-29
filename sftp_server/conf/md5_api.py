#!/usr/bin/env python
# encoding:utf-8

import json
import hashlib
from user_manage import User_Manger

class Md5_handle(object):
    def __init__(self,password):
        self.password = password

    def get_token(self):
        md5str = self.password
        m1 = hashlib.md5()
        m1.update(md5str.encode("utf-8"))
        token = m1.hexdigest()
        return token


print(Md5_handle('xiaopeng').get_token())
