#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 查看消息队列，和队列中消息个数
#c:\Program Files\RabbitMQ Server\rabbitmq_server-3.6.5\sbin>rabbitmqctl.bat list_queues
# 消息在RabbitMQ中，当RabbitMQ宕机或者重启之后，RabbitMQ数据就丢失了
# 消息持久化，只需要在channel声明的时候，加入一个参数，通知RabbitMQ server 这条消息需要持久化

import pika

# durable = True 通知 RabbitMQ server ,这个消息队列要持久化，在生产者和消费者端同时需要做此声明
channel.queue_declare(queue="hell3",durable=True)
# 例子可以查看 最简单的rabbitmq中示例


