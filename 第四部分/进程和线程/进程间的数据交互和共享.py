#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# Manager
# 可以实现，字典，列表，锁，递归锁，命名空间，等等的一系列的功能

from multiprocessing import Process, Manager
import os
def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    # print(l)
if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() # 生成一个可在多进程中共享和传递的字典
        l = manager.list(range(5))# 生成一个可在多进程中共享和传递的列表，默认5个随机数

        process_list = [] # 用于存储进程对象，进程循环等待执行完毕 join()
        for i in range(10):
            p = Process(target=f, args=(d, l)) # 将字典和列表传入子进程
            # 生成子进程，将字典和列表传送给子进程
            p.start()
            process_list.append(p)
            # 将子进程对象放入 列表 用户循环等待 join
        for res in process_list:
            res.join()
        # print(d)
        print(l)
        print(d)
# 用专门的语法生成一个，可在多个进程之间传递和共享的 字典，列表 （ manager)
