#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print(self.data)
                self.request.send(self.data.upper())

            except ConnectionResetError as e:
                print("err:",e)
                break
if __name__ == '__main__':
    IP, PORT = '0.0.0.0', 8888
    # server = socketserver.TCPServer((IP,PORT), MyTCPHandler) # 单线程，1对1
    # server.serve_forever()

    server = socketserver.ThreadingTCPServer((IP,PORT), MyTCPHandler) # 多线程并发
    server.serve_forever()

    # server = socketserver.ForkingTCPServer((IP,PORT), MyTCPHandler)# 多进程  只支持 linux
