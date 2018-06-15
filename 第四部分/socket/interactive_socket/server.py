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

        # 两次连续发，会出现数据粘包 ，下面2次就会粘包
        # 防止两次连续发送，会把数据放入统一缓冲区 send给客户端
        # 一种是中间增加 time.sleep(0.5) 0.5秒的停顿可以解决，但是会损失时间
        # 另外一种就是增加一次 接收，多一次接收交互，等待客户端确认
        conn.send(str(len(cmd_res.encode())).encode()) # 发送大小 两次encode，防止汉字生成3字节
        ack = conn.recv(1024).decode() # 防止粘包，增加一次交互，防止两次发送写入一个缓冲区一起发送给客户端
        conn.send(cmd_res.encode('utf-8')) # 发送结果



