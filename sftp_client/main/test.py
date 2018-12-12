#!/usr/local/env python3
# encoding:utf-8

__author__ = "xiaopeng"


from md5_api import Md5_handle

#aa = Md5_handle("xiaopeng")
#print(aa.get_token)

import time
import threading
import datetime


# def run(n):
#     print('[%s]------running----\n' % n)
#     time.sleep(22)
#     print('--done--')
#
#
# def main():
#     for i in range(5):
#         t = threading.Thread(target=run, args=[i, ])
#         t.start()
#         t.join(1)
#         print('starting thread', t.getName())
#
#
# m = threading.Thread(target=main, args=[])
# m.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
# m.start()
# m.join(timeout=2)
# print("---main thread done----")


def run(n):
    print("%s================runing=================\n" % n)
    time.sleep(2)
    print("over")

def main():
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()
        t.join(1)
        print("starting thread.", t.getName())

a = threading.Thread(target=main, args=())
a.setDaemon(True)
a.start()
a.join(timeout=4)
print("----main thread done------")


