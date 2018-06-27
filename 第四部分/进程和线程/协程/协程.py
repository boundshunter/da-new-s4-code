#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
协程：又称微线程，纤程，是一种用户态的轻量级线程
协程拥有自己的寄存器上下文和栈，当协程调度切换时，将寄存器上下文和栈保存到其他地方，
在切回来的时候，恢复之前保存的寄存器上下文和栈
因此：协程能保留上一次调用的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态
    换种说法，进行上一次离开时所处的逻辑状态
协程好处：
1、无需线程和上下文切换的开销
2、无需原子操作锁定及同步的开销
3、方便切换控制流，简化变成模型
4、高并发-高扩展-低成本：一个cpu支持上万个协程都不是问题，所以很适合用于高并发处理

总结： 高并发处理，协程   epoll，例如：nginx

缺点：
1、无法利用多核资源（单线程），协程的本质是单线程，不能运用多核，协程需要和进程配合才能运用在多cpu上（当然，我们
   平时的应用都没这个必要，除非是cpu密集型应用）
2、进行阻塞（Blocking) 操作，操作入（IO时）会阻塞掉整个程序
'''
# yield的实现简单协程的例子（单线程实现多并发效果）
import time

def Consumer(name): # 函数第一次调用，有yield 不执行，next的时候才执行，next方法在producer中
    print("---->%s starting eat baozi..."% name)
    while True:
        New_baozi = yield
        print("[%s] is eating baozi [%s]"% (name,New_baozi))
        # time.sleep(1)

def Producer():
    r = con1.__next__()
    r = con2.__next__()
    n = 1
    while n < 5:
        print("producer is making baozi %s"% n)
        n += 1
        con1.send(n) # send 两个作用：将值传送给yield的New_baozi
        con2.send(n)



if __name__ == '__main__':
    con1 = Consumer('c1')
    con2 = Consumer('c2')
    p1 = Producer()

