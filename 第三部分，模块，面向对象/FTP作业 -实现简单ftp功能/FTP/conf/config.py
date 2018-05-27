#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

# import sys
import os
import socket

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )

# Ip和port信息
IP_PORT = ('127.0.0.1', 9999)


# 用户数据
USERS_FILE = BASE_DIR+'/db/'

# 用户文件目录
USER_HOME = BASE_DIR+'/db/client'

# 服务器端目录
SERVER_HOME = BASE_DIR+'/db/server'