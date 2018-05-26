#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import json
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from conf import config

class User_auth(object):
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.user_home_dir = config.user_home_dir + user_name
        self.user_manage()


    def user_manage(self):
        '''
        用户认证，用户存在，提示，用户不存在则将数据序列化到文件(json)
        :return:
        '''
        user_db_file = config.user_auth_file + self.user_name + '.db'
        print(user_db_file)
        if os.path.isfile(user_db_file):
            print("用户已经存在，请使用其他用户")
        else:
            self.db_handler_dump()

    def db_handler_dump(self):
        '''
        创建用户，将用户信息写入以  [用户名.db] 命名的数据文件，将用户信息写入文件
        :return:
        '''

        db_path = '%s%s' % (config.user_auth_file, self.user_name + '.db')
        print(db_path)
        user_dict = {
            'username': self.user_name,
            'password': self.user_password,
            'home': db_path
        }
        with open(db_path, 'w') as f:
            json.dump(user_dict, f)

#
    def db_handler_load(self, user):
        '''
        取出用户数据
        :return:
        '''
        print("db_handler_load:", user)
        db_path = '%s' % (user)
        print('db_path',user)
        with open(db_path) as f:
            user_db = json.load(f)
            print(user_db['username'])
            print('user_db', user_db)
            return user_db



# aa = User_auth("alex", "abc")
# user = config.user_auth_file+'alex.db'
# print(user)
# aa.db_handler_load(user)