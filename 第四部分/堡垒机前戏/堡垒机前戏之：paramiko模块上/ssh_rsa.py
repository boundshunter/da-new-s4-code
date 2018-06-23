#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import paramiko
import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR + '/id_rsa.txt')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy) # 绕过 known_host确认过程，没登录过自动加入known_hosts

private_key = paramiko.RSAKey.from_private_key_file(BASE_DIR+'/id_rsa.txt')
ssh.connect('10.0.1.200',port=22,username='sujunfeng',pkey=private_key)

stdin,stdout,stderr = ssh.exec_command('top -bn 1')
# reserr = stderr.read()
res = stdout.read()
# print(reserr.decode())
print(res.decode())

ssh.close()




