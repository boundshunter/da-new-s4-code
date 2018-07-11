#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
# /usr/lib64/python3.6/configparser.py 需要复制成
# cp /usr/lib64/python3.6/configparser.py /usr/lib64/python3.6/ConfigParser.py 否则系统找不到

# 之后才能执行 pip3.6 install mysql-python

#mysql2.x使用
import MySQLdb

conn = MySQLdb.connect(host='10.0.1.110',user='jfsu',passwd='gxw#mP8t',db='test')

cur = conn.cursor()

recount = cur.execute('select * from B')

conn.commit()

cur.close()
conn.close()
print(recount)