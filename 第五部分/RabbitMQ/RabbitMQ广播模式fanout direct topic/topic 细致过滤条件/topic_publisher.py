#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
收所有:

python receive_logs_topic.py "#"
收以kern开头 "kern":

python receive_logs_topic.py "kern.*"
Or if you want to hear only about "critical" logs:
收所有以critical结尾
python receive_logs_topic.py "*.critical"
You can create multiple bindings:

python receive_logs_topic.py "kern.*" "*.critical"
收以kern开头的，还有critical结尾的
And to emit a log with a routing key "kern.critical" type:
收 kern.critical的
python emit_log_topic.py "kern.critical" "A critical kernel error"
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()