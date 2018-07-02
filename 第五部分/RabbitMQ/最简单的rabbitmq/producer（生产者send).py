#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 需要先启动 rabbit mq 服务
import pika

# 建立 socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 声明（开通）一个管道，在管道里发消息
channel = connection.channel() # 可能为了区分不同程序发的消息

# 管道里面要声明一个queue  [durable=True 通知RabbitMQ 消息需要持久化] 持久化的是这个消息队列的名字，不是里面的内容
channel.queue_declare(queue='b_queue',durable=True) # 管道名字叫a_queue

# 参数说明，[管道名字 routing_key='a_queue']，[发送到队列中的内容 body="Hello World"]
channel.basic_publish(exchange='',
                      routing_key='b_queue',
                      body="Hello World",
                      # durable = True 持久化了队列名字， 如果想让消息也持久化
                      properties=pika.BasicProperties(
                          delivery_mode=2 # make message persistent 使消息持久化
                      )
                      )

print("[x] Send 'Hello World!'")
connection.close()