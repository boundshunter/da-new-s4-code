#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，
# 那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。

# 启动了20个线程，每次执行5个，每执行完一个，在进入一个，不需要5个同时完成在同时释放

# 防止同一时间 启动的线程过多，将cpu跑慢，系统带慢
import threading,time

def run(n):
    semphore.acquire()
    time.sleep(1)
    print("run the thread:%s\n"%n)
    semphore.release()


if __name__ == '__main__':
    semphore = threading.BoundedSemaphore(5) # 最多同时允许5个线程一起运行
    for i in range(22):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    # print(threading.active_count())
    pass
else:
    print("all thread done".center(30,'-'))