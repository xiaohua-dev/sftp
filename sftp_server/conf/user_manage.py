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


#c = User_Manger("xiaopeng",'dasdsada')
#c.Check_Passwd()
#c.Check_User()