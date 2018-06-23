#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# http://www.cnblogs.com/alex3714/articles/5230609.html
import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    print('--get num:',num )
    time.sleep(1)
    num  -=1 #对此公共变量进行-1操作

num = 100  #设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()


print('final num:', num )

'''
正常来讲，这个num结果应该是0， 但在python 2.7上多运行几次，会发现，最后打印出来的num结果不总是0，为什么每次运行的结果不一样呢？
哈，很简单，假设你有A,B两个线程，此时都 要对num 进行减1操作， 由于2个线程是并发同时运行的，所以2个线程很有可能同时拿走了num=100
这个初始变量交给cpu去运算，当A线程去处完的结果是99，但此时B线程运算完的结果也是99，两个线程同时CPU运算的结果再赋值给num变量后，
结果就都是99。那怎么办呢？ 很简单，每个线程在要修改公共数据时，为了避免自己在还没改完的时候别人也来修改此数据，
可以给这个数据加一把锁， 这样其它线程想修改此数据时就必须等待你修改完毕并把锁释放掉后才能再访问此数据。

*注：不要在3.x上运行，不知为什么，3.x上的结果总是正确的，可能是自动加了锁
'''

# 加锁版本

import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    print('--get num:',num )
    time.sleep(1)
    lock.acquire() #修改数据前加锁
    num  -=1 #对此公共变量进行-1操作
    lock.release() #修改后释放

num = 100  #设定一个共享变量
thread_list = []
lock = threading.Lock() #生成全局锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )

