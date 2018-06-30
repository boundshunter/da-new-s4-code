#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

#select 缺点： 最多只能维护1024个socket(也就是用户能打开的默认文件句柄为1024）
#select 默认取的用户的文件句柄，修改系统的，select也跟着修改
# select 把多个socket连接，交给内核去监测，假如65535个连接需要监测，


# poll 出现之后，和select区别，就是没有默认文件句柄数的限制了

# epoll  django, twisted 等框架，都是epoll
# windows只支持select,
# linux 2.6内核之后支持epoll

# epoll解决了 select 大量循环的问题，提高了效率，同样也没有最大socket限制
# 同样监测多个 socket 连接，当哪个连接有数据了，直接通知用户，用户从内核拷贝数据到用户内存，获取数据
# 65535 并不是最大文件句柄数，epoll没有65535个限制，可以同时处理几十万个连接
# 一个连接 4k内存，1G内存的系统，可以支持10W个连接，同时连接过来

# epoll  水平触发，边缘触发 低层算法，不需要关注


# 市面上捡到的 各种异步IO，其实就是IO多路复用
# 但是系统多异步IO的支持都不是很好，有一个aio_ read ，作为支持异步IO的模块

#import asyncio 3.0后支持的，但是连nginx都不这么用，

# 只需要学会IO多路复用即可
