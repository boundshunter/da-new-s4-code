#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
队列的特点：
queue.Queue(maxsize=0) # 先进先出
queue.LifoQueue(maxsize=0) # Lifo =  last in firt out ，后进先出 比如卖水果，新鲜的卖的好
queue.PriorityQueue(maxsize=0) # 存储时可设置优先级的队列 格式：Q.put((4,'aa')) ，权重小，先出

'''

import queue
# q = queue.Queue()
# q.put('d1')
# q.put('d2')
# q.put('d3')
# # FLAG = True
# # while FLAG:
# #     try:
# #         q.get_nowait()
# #     except queue.Empty as e:
# #         print(e)
# #         FLAG = False
# q.get()
# q.get()
#
# q.get()
# print(q.queue)  # 查看队列内容
# q.qsize() # 查看队列个数


Q = queue.PriorityQueue(maxsize=0)
Q.put((4,'aa'))
Q.put((2,'bb'))
Q.put((1,'cc'))
Q.put((3,'dd'))
print(Q.get())
print(Q.get())
print(Q.get())
print(Q.get())

