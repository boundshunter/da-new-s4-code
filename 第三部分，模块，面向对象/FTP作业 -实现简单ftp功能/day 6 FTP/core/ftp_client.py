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
        auth_info = 'auth %s %s' % (username, password)
        self.client.send(auth_info.encode())
        bk_res = self.client.recv(1024).decode()
        print(bk_res)
        if bk_res.split()[2] == 'success':
            # print(bk_res.split())
            self.client_start()
        else:
            print("用户认证失败，请重新输入")
            return False

    def client_start(self):
        while True:
            # self.help()
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
                print("Command not found,please input again.")
                continue

    def ls(self, cmd):
        print(cmd)
        send_cmd = cmd[0]
        print("ls send command：", cmd[0])
        self.client.send(send_cmd.encode())
        server_back = self.client.recv(1024).decode
        print(server_back)




    def help(self, *args):
        # if len(cmd) == 1:
        for k, v in self.help.items():
            print("%s ：%s" % (k, v))


            print("aaa")