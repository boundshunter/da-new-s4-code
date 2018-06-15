#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
'''
1、创建一个请求类
2、实例化 tcpserver,传递ip和请求的类，给实例化tcpserver
3、调用server.serve_forever() # 启动进程，永远执行，可以处理多个请求，99%场景都使用这个

    server.handle_request() # 只处理一个请求（这个基本用不上）
**** 跟客户端所有的交互，都是在handle里完成的     def handle(self):
'''


