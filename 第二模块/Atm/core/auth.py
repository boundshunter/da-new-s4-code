#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os

import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
import json
import datetime
import hashlib
# db_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
# sys.path.append(db_dir)
#
from core import db_handler
from conf import settings
from core import accounts

def acc_auth(account,password):
    '''
    用户认证（根据用户输入账户，密码）
    :param account:
    :param password:
    :return: account_data
    '''
    db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE = conn_parms
    account_file = "%s/%s.json" % (db_path, account)
    # print(db_path)
    # print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            # print(account_data)

        if account_data['password'] == password:

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],'%Y-%m-%d')
            '''
            注意 strptime 和 strftime的区别
            strftime 是日期转换成字符串 datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')
            strptime 是字符串转换成日期 datetime.datetime.strptime('sep-21-09 16:33:33','%b-%d-%y %H:%M:%S')

           '''
            status = account_data['status']
            if datetime.datetime.now() > exp_time_stamp:
                print("\033[32;1m您的账户 [%s] 已过期，请联系管理员申请新的卡片！\033[0m"%(account))
            elif status == 0  or status == 8:
                # print(account_data)
                return account_data
            else:
                print("\033[31;1m您的账户状态有误，请联系管理员\033[0m")
        else:
            print("\033[32;1mAccount or password is not incorrect\033[0m")
    else:
        print(" 您的账户\033[33;1m [%s] \033[0m不存在"%(account))





def acc_login(user_data,log_obj):
    '''

    :param user_data:
    :param log_obj:
    :return: auth  =  account_data
    '''
    account = input('请输入账户ID:'.strip())
    password = input('请输入密码:'.strip())

    retry_count = 0
    exit_count = 3
    same_count = 0

    while user_data['is_authorized'] is False and retry_count < exit_count:
        auth = acc_auth(account,password)  # 返回 account_data  登录验证：验证用户，密码，状态，是否过期

        if auth:  # 如果非空
            user_data['is_authorized'] = True
            user_data['account_id'] = account
            # account_data = auth
            return auth
            # return account_data
        retry_count += 1

    else:
        same_count += 1
        if same_count == 3:
            log_obj.error("accounts [%s] too many login attempts" % account)
            exit()



def sign_up():

    exist_flag = True
    while exist_flag is True:
        account = input("请输入用户ID:".strip())
        password =input("请输入密码:".strip())
        user_exist = check_account(account)

        if user_exist:  # not None
            print("用户[%s]已存在，请输入其他用户ID" % account)
            exit_flag = True
            # continue
        else:
            curr_day = datetime.datetime.now().strftime("%Y-%m-%d")
            yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)  # 昨天日期
            after_3_years_day = yesterday.replace(year=(int(yesterday.strftime("%Y")) + 3))  # 三年后的昨天
            expire_day = after_3_years_day.strftime('%Y-%m-%d')   # 过期日期
            pay_day = 22

            account_data = {
                        'enroll_date': curr_day,
                        'password': password,
                        'id': account,
                        'credit': 15000,
                        'status': 0,
                        'balance': 0.0,
                        'expire_date': expire_day,
                        'pay_day': pay_day
             }
            accounts.dump_account(account_data)
            print("\033[32;1m账户 [%s] 创建成功，\033[0m" % account)
            print("账户信息:", account_data)
            return True  # 跳出当前循环

def account_info():
    '''
    :return:
    '''
    while True:
        account = input("账户ID>>>:".strip())
        account_data = check_account(account)  # True  return account_data
        # print(account_data)
        if account_data:  # not None    is  account_data
            # print(account_data)
            display_account_info(account_data)
            return True
        else:
            print("您查询的账户[%s] 不存在" % account)
            return True
    # return True

def display_account_info(account_data):
    '''
    :param account_data:
    :return True:
    '''
    account_data['password']=get_md5(account_data['password'].encode("utf-8")) # 密码加密
    for k in account_data:
        print("{:<20}:\033[32;1m{:<20}\033[0m".format(k,account_data[k]))
    return True

def get_md5(password):
    # 获取 md5
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


def account_modify():
    '''
    修改账户信息
    :return:
    '''
    retry_count = 0
    items = ['enroll_date','password','id','credit','status','balance','expire_date','pay_day']
    while True:
        account = input("输入要修改的账户ID>>>:")
        acc_data = check_account(account)   # if True  return  account_data dict
        db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE = conn_parms
        account_file = "%s/%s.json" % (db_path, account)
        if acc_data:  # Not None
            display_account_info(acc_data)
            # print(type(acc_data))
            while True:
                input_item = input("请选择您要修改的项目>>>:")
                input_value = input("请输入您要修改的值>>>:")
                acc_data[input_item] = input_value
                account_data = acc_data
                print("\033[31;1m您已将账户ID为[%s] 中项目 [%s] 值修改为 [%s] !\033[0m" % (account,input_item,input_value))

                accounts.dump_account(account_data)  # 修改数据写回用户ID数据文件
            #     with open(account_file,'w') as f:
            #         json.dump(acc_data,f)
            #
            #     return True
            # return True
                return True
        else:
            print("您要修改的用户 [%s] 不存在！" % account)
            return True


def check_account(account):
    '''
    检查用户是否存在
    :param account:用户ID
    :return: account_data
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)

    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            status = account_data['status']
            if status == 8:
                print("权限不足，账户为管理员.")
                return False

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],"%Y-%m-%d")
            curr_time = datetime.datetime.now()
            if  curr_time > exp_time_stamp:
                print("账户 [%s] 已过期!" % account)
                return False
            else:
                return account_data
    else:
        return False


