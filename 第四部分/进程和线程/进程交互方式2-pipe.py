#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from multiprocessing import Process,Pipe
#通过管道实现

def f(conn):
    conn.send([42,None,"from child 1"])
    conn.send([42,None,"from child 2"])
    print("from parent process:", conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe() # 管道生成，返回两个对象，一个是主进程， 一个子进程(管道这一头，管道那一条，谁是父子无所谓）
    # 把其中一头传递给子进程，然后启动
    # 此处说明，如果把child_conn 传递给子进程，recv的时候就要使用 parent_conn.recv()
    # 反之将parent_conn 传递给 子进程，recv的时候要使用 child_conn.recv()
    # 只是我们定义的 父子 对象，其实这两个对象是平行的，我们定义父子，只是为了便于区分
    # 父进程 Recv ，子进程就是send，然后close
    # 儿子发多次，父亲就要收多次
    # 同样父进程也可以发，子进程来收
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv()) # 子进程发，父进程收
    print(parent_conn.recv())
    parent_conn.send("from farther") # 父进程发，子进程收
    p.join()

    # 收发是一一对应的，不然就会出现一放卡住等到接收

