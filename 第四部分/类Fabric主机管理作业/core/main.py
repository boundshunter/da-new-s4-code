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
        print(msg_group) # 打印分组信息
        opts = input("Group options >>:").strip()
        if opts in msg_group_dic:
           # 循环显示选定组内IP信息
           for items in msg_group_dic[opts]:
               print(items,":",msg_group_dic[opts][items]["ip"])
               count += 1
        db = msg_group_dic[opts]
        # 将组内成员个数和成员数据（字典）返回
        return count,db

def Threads(num, db, func_name):
    '''
    初始化线程和启动线程函数,根据传入func_name 并行运行对一组主机进行操作
    :return:
    '''
    # print("\033[42;1m In thread\033[0m")
    # print(num,db,func_name)
    if func_name == "Commands":
        while True:
            print("按 'q' 返回")
            cmd = input("cmd shell>>:").strip()
            if cmd == "q":
                return False
            if not cmd:
                continue
            else:
                for keys in db:
                    host = db[keys]["ip"]
                    port = db[keys]["port"]
                    user = db[keys]["user"]
                    pwd = db[keys]["password"]
                    # 并发循环启动线程
                    p = threading.Thread(target=Commands, args=(host,port,user,pwd,cmd, ))
                    p.start()
                    p.join() # 等待线程执行结束
    else:
        print("\033[31;1m当前目录存在测试文件 test_putfile \033[0m".center(10,'-'))
        while True:
            print("按 'q' 返回")
            # 上传文件名
            put_file_name = input("input file name>>:").strip()
            # 判断文件是否为空（为空重新输入）
            if put_file_name == "q":
                return False
            if not put_file_name:
                continue
            # 判断本地文件是否存在(不存在重新输入）
            if not os.path.isfile(put_file_name):
                continue
            else: # 文件存在启动线程
                for keys in db:
                    host = db[keys]["ip"]
                    port = db[keys]["port"]
                    user = db[keys]["user"]
                    pwd = db[keys]["password"]
                    # 并发循环启动线程
                    p = threading.Thread(target=FileInteractive, args=(host,port,user,pwd,put_file_name, ))
                    p.start()
                    p.join() # 等待线程执行结束


def Commands(host, port, user, pwd, cmd):
    '''
    命令执行函数，线程启动后循环执行命令
    :return:
    '''
    # print("in command db", host, port, user, pwd)
    # 初始化 远程连接类
    ssh = paramiko.SSHClient()
    # 忽首次登录的交互，直接加入known_hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 传入信息，建立连接
    ssh.connect(hostname=host,port=port,username=user,password=pwd)
    # 定义输入输出，错误
    stdin, stdout, stderr = ssh.exec_command(cmd)
    rlt = stdout.read()
    print("\033[31;1m [%s] Result \033[0m".center(50,'*')% host)
    # 显示返回信息
    print(rlt.decode())
    ssh.close()

def FileInteractive(host,port,user,pwd,put_file_name):
    '''
    发送文件函数，线程启动后和相应的组进行文件交互
    同样可以下载文件，增加一个get方法
    在入口处做处理，提示用户选择上传还是下载，或者用户直接输入，通过startwith和split来处理用户行为和文件名
    :return:
    '''
    print("running file options")
    # 初始化 文件传输对象，传入ip,端口，用户，密码
    transport = paramiko.Transport((host,port))
    transport.connect(username=user,password=pwd)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 传入路径
    to_dir = "/tmp/"
    print(BASE_DIR+"/core/"+put_file_name)
    print("[%s] start put file".center(30,'-')% host)
    sftp.put(put_file_name,to_dir+"%s_%s"%(host,put_file_name))
    transport.close()
    print("[%s] Put file done"% host)

def HostManager(num, db):
    '''
    主机交互管理，可以选择执行命令和文件传输两种方式
    :return:
    '''
    msg_manager = u'''\033[35;1m
    --------- options info -------
    1:  execute commands
    2:  file transport\033[0m
    '''
    msg_manager_dic = {
        "1":    "Commands",
        "2":    "FileInteractive"
    }
    while True:
        print(msg_manager)
        print("[q] 退出程序")
        opts = input("options>>:").strip()
        if opts in msg_manager_dic:
            funcname = msg_manager_dic[opts]
            # 将 组内成员个数，成员字典，函数名，传输给线程处理
            Threads(num, db, funcname)
        elif opts == 'q':
            return False
        else:
            print("Options error.")

def Run():
    '''
    入口函数
    :return:
    '''
    num,db = Group()
    HostManager(num,db)

