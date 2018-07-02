#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import pika

# 建立 socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 声明（开通）一个管道，在管道里发消息
channel = connection.channel() # 可能为了区分不同程序发的消息

# 管道里面要声明一个queue 消费者也需要声明收消息的队列
# 为什么要再次声明队列，我们之前生产者声明了一次，消费者需要再声明一次么？
# 原因是，如果你确定，这个队列存在了，已经被声明过了，那么你不需要声明
# 如果无法确定，比如消费者先执行，在没有这个队列声明的前提下，是会报错的，
# 所以为了保险，不报错，需要声明一次
channel.queue_declare(queue='b_queue',durable=True) # 声明收消息的队列

def callback(ch, method, properties, body):
    # callback默认带四个参数
    # 打印4个参数值
    # ch 就是 channel
    # print("ch:%s\nmethod:%s\nproperties:%s\nbody:%s"% (ch, method, properties, body))
    print("[x] Received %r"% body)
    # 手动给服务端确认消息已处理完毕
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(# 消费消息
                      callback,# 如果收到消息就调用callback回调函数来处理消息
                      queue='b_queue')
                      # no_ack = True # no ack = no acknownledgement ，也就是不给生产者回消息，不通知生产者消息是否完成
                      # 去掉 no_ack 增加一个sleep(30)，如果消费者在没消费完成之前，断开，消息会自动转到第二个消费者身上

# 多个消费者 消费， 是采用轮训机制，把多个消息公平的发送给每个消费者，先到先得
print('[*] Waiting for message.To exit press CTRL+C')
channel.start_consuming()