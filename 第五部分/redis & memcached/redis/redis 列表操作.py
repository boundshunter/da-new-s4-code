#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
'''
127.0.0.1:6379> lpush names alex jfsu abc bcd
(integer) 4
127.0.0.1:6379> LRANGE names 0 -1 # 0,-1表示所有
1) "bcd"
2) "abc"
3) "jfsu"
4) "alex"

# 最后一个插入的在最左边
127.0.0.1:6379> LRANGE names 1 2 # 列表切片
1) "abc"
2) "jfsu"

同理 Rpush 相反

127.0.0.1:6379> LPUSH name1 daq dbq dcq ddq
(integer) 4
127.0.0.1:6379> LLEN name1
(integer) 4
127.0.0.1:6379> LASTSAVE name1
(error) ERR wrong number of arguments for 'lastsave' command
127.0.0.1:6379> LASTSAVE \
(error) ERR wrong number of arguments for 'lastsave' command
127.0.0.1:6379> LASTSAVE
(integer) 1530697916
127.0.0.1:6379> LINDEX name1 1
"dcq"
127.0.0.1:6379> LINDEX name1 0
"ddq"
127.0.0.1:6379> LINDEX name1 5
(nil)
127.0.0.1:6379> LINDEX name1 4
(nil)
127.0.0.1:6379> LINDEX name1 3
"daq"
127.0.0.1:6379> LINSERT name1 before daq ddd
(integer) 5
127.0.0.1:6379> LINSERT name1 after daq ddd
(integer) 6
127.0.0.1:6379> LRANGE name1 0 -1
1) "ddq"
2) "dcq"
3) "dbq"
4) "ddd"
5) "daq"
6) "ddd"
127.0.0.1:6379> LPUSHX name1 bbb
(integer) 7
127.0.0.1:6379> LRANGE name1 0 -1
1) "bbb"
2) "ddq"
3) "dcq"
4) "dbq"
5) "ddd"
6) "daq"
7) "ddd"
127.0.0.1:6379> LSET name1 1 aaa
OK
127.0.0.1:6379> LRANGE name1 0 -1
1) "bbb"
2) "aaa"
3) "dcq"
4) "dbq"
5) "ddd"
6) "daq"
7) "ddd"
127.0.0.1:6379> LSET name1 0 abc
OK
127.0.0.1:6379> LRANGE name1 0 -1
1) "abc"
2) "aaa"
3) "dcq"
4) "dbq"
5) "ddd"
6) "daq"
7) "ddd"

127.0.0.1:6379> LREM name1 2 ddd # 从左删除name1下的2个ddd
(integer) 2
127.0.0.1:6379> LRANGE name1 0 -1
1) "abc"
2) "aaa"
3) "dcq"
4) "dbq"
5) "daq"

127.0.0.1:6379> LPOP name1 从左侧获取第一个，并从列表中移除
"abc"

r.lrem(name, value, num)

# 在name对应的list中删除指定的值

# 参数：
    # name，redis的name
    # value，要删除的值
    # num，  num=0，删除列表中所有的指定值；
           # num=2,从前到后，删除2个；
           # num=-2,从后向前，删除2个
127.0.0.1:6379> LTRIM name1 0 1 # 只保留0到1下标的数据
OK
127.0.0.1:6379> LRANGE name1 0 -1
1) "aaa"
2) "dcq"

127.0.0.1:6379> RPOPLPUSH name1 name2
"dcq"
127.0.0.1:6379> LRANGE name2 0 -1
1) "dcq"
2) "kkk"
3) "yyy"
4) "qqq"
5) "zzz"
127.0.0.1:6379> LRANGE name1 0 -1
1) "ddd"
2) "acc"
3) "abb"
4) "ddd"
5) "ccc"
6) "bbb"
7) "aaa

# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
# 参数：
    # src，要取数据的列表的name
    # dst，要添加数据的列表的name

blpop(keys, timeout) 从左到右删除列表中的值，执行一次删除一个，
timeout的作用说明：如果列表有值，则立即完成，列表没有值（empty)则等待超时时间，最后返回超时时间，在等待过程中
如果列表有值插入，则立刻返回超时时间同时删除一个值


# 将多个列表排列，按照从左到右去pop对应列表的元素

# 参数：
    # keys，redis的name的集合
    # timeout，超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞

# 更多：
    # r.brpop(keys, timeout)，从右向左获取数据

127.0.0.1:6379> LRANGE name3 0 -1
1) "jfsu"
2) "abc"
3) "ddd"
127.0.0.1:6379> LRANGE name4 0 -1
(empty list or set)
127.0.0.1:6379> LRANGE names4 0 -1
1) "lili"
2) "hanhan"
3) "xixi"
127.0.0.1:6379> BRPOPLPUSH name3 names4 10 # 删除第一个列表中的右数第一个元素，插入到第二个列表的第一个位置，
                                          # 超时时间为10s，如果第一个列表为空，则等待10s,中间又数据插入name3，立即完成并返回时间
                                          # 否则一直到等待10s结束，返回空列表和等待时间
                                          # 127.0.0.1:6379> BRPOPLPUSH name3 names4 10
                                          #   (nil)
                                          #   (10.07s)
                                          应用场景：两个进程数据同步，第一个进程从queue中存入redis，删除的同时，插入第二个进程的queue，
                                          实现两个进程数据的一致性
"ddd"
127.0.0.1:6379> LRANGE names4 0 -1
1) "ddd"
2) "lili"
3) "hanhan"
4) "xixi"
127.0.0.1:6379> LRANGE name3 0 -1
1) "jfsu"
2) "abc"
'''