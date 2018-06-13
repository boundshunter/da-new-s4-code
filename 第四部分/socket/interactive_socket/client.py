#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import socket
client = socket.socket()
# client.connect(('127.0.0.1',9999))
client.connect(('10.0.1.110',9999))


while True:
    cmd = input(">>:").strip()
    if not cmd:continue
    # 发送大小
    client.send(cmd.encode())
    total_size = client.recv(1024).decode() # 接收大小
    print("total_size:",total_size)
    recv_size = 0
    recv_data = b''
    while recv_size < int(total_size):
        data = client.recv(1024)
        recv_size += len(data)
        print("recv_size:",recv_size)
        recv_data += data # 做接收数据累加结果
    else:
        print("recv done")
        print(recv_data.decode()) # 显示最终接收结果


