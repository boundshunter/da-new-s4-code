#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys, os, paramiko, threading, time
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

def Group():
    '''
    显示 分组 和 组成员列表
    :return:
    '''
    msg_group = u'''\033[35;1m
    ----------Group Informations----------
    1、Host Group 1
    2、Host Group 2\033[0m
    '''
    msg_group_dic = {
        "1":    settings.group1,
        "2":    settings.group2
    }
    count = 0
    while True:
        print(msg_group)
        opts = input("Group options >>:").strip()
        if opts in msg_group_dic:
           for items in msg_group_dic[opts]:
               print(items,":",msg_group_dic[opts][items]["ip"])
               count += 1

           db = msg_group_dic[opts]
        return count,db
        # return [num1,num2]


def Threads(num, db):
    '''
    初始化线程和启动线程
    :return:
    '''
    while True:
        cmd = input("cmd shell>>:").strip()
        if not cmd:
            continue
        else:
            for keys in db:
                host = db[keys]["ip"]
                port = db[keys]["port"]
                user = db[keys]["user"]
                pwd = db[keys]["password"]
                p = threading.Thread(target=Commands, args=(host,port,user,pwd,cmd ))
                p.start()
                # p.join()

def Commands(host, port, user, pwd, cmd):
    '''
    命令执行函数，线程启动后循环执行命令
    :return:
    '''
    # print("in command db", host, port, user, pwd)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,port=port,username=user,password=pwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    rlt = stdout.read()
    print("\033[31;1m [%s] Result \033[0m".center(50,'*')% host)
    print(rlt.decode())
    ssh.close()

def FileInteractive():
    '''
    发送文件函数，线程启动后和相应的组进行文件交互
    :return:
    '''
    print("running file options")


def HostManager(num, db):
    '''
    主机交互管理
    :return:
    '''
    msg_manager = u'''\033[35;1m
    --------- options info -------
    1:  execute commands
    2:  file transport\033[0m
    '''
    msg_manager_dic = {
        "1":    Commands,
        "2":    FileInteractive
    }
    while True:
        print(msg_manager)
        opts = input("options>>:").strip()
        if opts in msg_manager_dic:
            Threads(num, db)
            # msg_manager_dic[opts]()
        else:
            print("Options error.")

        return True

def Run():
    '''
    入口函数
    :return:
    '''
    num,db = Group()
    HostManager(num,db)

