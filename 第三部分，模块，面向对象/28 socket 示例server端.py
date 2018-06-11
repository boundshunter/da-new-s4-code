#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# server 端
import socket
import os
server = socket.socket()  # 声明类型，生成连接对象
server.bind(('localhost',6969)) # 绑定server 监听端口
server.listen(5) # 监听端口，先绑定后监听,5为允许连接排队数，默认不限制
                 # 连接数在异步情况下才能测试出来。
print("starting wait...")
while True:
    print("wait new conn incoming")
    conn,addr = server.accept() # 等待 请求
    # conn 就是客户端连接过来，而服务器端为其生成的一个连接实例
    while True:
        data = conn.recv(102400) # 接收数据大小 1024字节
        if not data:break
        print("recv:",data)
        conn.send(data.upper()) # 发送大写的返回数据
