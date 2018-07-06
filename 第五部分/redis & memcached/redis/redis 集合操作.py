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
127.0.0.1:6379> SADD name3 jack alex wu
(integer) 3
127.0.0.1:6379> SADD name4 abc bbb ddd
(integer) 3
127.0.0.1:6379> SADD name4 jack
(integer) 1
127.0.0.1:6379> SDIFF name3 name4
1) "wu"
2) "alex"
127.0.0.1:6379> SDIFFSTORE name5 name3 name4
(integer) 2
127.0.0.1:6379> SMEMBERS name5
1) "wu"
2) "alex"
127.0.0.1:6379> SINTER name3 name4
1) "jack"
127.0.0.1:6379> SISMEMBER name3 abc
(integer) 0
127.0.0.1:6379> SISMEMBER name3 alex
(integer) 1
127.0.0.1:6379> SISMEMBER name3 wu
(integer) 1
127.0.0.1:6379> SMOVE name3 name4 alex
(integer) 1
127.0.0.1:6379> SMEMBERS name4
1) "bbb"
2) "abc"
3) "jack"
4) "ddd"
5) "alex"
127.0.0.1:6379> SMEMBERS name3
1) "wu"
2) "jack"
127.0.0.1:6379> SRANDMEMBER name3 1 # 随机获取一个值
"wu"
127.0.0.1:6379> SUNION name3 name4
1) "jack"
2) "abc"
3) "bbb"
4) "wu"
5) "alex"
6) "ddd"
127.0.0.1:6379> SUNIONSTORE name6 name3 name4
(integer) 6
127.0.0.1:6379> SMEMBERS name6
1) "jack"
2) "abc"
3) "bbb"
4) "wu"
5) "alex"
6) "ddd"
'''

#有序集合

'''
127.0.0.1:6379> ZADD z1 10 alex 5 jack 8 rain 4 jami # 有序集合，数字代表最后排序时的权重
(integer) 4
127.0.0.1:6379> ZCOUNT z1
(error) ERR wrong number of arguments for 'zcount' command
127.0.0.1:6379> ZCOUNT z1 1 2
(integer) 0
127.0.0.1:6379> ZCOUNT z1 0 -1
(integer) 0
127.0.0.1:6379> ZRANGE z1 0 -1
1) "jami"
2) "jack"
3) "rain"
4) "alex"
127.0.0.1:6379> ZADD z1 6 alex
(integer) 0
127.0.0.1:6379> ZRANGE z1 0 -1
1) "jami"
2) "jack"
3) "alex"
4) "rain"
127.0.0.1:6379> ZRANGE z1 0 -1 withscores # 某些情况下可以用权重来代表分数进行学生排序使用
1) "jami"
2) "4"
3) "jack"
4) "5"
5) "alex"
6) "6"
7) "rain"
8) "8"
127.0.0.1:6379> ZCOUNT z1 6 8 # 获取分数在6-8之间的个数
(integer) 2

127.0.0.1:6379> ZRANK z1 jami # 返回在集合中的排序位数，从0开始
(integer) 0
127.0.0.1:6379> ZRANK z1 rain
(integer) 3

127.0.0.1:6379> ZADD z3 5 alex 7 wusir 90 hanyang
(integer) 3
127.0.0.1:6379> ZADD z4 8 alex 11 jfsu 100 han
(integer) 3
127.0.0.1:6379> ZINTERSTORE z5 2 z3 z4
(integer) 1
127.0.0.1:6379> ZRANGE z5 0 -1
1) "alex"
127.0.0.1:6379> ZRANGE z5 0 -1 withscores
1) "alex"
2) "13"

'''