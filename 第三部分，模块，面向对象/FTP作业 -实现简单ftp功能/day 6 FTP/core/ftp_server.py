#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import config
from core.user_auth import User_auth


class Ftp_server(object):

    def __init__(self):
        # 声明socket 类型， 调用config生成的socket连接对象
        self.server = config.socket
        self.server.bind(config.ip_port)
        self.server.listen(config.listen_num)
        self.manager()



    def user_regist(self):
        user_name = input("请输入您要创建的用户名：").strip()
        user_password = input("请输入创建用户的密码：").strip()
        self.user_obj = User_auth
        self.user_obj.create_user(user_name, user_password)



    def server_start(self):
        while True:
            print("\033[35;1m服务器正在等待连接：\033[0m")
            self.conn, self.addr = self.server.accept()
            print("----连接建立----", self.conn)

            while True:
                self.data = self.conn.recv(1024)
                # 判断接收是否为空
                if not self.data:
                    print("客户端断开连接")
                    break

                # 数据不为空，继续接收，将接收数据进行转义，接收端进行decode，发送端进行encode
                res = self.data.decode().split()
                # 将接收数据进行分离，取第一字段，判断命令是否存在
                action = res[0]
                print("server start :", res)
                if hasattr(self, action):
                    server = getattr(self, action)
                    server(res[1])
                else:
                    print("您输入的命令有误，请重新输入")

    def auth(self, cmd):
        print(cmd)
        user = config.user_auth_file+cmd+'.db'
        print("\033[35;1m user \033[0m", user)
        # print("认证配置路径:%s \n文件名：%s" % (config.user_auth_file, cmd))
        # print("auth:", user)
        # 判断用户文件是否存在
        '''
        # aa = User_auth("alex", "abc")
        # user = config.user_auth_file+'alex.db'
        # print(user)
        # aa.db_handler_load(user)
        '''
        if os.path.isfile(user):
            user_db = self.user_obj.db_handler_load(user)
            # user_db = User_auth.db_handler_load(user)
            if user_db['username'] == cmd[1]:
                if user_db['password'] == cmd[2]:
                    self.conn.send("User auth success".encode())
                else:
                    self.conn.send("Password is wrong.".encode())
            else:
                self.conn.send("Username is not exist.".encode())
        else:
            self.conn.send("Username is not exist.".encode())




    def manager(self):
        menu = u'''
            \033[33;1m------- Manage Info -------
                1、创建用户
                2、启动程序\033[0m
        '''
        menu_dic = {
            '1': 'user_regist',
            '2': 'server_start',
        }

        while True:
            print(menu)
            print("\033[35;1m请输入选项的序号\033[0m")
            user_ops = input("请输入选项：").strip()
            action = menu_dic[user_ops]
            if hasattr(self, action):
                func = getattr(self, action)()

            else:
                print("您的选项有误，请重新选择。")