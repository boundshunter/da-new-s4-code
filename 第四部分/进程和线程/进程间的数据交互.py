#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 使用进程q
from multiprocessing import Process,Queue

def f(qq):
    qq.put([11,None,False])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
# 父进程的q，通过启动子进程，传递给子进程，子进程put数据后，父进程可以通过传递的q建立通信访问到
# 进程交互的说明：
'''
实际上，有一个内存中间翻译，子进程首先将数据序列化到中间方内存，中间方（pickle)反序列化到父进程的内存中
实际上是两个不通的Q,只不过是因为有中间的pickle过程，我们是不知道的，但是他们是两个Q,相当于克隆了一份
才实现两个进程间的通信，两个进程的通信不是共享内存，是通过中间的一个pickle正反序列化到两块内存实现

两个进程，数据共享不是修改数据，只是一个进程的数据，通过Pickle传递给另外一个进程

'''