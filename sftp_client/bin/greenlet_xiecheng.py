#!/usr/bin/env python
# encoding:utf-8

from greenlet import greenlet



def t1():
    print(22)
    gr2.switch()
    print(44)
    gr2.switch()

def t2():
    print(53)
    gr1.switch()
    print(63)

gr1 = greenlet(t1)
gr2 = greenlet(t2)
gr1.switch()

import django