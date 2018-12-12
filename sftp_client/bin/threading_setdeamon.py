#!/usr/local/env python
# encoding:utf-8

import threading
import datetime
import time


def run(n):
    print('[%s]--------runing----------\n' %n)

    time.sleep(3)
    print('----done----')

def main():
    for i in range(5):
        t = threading.Thread(target=run, args=[i,])
        t.start()
        t.join()

        print('staring thread', t.getName())

m = threading.Thread(target=main, args=[])
m.setDaemon(True)
m.start()
m.join(timeout=10)
print("-----main thread done---------")