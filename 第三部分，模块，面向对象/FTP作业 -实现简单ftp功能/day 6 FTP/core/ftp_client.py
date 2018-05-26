#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config

class Ftp_client(object):
    def __init__(self):
        self.client = config.socket
        self.client.connect(config.ip_port)
        self.help = {
            "get": "用于下载，如: get abc.txt,即 get 文件名",
            "put": "用于上传，如: put abc.txt,即 put 文件名",
            "ls": "用于显示当前目录下的文件列表详细信息",
        }
        self.auth()

    def auth(self):
        username = input("\033[33;1mFTP账户：\033[0m").strip()
        password = input("\033[33;1mFTP密码：\033[0m").strip()
        auth_info = 'auth %s %s'% (username, password)
        self.client.send(auth_info.encode())
        bk_res = self.client.recv(1024).decode()
        if bk_res.split()[2] == 'success':
            print(bk_res.split())
            return True
        else:
            print("用户认证失败，请重新输入")
            return False

    def client_start(self):
        while True:
            client_input = input(">>：").strip()
            if len(client_input) == 0:
                continue

            client_input = client_input.split()
            if client_input[0] == 'q':
                print("退出程序")
                break
            action = client_input[0]
            if hasattr(self, action):
                func = getattr(self, action)
                func(client_input)
            else:
                print("Command not fount,please input again.")
                continue

    def ls(self, cmd):
        # print(cmd[0])
        # 发送 ls 命令到 Server
        client_send_to_server_info = '%s' % cmd[0]
        print(client_send_to_server_info)
        self.client.send(client_send_to_server_info.encode())
        # 接收 server 端返回
        server_back = self.client.recv(1024).decode()
        print("ls 命令返回结果大小：", server_back)
        # 发送ok信号，提示server端，可以准备好接收数据了
        self.client.send("ok".encod())
        # 初始化接收数据大小为0
        recv_size = 0
        # 初始化接收数据为空
        recv_data = b""
        # 循环条件：如果接收数据小于实际返回数据大小
        while recv_size < int(server_back):
            # 每次接收数据内容
            data = self.client.recv(1024)
            # 接收数据大小赋值
            recv_data = data
            # 接收数据大小累加，接收数据大小 = 当前接收的大小 + 内次返回数据的大小
            recv_size += len(data)
        else:
            print(recv_data.decode())

    def help(self, cmd):
        # if len(cmd) == 1:
        for k, v in self.help.items():
            print("%s ：%s" % (k, v))