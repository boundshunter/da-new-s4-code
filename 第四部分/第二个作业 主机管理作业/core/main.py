#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import paramiko,sys,os,threading

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

class Groups(object):
    '''
    显示组内成员，参数为组名
    :param group_name:
    :return:
    '''
    def __init__(self):
        self.group_1 = settings.group1
        self.group_2 = settings.group2
        self.ssh = paramiko.SSHClient()
        # self.transport = paramiko.Transport()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # def thread(self,group):
    #     if group == "group1":
    #         for items in
    #             p = threading.Thread(target=exec_cmd,args=(,))
    #
    #     else:
    #         pass
    #
    #     p = threading.Thread(target=func,args=(dic,))
    #     p.start()

    def interactive(self,group):
        # print("interactive",group)
        msg = u'''
        -------操作选项--------
        1、执行命令
        2、发送文件
        '''
        msg_dic = {
            "1":"exec_cmd",
            "2":"send_file"
        }
        group_name = group
        while True:
            print(msg)
            choice = input("2>>:").strip()
            if choice in msg_dic:
                self.thread(group)
            # if hasattr(self,msg_dic[choice]):
            #     func = getattr(self,msg_dic[choice])
            #     func(group)
            #     return True
            else:
                print("interactive 中选项错误，重新输入")

    def exec_cmd(self,group):
        # print("进入exec_cmd",group)
        if group == "group1":
            p = threading.Thread(target=exec_cmd,args=(,))

        elif group == "group2":
            pass
        else:
            print("xxx")


        # print("exec cmd",dic)
        # hostname = dic["ip"]
        # port = dic["port"]
        # username = dic["user"]
        # password = dic["password"]
        # print(hostname,port,username,password)
        # self.ssh.connect(hostname=hostname,port=port,username=username,password=password)
        #
        # cmd = input("3.1输入命令>>:").strip()
        # stdin, stdout, stderr = self.ssh.exec_command(cmd)
        # rlt = stdout.read()
        # print(rlt.decode())
        # self.ssh.close()

    def send_file(self):
        pass

    def run(self):
        msg = u'''
        1、Host Group 1
        2、Host Group 2
        '''

        dict = {
            "1":self.group_1,
            "2":self.group_2
        }
        while True:
            print("分组信息".center(20,'*'))
            print(msg)
            option = input("1输入选项>>:").strip()
            if option in dict:
                h_dict = dict[option]
                for items in h_dict:
                    print(items,":",h_dict[items]["ip"])
                    # db = h_dict[items]
                group = "group%s"% option
                self.interactive(group)
                return group
            else:
                print("\033[31;1m选择有误，请重新选择。\033[0m")



obj = Groups()
obj.run()