#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from multiprocessing import Pool
import time, os

def Foo(i):
    time.sleep(2)
    print("In process:",i)
    return i+100
def Bar(arg):
    print("回调时使用的进程id:",os.getpid(),"回调获取的参数为:",arg," Foo函数返回值：",arg)
if __name__ == '__main__':
    pool = Pool(processes=3) # 允许进程池同时放入3个进程 ，也可以写成 pool = Pool(3)
    print("主进程：",os.getpid())

    # pool 的参数说明示例2：
    # apply 同步 串行执行,改成 apply就一个一个执行了
    # apple_async 异步，并行执行
    # 此处 callback 为回调，回调其实是父进程执行的，从获取的getpid可以证明
    # 回调的场景，比如执行完某个程序，需要记录一条日志到数据库，这样调用回调写数据库，好处是，回调在父进程中执行
    # 只需要连接一次数据库，也可以在子进程写数据库，那样就每个子进程做一次数据库连接和写入，打开的连接数太多
    # 所以采用回调方式去写数据库(只建立一次数据库连接）

    for i in range(1,10):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
        # 回调是等待Foo执行完毕后才执行 Bar,否则不执行
        # 如果回调函数Bar有参数，则使用Foo执行完毕后返回的值，
        # 否则回调获取的参数为 None

    print("end")
    # 此处 注意，一定要先关闭进程池，在等待进程执行结束，官方固定写法，否则出错
    pool.close() #关闭进程池
    pool.join() #wait
