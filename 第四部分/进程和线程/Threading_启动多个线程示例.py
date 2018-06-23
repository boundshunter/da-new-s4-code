#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import threading
import time

# class MyThread(threading.Thread):
#     def __init__(self,n):
#         super(MyThread,self).__init__()
#         self.n = n
#
#     def run(self):
#         print("running task:",self.n)
#         time.sleep(2)

def run(n):
    print("running task:",n,threading.current_thread())
    # print(threading.current_thread())
    time.sleep(2)


start_time = time.time()
tobjs = []
for i in range(1,50):
    t = threading.Thread(target=run,args=("t-%s"% i,))
    t.setDaemon(True) # 把当前线程变成为守护线程，守护线程，程序默认是不会等待结束的,不需要t.join去等待线程结束，
                      # 守护线程相当于 仆人，主线程不会去管它是否执行完毕，所有就不会执行等到的2s
    t.start()

    tobjs.append(t)

# for t in tobjs:
#     t.join()  # = wait() 等待执行结束
# t.join() 单独写外面只等待最后一次，

# 把每一次执行的对象存入列表，然后循环去等到每一次的执行结果，

print("all thread has finished",threading.current_thread(),threading.active_count())
print("cost time:",time.time()-start_time,threading.current_thread(),threading.active_count())

# threading.current_thread() # 查看当前线程是否为主线程
# threading.active_count() # 查看当前活动线程的个数


'''
应用场景：
写一个socket server
每个链接过来就启动一个新线程
如果手动停掉socket server,这种情况是不会等待线程结束的
此种情况下，所有client都属于守护线程 (主线程是不会等待守护线程结束的)
'''