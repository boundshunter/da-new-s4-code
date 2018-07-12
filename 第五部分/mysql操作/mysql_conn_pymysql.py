#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import pymysql

conn = pymysql.connect(host='10.0.1.110',user='root',passwd='gxw#mP8t',db='test')

cursor = conn.cursor()

# recount = cursor.execute("select user,host from user")

data = [
    ('A1','male','2018-07-12'),
    ('A2','female','2018-07-11'),
    ('A3','male','2018-07-10')
]
cursor.executemany("insert into student (name,gender,datetime) values(%s,%s,%s)",data) # 批量插入数据
student_info = cursor.execute("select * from student")

conn.commit()
cursor.close()
conn.close()
# print(recount) # 显示的是数据的条数
print(cursor.fetchall()) # 显示所有结果

# for i in range(recount): # 去所有结果 循环，每次取1条
#     print(cur.fetchone())
