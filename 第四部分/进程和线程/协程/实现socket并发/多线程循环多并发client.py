#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import socket, threading

def ClentConnect():
    cli = socket.socket()
    cli.connect(('127.0.0.1',8082))
    count = 0
    while True:
        info = "Hello %s"% count
        cli.send(info.encode())
        data = cli.recv(1024)
        print("{%s} recv from server:"% threading.get_ident(), data.decode())
        count += 1
    cli.close()

if __name__ == '__main__':
    for i in range(10):
        p = threading.Thread(target=ClentConnect)
        p.start()