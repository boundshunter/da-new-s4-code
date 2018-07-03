#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 核心是发给exchange
'''
fanout：所有绑定到exchange的queue都可以接收消息
direct:通过routingKey和exchange决定的那个唯一的queue可以接收消息
topic:所有符合routingKey(此时可以事一个表达式)的routingKey所绑定的queue可以接收到消息
'''
# fanout 中，exchange将producer的消息，放入 queue中，然后消费者去queue中获取消息
# 实时广播，消费端如果当时没在，就收不到消息

# publisher
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
