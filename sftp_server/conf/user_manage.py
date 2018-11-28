#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import os
import time
import sys
import json
import hashlib

class User_Manger(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def Write(self, json_name):
        with open('%s.json'%(json_name), 'w+', encoding="utf-8") as f:
            json.dump(json_name,f)
            f.close()

    def ReadJson(self):
        Json_file = open("%s.json" %(self.name), 'r+', encoding='utf-8')
        Read_file = json.load(Json_file)
        js_name = Read_file["name"]
        return Read_file

    def Check_User(self):
        if self.name == self.ReadJson()["name"]:
            print("The %s name is exit" % self.name)
            print(self.ReadJson())
        else:
            print("The %s name is not exit." % self.name)

    def Check_Passwd(self):
        if self.password == self.ReadJson()["password"]:
            print("The %s password is right..." % self.name)
        else:
            print("The %s password is wrong..." % self.name)


c = User_Manger("xiaopeng",'dasdsada')
c.Check_Passwd()
c.Check_User()