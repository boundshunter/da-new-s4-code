#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
# greenlet 需要安装 gevent
# greenlet 手动切换
# gevent 是自动切换，gevent封装了greenlet


# 手动切换示例
from greenlet import greenlet

def func1():
    print(12) #2
    gr2.switch()#3
    print(34)#6
    gr2.switch()#7
    print(111)#10
def func2():
    print(56)#4
    gr1.switch()#5
    print(78)#8
    gr1.switch()#9

if __name__ == '__main__':
    gr1 = greenlet(func1)  # 启动一个协程
    gr2 = greenlet(func2)
    gr1.switch() # 先启动func1 步骤说明   # 1