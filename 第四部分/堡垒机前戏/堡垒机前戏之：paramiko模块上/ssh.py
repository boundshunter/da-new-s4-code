#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import paramiko

# 创建对象
ssh = paramiko.SSHClient()

# 允许连接不在known_hosts中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='10.0.1.200',port=22,username='root',password='dongao@(*&IT')

#执行命令
stdin,stdout,stderr = ssh.exec_command("top -bn 1")
# l = []
rlt = stdout.read() # 默认是bytes格式
print(rlt.decode())
# for i in rlt:
#     l.append(i)

# print(l)

ssh.close()
