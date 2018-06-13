#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import os,socket
server = socket.socket()
server.bind(('127.0.0.1',9999))
server.listen(3)

while True:
    print("等待客户端进入...")
    conn, addr = server.accept()
    while True:
        print("开始接收数据")
        cmd = conn.recv(1024)# 接收大小
        if not cmd: break
        cmd_res = os.popen(cmd.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output."
        conn.send(str(len(cmd_res.encode())).encode()) # 发送大小 两次encode，防止汉字生成3字节
        conn.send(cmd_res.encode('utf-8')) # 发送结果



