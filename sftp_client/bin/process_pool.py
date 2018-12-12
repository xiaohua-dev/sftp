# !/usr/bin/env python
# encoding:utf-8

from multiprocessing import Process,Pool
import os
import time

def foo(i):
    time.sleep(2)
    print("process id: ",os.getpid())
    return i+100

def f(arg):
    print('the poil is ending.',arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(10):
        # pool.apply(func=foo,args=(i,))  #串行执行进程池
        # pool.apply_async(func=foo, args=(i,))  # 并行行执行进程池
        pool.apply_async(func=foo, args=(i,), callback=f)  # 并行行执行进程池,callback是指回调的意思，当进程执行完之后，执行一个命令
    print('end')
    pool.close()
    pool.join()