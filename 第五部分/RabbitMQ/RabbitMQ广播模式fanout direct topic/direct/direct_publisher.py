#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import pika
import sys
# 执行方式，默认发送到info, 指定发送级别
# python direct_consumer info warning # 指定2个发送级别
# python direct_consumer error # 指定一个发送级别
# 指定的发送级别，只有相应的接收端才能接收到
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity, # 相当于发到哪个queue，发送到哪个级别里面
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()