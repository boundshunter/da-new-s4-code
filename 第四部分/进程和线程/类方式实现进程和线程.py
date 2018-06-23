#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import threading


class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self): # 此处必须用run定义类中的函数，调用时候内部执行的是调用run
        print("running task:",self.n)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()
