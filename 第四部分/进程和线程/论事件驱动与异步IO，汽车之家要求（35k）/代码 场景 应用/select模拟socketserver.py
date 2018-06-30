#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
# 通过echo server 例子了解 select 是如何通过单进程实现同时处理多个socket连接的

import select
import socket
import sys
import queue

# 非阻塞模式下才能实现Io多路复用
# create a tpc/ip socket
server = socket.socket()
server.bind(('0.0.0.0',8000))
server.listen(1024)

server.setblocking(False) # 设置为非阻塞模式 recv accept 都不阻塞，不用判断accept数据为空

inputs = [server,] # 监测的链接 ，好的，不好的都在里面
outputs = []

#
readable, writeable, exceptional = select.select(inputs, outputs,inputs)
print(readable,writeable,exceptional)
# while True:
server.accept()