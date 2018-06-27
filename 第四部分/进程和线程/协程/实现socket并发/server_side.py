#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys, time, socket, gevent
from gevent import  monkey
monkey.patch_all() # 记录所有io操作

def Server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(500) # 允许500个并发
    while True:
        cli, addr = s.accept()
        gevent.spawn(HandleRequest,cli)

def HandleRequest(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:",data)
            conn.send(data)
            print("send:",conn.send(data))
            if not data: #null
                conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print("err",e)
    finally:
        conn.close()

if __name__ == '__main__':
    Server(8082)
