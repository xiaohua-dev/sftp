#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import socket
import time
import sys
import os
import threading
import json
import hashlib
from user_manage import User_Manger

print("""
要求：

用户加密认证
允许同时多用户登录
每个用户有自己的家目录 ，且只能访问自己的家目录
对用户进行磁盘配额，每个用户的可用空间不同
允许用户在ftp server上随意切换目录
允许用户查看当前目录下文件
允许上传和下载文件，保证文件一致性
文件传输过程中显示进度条
附加功能：支持文件的断点续传
""")


class Sftp_api(object):
    def __init__(self, name, password, space, path, signal):
        self.name =name
        self.password = password
        self.space = space
        self.path = path
        self.signal = signal

    def ReadJson(self):
        Json_file = open("%s.json" %(self.name), 'r+', encoding='utf-8')
        Read_file = json.load(Json_file)
        js_name = Read_file["name"]
        return Read_file

    def Client_user_Signal(self):
        status_signal = "注册"
        if self.signal == status_signal:
            a = User_Manger(self.name, self.password)
            a.Check_User()
            a.Check_Passwd()
            print("a")

    def Check_Space(self):
        Json_file = open("package.json", 'r+', encoding='utf-8')
        Read_Json = json.load(Json_file)
        print(Read_Json["space"])


a = Sftp_api("xiaopeng","76cd438bd0e8899a61aff632ace54dbb",11,'/home/xiao',"注册")
a.Client_user_Signal()
#a.Check_Space()
