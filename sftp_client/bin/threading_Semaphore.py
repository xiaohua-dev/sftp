#!/usr/bin/env python
# encoding:utf-8


import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(2)
    print("run the thread: %s\n" %n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    num = 0
    for i in range(20):
        t = threading.Thread(target=run, args=[i,])
        t.start()


while threading.active_count() != 1:
    pass
else:
    print("-----all threads done-----")
    print(num)