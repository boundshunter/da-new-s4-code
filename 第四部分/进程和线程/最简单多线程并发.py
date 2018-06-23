#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import threading
import time

def run(n):
    print("task:",n)
    time.sleep(2)
t1 = threading.Thread(target=run,args=("k1",))
t2 = threading.Thread(target=run,args=("k2",))
t1.start()
t2.start()

# 程序说明，因为线程是并行的，等待2秒，t1,t2本来都需要各自等到2s，但是因为线程并行的，所以一共等待两秒

run("t1") # 此种无并发模式下，需要各自等待2s
run('t2')