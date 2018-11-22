#!/usr/bin/env python
# encoding:utf-8

__author__ = 'xiaopeng'

import sys
import time
import os
import json

class User_home(object):
    def __init__(self, name, home_path):
        self.name = name
        self.home_path = home_path

    def Home_Path(self):
        command_result = os.popen('dir').read()
        print(command_result)


b = User_home('xiaopeng', '/home/path')
b.Home_Path()