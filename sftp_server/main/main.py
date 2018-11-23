#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import socketserver
import time
import sys
import os
import threading
import json


class MyTCPHandler(socketserver.BaseRequestHandler):
    def Get(self,*args):
        print("aaaaa")
        self.request.send(b'success')

    def Create(self,*args):
        print("bbbbb")
        data = json.loads(self.data.decode())
        print(data["action"], data["home_path"], data["chmod"])
        command_status = os.popen('useradd %s' %(data["home_path"])).read()
        print(command_status)
        print("ccccc")
        self.request.send(b'sucess')

    def handle(self):
        while True:
            print(self.client_address[0])
            self.data = self.request.recv(1024).strip()
            print(self.data)
            cms_result = json.loads(self.data.decode())
            action = cms_result["action"]
            if hasattr(self, action):
                func = getattr(self,action)
                func(cms_result)
            else:
                print("the methond is not.")
                self.request.send(b'404')


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
