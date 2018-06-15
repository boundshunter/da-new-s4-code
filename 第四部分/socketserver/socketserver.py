#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'jfsu'

import socketserver


# class MyTCPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         while True:
#             try:
#                 self.data = self.request.recv(1024).strip()
#                 self.request.send(self.data.upper())
#             except ConnectionResetError as e: # 自动捕获客户端断开，不用判断空数据
#                 print("err:",e)
#                 break
# if __name__ == '__main__':
#     HOST, PORT = '127.0.0.1', 9999
#     server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
#     server.serve_forever()

class mytcphandler(socketserver.BaseRequestHandler):
    print("abc")

if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 9999
    server = socketserver.TCPServer((HOST, PORT), mytcphandler)
    server.serve_forever()