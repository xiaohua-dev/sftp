#!/usr/local/env python3
# encoding:utf-8

__author__ = "xiaopeng"

import hashlib
import sys
import time
import os



class Md5_handle(object):
    def __init__(self, password):
        self.password = password

    def get_token(self):
        md5str = self.password
        m1 = hashlib.md5()
        m1.update(md5str.encode("utf-8"))
        token = m1.hexdigest()
        return token

