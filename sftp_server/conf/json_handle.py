#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import json
import hashlib
import sys
import os

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(Base_dir)

class Json_handle(object):
    def __init__(self,json_name,arg):
        self.json_name = json_name
        self.arg = arg

    def Write(self):
        with open('%s/user_dir/%s.json' % (Base_dir,self.json_name), 'w+', encoding="utf-8") as f:
            json.dump(self.arg, f)
            f.close()
        return "The %s is save suceess...." %(self.json_name)


    def ReadJson(self):
        Json_file = open('%s/user_dir/%s.json' % (Base_dir,self.json_name), 'r+', encoding='utf-8')
        Read_file = json.load(Json_file)
        js_name = Read_file["user_name"]
        return Read_file

