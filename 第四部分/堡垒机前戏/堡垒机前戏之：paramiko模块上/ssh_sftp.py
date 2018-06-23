#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import paramiko


transport = paramiko.Transport(('10.0.1.200',22))
transport.connect(username='root',password='dongao@(*&IT')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将aaa.py 上传至服务器 /tmp/bbb.py
# sftp.put('笔记 进程与线程介绍','/tmp/bbb.txt')

# 将 remove_path 下载到本地 local_path
sftp.get('/root/ops-admin.tar.gz','aaa.tar.gz')

transport.close()
