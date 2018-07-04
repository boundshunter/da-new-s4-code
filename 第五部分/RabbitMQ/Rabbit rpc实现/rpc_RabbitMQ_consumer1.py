#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import pika
import uuid,time

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties( # 消息持久化
                                         reply_to = self.callback_queue,# 让服务器端返回结果发送到这个queue里
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n)) # n 传入的是30
        while self.response is None: # 此循环的意思是，每次检测，只要没消息，就不阻塞
            self.connection.process_data_events() # 非阻塞版的start_consuming()
            print("no message (走到这就等于没消息)")
            time.sleep(0.5)
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)