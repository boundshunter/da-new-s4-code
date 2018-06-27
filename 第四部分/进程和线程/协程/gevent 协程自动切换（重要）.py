#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
'''
gevent 说明：
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在Gevent用到的主要模式是Greenlet,
    它是以C扩展模块形式接入python的轻量级协程，Greenlet 全部运行在主程序操作系统进程的内部，但他们被协作式的调用。
'''

import gevent
def Foo():
    print("Foo1")    # 1
    gevent.sleep(2) # 2 #7  #10 # 13 13-14等待1s
    print("Foo2")  #14

def Bar():
    print("Bar1")   # 3
    gevent.sleep(1) # 4 #8 #11 11-12等待1s
    print("Bar2") # 12

def func():
    print("running func") # 5
    gevent.sleep()# 6
    print("running func again") # 9

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(Foo),gevent.spawn(Bar),gevent.spawn(func)])
    #执行顺序
    gevent.sleep() # 可以判断io操作


# 切换过程是为了消除等待时间，当有函数执行完成之后，只在未完成之间切换，未完成函数之间如果有等待时间，先完成等待时间少的
# 然后在完成等待时间多的，一直在来回切换，直至最终完成