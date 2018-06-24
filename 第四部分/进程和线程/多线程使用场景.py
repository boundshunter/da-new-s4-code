#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
'''
io操作不占用cpu,运算才占用cpu
python 多线程 不适合cpu秘籍操作型任务，适合I/O密集型任务
使用多进程，每个进程一个线程，来实现多线程利用多核运算问题，但是
这多个进程之间的线程，无法共享数据
'''

