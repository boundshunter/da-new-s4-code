#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
redis的哈希，类似于 多级字典

127.0.0.1:6379> HSET info name jfsu
(integer) 1
127.0.0.1:6379> HSET info age 30
(integer) 1
127.0.0.1:6379> HSET info sal 30000
(integer) 1
127.0.0.1:6379> HGETALL
(error) ERR wrong number of arguments for 'hgetall' command
127.0.0.1:6379> HGETALL info
1) "name"
2) "jfsu"
3) "age"
4) "30"
5) "sal"
6) "30000"
127.0.0.1:6379> HGET info name
"jfsu"
127.0.0.1:6379> HVALS info
1) "jfsu"
2) "30"
3) "30000"

127.0.0.1:6379> HDEL info sal
(integer) 1
127.0.0.1:6379> HVALS info
1) "jfsu"
2) "30"
127.0.0.1:6379> HKEYS info
1) "name"
2) "age"
127.0.0.1:6379> HLEN info #获取key个数
(integer) 2
127.0.0.1:6379> HMGET info age name #多个key的values
1) "30"
2) "jfsu"
127.0.0.1:6379> HEXISTS info1 name # 获取info1下的key name 是否存在，存在返回1，不存在返回0
(integer) 1
127.0.0.1:6379> HEXISTS info1 abc
(integer) 0
hdel删除key
127.0.0.1:6379> HMSET info2 name 1 age 11
OK
127.0.0.1:6379> HINCRBY info2 name 1
(integer) 2
127.0.0.1:6379> HSCAN info2 1 match *a* # 匹配获取含有a的key
1) "0"
2) 1) "name"
   2) "11"
   3) "age"
   4) "11"

获取值太多，使用迭代器方式
'''
