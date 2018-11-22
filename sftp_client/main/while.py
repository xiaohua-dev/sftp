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

    def check_input(self):
        while True:
            raw_input = input(">>").strip()
            if len(raw_input) == 0:
                continue
            fun_result = raw_input.split()[0]
            if fun_result == "put":
                print("put result: %s" %(self.Put(raw_input.split()[0],raw_input.split()[1],raw_input.split()[2])))
                result = self.Put(raw_input.split()[0], raw_input.split()[1], raw_input.split()[2])
                self.client.send(json.dumps(result).encode("utf-8"))
                print(self.client.recv(1024))
            elif fun_result == "get":
                print("put result: %s" %(self.Get(raw_input.split()[0],raw_input.split()[1],raw_input.split()[2])))
                result = self.Get(raw_input.split()[0], raw_input.split()[1], raw_input.split()[2])
                self.client.send(json.dumps(result).encode("utf-8"))
            elif fun_result == "create":
                print("put result: %s" %(self.Create(raw_input.split()[0],raw_input.split()[1],raw_input.split()[2])))
                result = self.Create(raw_input.split()[0], raw_input.split()[1], raw_input.split()[2])
                self.client.send(json.dumps(result).encode("utf-8"))
            else:
                self.Help()

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

    def Create(self, create, home, chmod):
        msg_dir = {
            "action": create,
            "home_path": home,
            "chmod": chmod
        }
        return msg_dir




sftp = FtpClient()
sftp.Sftp_connect('localhost', 9999)
sftp.check_input()