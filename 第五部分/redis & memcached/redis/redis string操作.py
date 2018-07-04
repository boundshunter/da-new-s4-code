#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

# redis-cli

#set name abc
#get name

# set name bcd ex 3 # 3秒过期
#get name
# 简单redis 操作
import redis,time
r = redis.Redis(host='10.0.1.110',port=6379)
r.set('foo','abc')
print(r.get('foo'))

# 生成一个连接池，不用重复建立连接
pool = redis.ConnectionPool(host='10.0.1.110',port=6379)
rds = redis.Redis(connection_pool=pool)

rds.set('pql','abb',ex=3) # 设置值，3秒后清除
print(rds.get('pql'))
time.sleep(2)
print(rds.get('pql'))
time.sleep(1)
print(rds.get('pql'))

# 说明
# set(name,value,ex=None,px=None,nx=False,xx=False)
# redis 中设置值，不存在则创建，存在则修改
'''
参数：
    ex: 过期时间（秒）
    px: 过期时间（毫秒）
    nx: 如果设置为True,则只有name不存在时，当前set操作才执行
    xx: 如果设置为True,则只有name存在时，当前set操作才执行 # 用于修改值
'''
'''
setnx(name, value)

设置值，只有name不存在时，执行设置操作（添加）
setex(name, value, time)

# 设置值
# 参数：
    # time，过期时间（数字秒 或 timedelta对象）
psetex(name, time_ms, value)

# 设置值
# 参数：
    # time_ms，过期时间（数字毫秒 或 timedelta对象）
mset(*args, **kwargs)

批量设置值
如：
    mset(k1='v1', k2='v2')
    或
    mget({'k1': 'v1', 'k2': 'v2'})
get(name)

1
获取值
mget(keys, *args)

批量获取
如：
    mget('ylr', 'wupeiqi')
    或
    r.mget(['ylr', 'wupeiqi'])
getset(name, value)

设置新值并获取原来的值
getrange(key, start, end)

# 获取子序列（根据字节获取，非字符）
# 参数：
    # name，Redis 的 name
    # start，起始位置（字节）
    # end，结束位置（字节）
# 如： "武沛齐" ，0-3表示 "武"
setrange(name, offset, value)

# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# 参数：
    # offset，字符串的索引，字节（一个汉字三个字节）
    # value，要设置的值

#重点：setbit



#命令行格式：
#setbit(name,offset,value)
#举个例子：
redis 中
127.0.0.1:6379> set name sujf
OK
127.0.0.1:6379> get name
"sujf"
# 我现在想把结果中 sujf变成 Sujf，把小写的s变成大写的S
# 首先我需要在python中转换 s 的二进制，
>>> ord("s")
115
>>> bin(115)
'0b1110011' # 再将二进制变成8进制
下面是转换过程
		64	32	16	8	4	2	1
s:0	b	1	1	1	0	0	1	1     ( 64+32+16+2+1=115 )

通过命令我可以获取
>>> ord("S")
83
>>> bin(83)
'0b1010011'
大写S的8进制为如下：
S:0	b	1	0	1	0	0	1	1
s:0	b	1	1	1	0	0	1	1     ( 64+32+16+2+1=115 )
位置    1   2   3   4   5   6   7
和小写s相比只需要吧位置2的0，变成 1
也就是
setbit name 2 0

strlen(name)

1
# 返回name对应值的字节长度（一个汉字3个字节）
# 比如统计在线用户，来一个用户+1，掉线一个用户-1 decr(self,name)
incr(self, name, amount=1)
127.0.0.1:6379> incr login_user
(integer) 1
127.0.0.1:6379> incr login_user
(integer) 2

127.0.0.1:6379> decr login_user
(integer) 3
127.0.0.1:6379> decr login_user
(integer) 2
127.0.0.1:6379> decr login_user
(integer) 1
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

# 参数：
    # name,Redis的name
    # amount,自增数（必须是整数）

# 注：同incrby
incrbyfloat(self, name, amount=1.0)

# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

# 参数：
    # name,Redis的name
    # amount,自增数（浮点型）
'''