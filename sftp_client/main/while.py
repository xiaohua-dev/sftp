#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import socket
import time
import sys
import json

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def Sftp_connect(self, ip, port):
        self.client.connect((ip,port))

    def Help(self):
        msg = """
            get filename
            put filename
            create user
            ls
            cd ../..
        """
        print(msg)

    def Login_choise(self):
        print("""
            欢迎登录到简单版的sftp服务，登录|注册
        """)
        while True:
            first_input = input("登录|注册 >>").strip()
            if len(first_input) == 0:
                continue
            if first_input == "登录":
                self.check_input()
            elif first_input == "注册":
                self.Create_user_input()
            elif first_input == "exit":
                print("退出sftp服务")
                exit()



    def check_input(self):
        while True:
            raw_input = input("输入账号>>").strip()
            raw_passwd_input = input("请输入密码>>").strip()
            if len(raw_input) == 0:
                continue
            if len(raw_passwd_input) == 0:
                continue
            if raw_input == "exit":
                print("退出sftp服务系统")
                exit()
            fun_result = raw_input.split()[0]
            if hasattr(self,fun_result):
                func = getattr(self, fun_result)
                return_result = func(raw_input.split()[0], raw_input.split()[1], raw_input.split()[2])
                self.client.send(json.dumps(return_result).encode("utf-8"))
                print(self.client.recv(1024))
            else:
                self.Help()

    def Create_user_input(self):
        while True:
            action_input = input("接下来的动作>>").strip()
            create_user_input = input("请输入新建账号>>").strip()
            create_passwd_input = input("输入新用户密码>>").strip()
            if len(create_user_input) == 0:
                continue
            elif len(create_passwd_input) == 0:
                continue
            elif len(action_input) == 0:
                continue

            if hasattr(self, action_input):
                func = getattr(self, action_input)
                return_create_result = func(action_input, create_user_input, create_passwd_input)
                print(return_create_result)
                self.client.send(json.dumps(return_create_result).encode("utf-8"))
                print(self.client.recv(1024))


    def Put(self, put, filename, filesize):
        msg_dir = {
            "action": put,
            "filename": filename,
            "size": filesize,
            "overridden": True
        }
        return msg_dir
    def Get(self, get, filename, status):
        msg_dir = {
            "action": get,
            "filename": filename,
            "status": status
        }
        return msg_dir

    def Create(self, action, user_name, password):
        msg_dir = {
             "action": action,
             "user_name": user_name,
             "password": password
        }
        return msg_dir




sftp = FtpClient()
sftp.Sftp_connect('39.105.128.207', 9999)
sftp.Login_choise()
sftp.check_input()