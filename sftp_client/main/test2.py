#!/usr/local/env python3
# encoding:utf-8

__author__ = "xiaopeng"


import threading
import datetime

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num1
    num1 += 1
    lock.release()
    return  num1

def run3():
    lock.acquire()
    res = run1()
    print("--------between run1 and run2-----")
    res1 = run2()
    lock.release()
    print(res,res1)

if __name__ == '__main__':
    num,num1 = 0,0
    lock = threading.RLock()
    for i in range(5):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())

else:
    print('----all threads done---')
    print(num, num1)

from multiprocessing import Process
import time


def f(name):
    time.sleep(2)
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()