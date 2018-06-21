#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import socket
client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
client.connect(('127.0.0.1',8888))
while True:
    msg = input(">>>").strip()
    if len(msg) ==0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)#这里是字节1k
    print("recv:>",data.decode())
client.close()