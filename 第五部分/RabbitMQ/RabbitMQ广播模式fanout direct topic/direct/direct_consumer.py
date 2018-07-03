#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import pika
import sys
# 执行方式，默认发送到info, 指定接收级别，
# python direct_consumer info warning # 指定2个接收级别
# python direct_consumer error # 指定一个接收级别
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:] # 获取脚本执行所有的参数
if not severities: # 如果参数不存在
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities: # 循环接收发送到severity级别的消息
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()