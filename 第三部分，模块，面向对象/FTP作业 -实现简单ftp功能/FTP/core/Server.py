#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import config
from core import UserAuth

class ftpServer:
    def __init__(self):
        self.server = config.socket.socket()
        self.server.bind(config.IP_PORT)
        self.server.listen(5)
        self.userobj = UserAuth.users() # 把users类实例化
        self.start()

    def start(self):
        while True:
            print("服务器正在等待连接...")
            self.conn,self.addr = self.server.accept()
            print("一个连接建立", self.conn)
            while True:
                self.data = self.conn.recv(1024)
                if not self.data: # 判断接收为空
                    print("客户端断开连接")
                    break
                # 数据不为空，继续执行
                res = self.data.decode().split() # py3 中每一步都接收和发送都需要转码
                action = res[0] # 获取接收执行动作
                print("start:", action)
                if hasattr(self, action):  # 反射
                    fc = getattr(self, action)  # 存在获取执行动作
                    fc(res)  # fc 相当于先对对象实例化，然后实例化后调用传入的方法action，然后在执行action方法，需要传入参数传入参数，只有self则不传入参数
                    fc('ls')  # d = obj()   d.ls('ls')
                else:
                    print("输入错误")

    def auth(self, cmd):
        print(cmd) # cmd 格式 auth username password
        user = self.userobj.get_user(cmd[1]) # 从获取用户名中去 userauth中做认证，userauth，认证成功返回user的字典
        print(user)
        if user: # 判断用户字典非空
            if user['password'] == cmd[2]: # 判断密码是否正确
                self.curr_user = user
                self.curr_path = user['home']
                self.user_home = config.USER_HOME
                self.conn.send(b'ok')
            else:
                self.conn.send(b'password is wrong')
        else:
            self.conn.send(b'%s is not exist'%cmd[1])

    def put(self,cmd):
        # 文件完整路径
        file_name = self.user_home+self.curr_path+cmd[1]
        # 文件总大小为传入的值，传入的命令样式 "put filename size"
        total_size = cmd[2]
        # 传入文件写入
        with open(file_name,'wb') as f:
            self.conn.send('200'.encode())
            recv_size = 0
            # 判断如果 收到的大小比总大小，就一直循环收
            while recv_size < int(total_size):
                data = self.conn.recv(1024)
                recv_size += len(data)
                # 收完写入文件
                f.write(data)
            else:
                print("\033[41[1maction：put,server received complete\033[0m")

    def ls(self, cmd):

        user_path = self.user_home
        print('\033[42;1maaa\033[0m',(user_path,cmd[0]))

        res = os.popen("%s %s"% (cmd[0],user_path)).read()
        print("\033[42;1mbbb:\033[0m",res)
        if len(res) == 0:
            res = "command's result is empty.there is no file or directory in %s"% (user_path)
        self.conn.send(res.encode())
        # self.conn.recv(1024)
        # self.conn.send(res.encode())


