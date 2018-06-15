#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
'''
ftp server:
1、读取文件名
2、检测文件是否存在
3、打开文件
4、检测文件大小
5、发送文件大小给客户端，发送文件大小和md5值给客户端
6、等到客户端确认的ack
7、边读边发数据
8、关闭文件
'''
'''
#生成md5
import hashlib
m = hashlib.md5()
m.update(b'test')
print(m.hexdigest())
'''
import socket,os,time
server = socket.socket()
server.bind(('127.0.0.1',8888))
server.listen()

while True:
    print("等待新连接...")
    conn,addr = server.accept()

    while True:
        print("开始循环接收命令...")
        cmd = conn.recv(1024).decode() # get filename
        if not cmd:
            print("cmd is empty")
            break
        file_name = cmd[1]
        # 判断文件是否存在
        if len(cmd) == 2: # 判断发送命令是否为2个参数
            if os.path.isfile(file_name): # 判断文件是否存在

            else:
                print("文件不存在")
        else:
            print("命令格式不正确:",cmd)
