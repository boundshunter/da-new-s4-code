#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import gevent, time
from urllib import request
from gevent import monkey
# 实际上 gevent 和urllib是没有关系的，也无法发现他出现io的地方，只需要加上下面的说明即可实现

monkey.patch_all() # 意思是：把当前程序的所有io操作给做上标记

def func(url):
    print("GET: %s"% url)
    response = request.urlopen(url)
    data = response.read()
    print("%d bytes received from %s"% (len(data), url))

# 串行效果演示
urls = [
    'https://www.python.org',
    'https://www.sina.com.cn',
    'https://www.github.com'
]

time_start = time.time()
for url in urls:
    func(url)
print("rsync cost:",time.time()-time_start)

# 并行效果演示，如果没有monkey.patch_all()做io操作标记，此处同样为串行，因为本身urllib和gevent没有内部关联
async_start_time = time.time()
gevent.joinall([
    gevent.spawn(func,"https://www.python.org"),
    gevent.spawn(func,"https://www.sina.com.cn"),
    gevent.spawn(func,"https://www.github.com")
])
print("async cost:",time.time()-async_start_time)