# !/usr/bin/env python
# encoding:utf-8

import os
from multiprocessing import Process,Manager

def f(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as  manger:
        d = manger.dict()

        l = manger.list(range(5))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)