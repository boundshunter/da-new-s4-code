#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
event = threading.Event()
event.wait() 等到标志位被设定
event.set() # 设置标志位 ，标志位设定了，假如代表绿灯
event.clear() # 清空标志位 标志位被清空，无标志位了，代表红灯，wait等到边绿灯，多辆车等待同一个红绿灯事件
'''

import time
import threading


def car(name):
    while True:
        if event.is_set(): # 代表绿灯
            print("[%s] go on running"% name)
            time.sleep(1)
        else: # 代表红灯
            print("[%s] stop running, waiting for light to green"% name)
            event.wait() # 等待event.set() 变绿灯
            print("\033[32;1m green light is on [%s] start going\033[0m"% name)

def lighter():
    count = 0
    event.set()
    while True:
        if count>5 and count<=10: #代表红灯
            print("\033[41;1m red light waiting\033[0m")
            event.clear() # 变红灯，清空标志位，未设置标志位就代表红灯
            print(count)
        elif count  > 10:
            print("\033[42;1m green light going \033[0m")
            event.set() # 设置标志位，变绿灯
            print(count)
            count=0
        else:
            print("\033[42;1m green light going \033[0m")
            print(count)

        time.sleep(1)
        count += 1


if __name__ == '__main__':
    event = threading.Event()
    light = threading.Thread(target=lighter,)
    light.start()

    carx = threading.Thread(target=car,args=("G63",))
    carx.start()
