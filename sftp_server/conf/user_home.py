#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import sys
import time
import os
import json

class User_home(object):
    def __init__(self, name, home_path):
        self.name = name
        self.home_path = home_path

    def Home_Path(self):
        command_result = os.popen('dir').read()
        print(command_result)


#b = User_home('xiaopeng', '/home/path')
#b.Home_Path()


import threading

def run(n):
    print("task", n)
    time.sleep(2)
    print("task done",n, threading.current_thread())

start_time = time.time()
t_obj = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.setDaemon(True)
    t.start()
    t_obj.append(t)


print("--------------all threads has finished",threading.current_thread(),threading.active_count())
print("cost", time.time() - start_time)