# !/usr/bin/env python
# encoding:utf-8


import threading
import multiprocessing
import time

def Mythread(name):
    print("the num is %s" %name)
    time.sleep(1)

def run(name):
    print("hello %s" % name)
    time.sleep(2)
    t = threading.Thread(target=Mythread, args=["largs",])
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=["name %i" % i])

        p.start()
        p.join(2)
