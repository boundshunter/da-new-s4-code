#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import socket
HOST = 'localhost'
PORT = '8082'

cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(('127.0.0.1',8082))

def Client():
    while True:
        msg = input(">>:").strip()
        if not msg: # null
            continue
        else:
            cli.send(msg.encode())
            data = cli.recv(1024)
            print("recv:",data)
    cli.close()

if __name__ == '__main__':
    Client()
