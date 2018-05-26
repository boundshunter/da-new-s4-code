#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#[auth]
user_auth_dir = BASE_DIR + '/db'
user_auth_file = user_auth_dir + '/user_db/'


#[socket]
socket = socket.socket()

#[ip_port]
ip_port = ('127.0.0.1', 20021)

#[listen]
listen_num = 5

#[user_home_dir]
user_home_dir = BASE_DIR + '/db/home/'