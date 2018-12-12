#!/usr/local/env python
# encoding:utf-8

import threading
import datetime
import time

def say(num):
    print("runing on number:%s " %num)
    time.sleep(2)

if __name__ == "__main__":
    t1 = threading.Thread(target=say, args=[1,])
    t2 = threading.Thread(target=say, args=[2,])

    #t1.start()
    #t2.start()

    #t1.join(timeout=60)
    #t2.join(timeout=60)

    #print(t1.getName())
    #print(t2.getName())



class Mythread(threading.Thread):
    def __init__(self, num):
        self.num = num
        threading.Thread.__init__(self)

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)


if __name__ == '__main__':
    for i in  range(10):
        t1 = Mythread(i)
        t1.start()
        print(t1.getName())

    #简单版多线程机继承
    #t1 = Mythread(1)
    #t1.start()
    #t2 = Mythread(1)
    #t2.start()