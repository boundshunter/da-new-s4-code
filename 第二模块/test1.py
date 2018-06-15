#!/usr/bin/env python
#-*- coding:utf-8 -*-
# # Author:summer_han
# '''
#  headings = ['date', 'pv', 'uv']
#     data = [
#     [2, 3, 4, 5, 6, 7],
#     [10, 40, 50, 20, 10, 50],
#     [30, 60, 70, 50, 40, 30],
#     ]
#     worksheet.write_row("B2", headings)
#     worksheet.write_column("B3", data[0])
#     worksheet.write_column("C3", data[1])
#     worksheet.write_column("D3", data[2])
#
# '''
# # # 当前日期
# # import time
# # print(time.time())
# #
# # print(time.localtime(time.time()))
# #
# # print(time.strftime('%Y/%m/%d'))
#
# print(1+(2+(3*(4+5))+6))
#
# aa = ['ls', '/home/sujunfeng']
# print(aa[0])
# bb = "%s %s"%(aa[0],aa[1])
# print(type(bb))
# print(bb.encode())

import random

# print(random.randint(1, 100))
# aa = random.randint(1,100)
bb = random.choice("ijga3912059153094jmkdvcgnqatjioqrjkgqjr192349*#$*!*^!)#!%&)*^!)#!^*!^#(**^#$")
i = 0
cc = []
while i < 10:
    print(i)
    i += 1
    cc = cc.append(bb)
    print(cc)