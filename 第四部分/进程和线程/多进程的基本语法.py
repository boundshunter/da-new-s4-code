#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 使用多进程，实现多多核的利用，但是多进程之间的线程，无法共享数据
import multiprocessing
# 多进程和多线程语法进本相同
import time
import threading

# def thread_run():
#     print("thread_id:",threading.get_ident())
#
# def run(name):
#     time.sleep(2)
#     print("%s process start running..."% name)
#     t = threading.Thread(target=thread_run,)
#     t.start()
#     t.join()
# if __name__ == '__main__':
#     start_time = time.time()
#     for i in range(10):
#         p = multiprocessing.Process(target=run,args=("jjj-%s"%i,))
#         p.start()
#     p.join()
#     print(time.time() - start_time)

# 多进程方式同样相当于多线程，
# 启动10个进程，每个进程里面又启动一个线程

# linux 上每个进程都会默认有一个父进程，那个父进程，就是terminal自己
# eg:
import os
def info(title):
    print(title)
    print("module_name:",__name__)
    print("parent process id:",os.getppid()) # pid是进程号，ppid是父进程号
    print("curr process id:",os.getpid())

def f(name):
    info("called from child process func f")
    # print('hello',name)

if __name__ == '__main__':
    info("main process line")
    print("\n")
    p_p = multiprocessing.Process(target=f,args=("Baby",))
    p_p.start()