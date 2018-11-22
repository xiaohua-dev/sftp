#!/usr/bin/env python
# encoding:utf-8

import json
import hashlib
from user_manage import User_Manger

def get_token():
    md5str = "xiaopeng"
    m1 = hashlib.md5()
    m1.update(md5str.encode("utf-8"))
    token = m1.hexdigest()
    return token


print(get_token())

d = User_Manger("xiaopsng","xxx")


print(d.Check_User())