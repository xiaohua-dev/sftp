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

d = User_Manger("xiaopeng","xxx")


print(d.Check_User())


def Write_Json(arg):
    with open("xiaopeng.json", 'w+', encoding="utf-8") as  f:
        json.dump(arg,f)
        f.close()

aa= {
    "name": "xiaopeng",
    "password": "76cd438bd0e8899a61aff632ace54dbb",
    "path": "/home/xiaopeng",
    "space": 0 }

Write_Json(aa)


def Read_Json(*args):
    with open("xiaopeng.json", "r+", encoding="utf-8") as f:
        a = json.load(f)
        for i in args:
            print(a[i])

print("@@@@@")
Read_Json("name","space")
print("@@@@@")

