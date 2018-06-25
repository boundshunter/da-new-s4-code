#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from multiprocessing import Process, Lock
# 这个锁的场景举例说明，你打印一个东西，由于比较损耗时间，下一个就插进来了，在这个没打印完成的进程中插入一段打印的输出
# 这个时候就需要这种锁，防止打印没完成之前，另外一个打印乱入
def f(lock, num):
    print("Hello,%s"% num)

if __name__ == '__main__':
    lock = Lock() #生成锁对象

    for num in range(10):
        Process(target=f, args=(lock, num,)).start()





