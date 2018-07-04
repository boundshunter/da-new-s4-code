#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# 集合默认去重
'''
127.0.0.1:6379> SADD names3 jack alex jfsu jack 3 4 3 2 3 3 1
(integer) 7

127.0.0.1:6379> SMEMBERS names3
1) "jfsu"
2) "2"
3) "alex"
4) "jack"
5) "1"
6) "3"
7) "4"
'''
