#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

'''
生产者，消费者模型
队列： 生产数据put，消费数据get,
    运维的集群，就是生产消费模型，用户访问消费服务器，集群作为生产者调度
'''
import  queue
import threading
import time
'''
q = queue.Queue(maxsize=10)

def Producer(name):
    for i in range(10):
        q.put('%s生产骨头%s'%(name,i))
        print(q.queue)
        time.sleep(1)
def Consumer(name):
    # 判断队列>0
    while q.qsize()>0:
        print("[%s] 取到 [%s] 吃了"% (name,q.get()))
        time.sleep(1)
    else:
        print("骨头没有了，不够吃")
a = threading.Thread(target=Producer,args=("alex",))
b = threading.Thread(target=Consumer,args=("chenronghua",))
a.start()
b.start()

'''

q = queue.Queue(maxsize=10) # 最多放10个

def Producer(name):
    count = 1
    while True:
        q.put("%s 生产骨头编号[%s]"%(name,count))
        count +=1
        if q.qsize()<10:
            print("剩余骨头数：",q.qsize())
        else:
            pass
        time.sleep(0.5)

def Consumer(name):
    while True: #此处不用q.qsize>0 防止出现生产了一个吃掉之后，就变成0了，然后消费者卡住了
        print("%s吃骨头%s"%(name,q.get()))
        time.sleep(0.6)

if __name__ == '__main__':
    # 可以多个生产者，多个消费者
    # 队列最多存储10个，生产者生产，消费者消费，不断循环
    # 使用先进先出方式
    p1 = threading.Thread(target=Producer,args=("alex",))
    p2 = threading.Thread(target=Producer,args=("wupeiqi",))
    c1 = threading.Thread(target=Consumer,args=("wangsen",))
    c2 = threading.Thread(target=Consumer,args=("陈荣华",))

    p1.start()
    p2.start()
    c1.start()
    c2.start()