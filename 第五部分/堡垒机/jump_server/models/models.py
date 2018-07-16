#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,Integer,Index,DATE,ForeignKey,UniqueConstraint,PrimaryKeyConstraint,Table
from sqlalchemy_utils import ChoiceType,PasswordType
from sqlalchemy import create_engine

Base = declarative_base()

#多对多（mtm）关系建立

user_mtm_bindhost = Table('user_mtm_bindhost',Base.metadata,
                            Column('user_profile_id',Integer,ForeignKey('user_profile.id')),
                            Column('bindhost_id',Integer,ForeignKey('bind_host.id')),
                            )

bindhost_mtm_hostgroup = Table('bindhost_mtm_hostgroup',Base.metadata,
                               Column('bindhost_id',Integer,ForeignKey('bind_host.id')),
                               Column('hostgroup_id',Integer,ForeignKey('group.id')),
                               )

user_mtm_hostgroup = Table('user_mtm_hostgroup',Base.metadata,
                           Column('userprofile_id',Integer,ForeignKey('user_profile.id')),
                           Column('hostgroup_id',Integer,ForeignKey('group.id')),
                           )
class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    # 关联关系参数说明，(建立关系的类名、第三张关系表的表名，允许remote_user反查的名字
    # 一个主机包含多个用户，一个用户关联多个主机，关系建立
    # remote_users = relationship('RemoteUser',secondary=host_mtm_remoteuser,backref='hosts')

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64),unique=True)
    bind_hosts = relationship("BindHost",secondary='')
    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    # 联合唯一 ，联合唯一三个字段，名字为'_user_password_auth'
    __table_args__ = (UniqueConstraint('auth_type','username','password',name='_user_password_auth'))
    AuthTypes = [
        (u'ssh/password',u'SSH/Password'), # 第一个是真正存在数据库中的，第二个是显示给我们看的，第二个可以存中文之类的，这是一个映射关系
        (u'ssh-key',u'SSH/KEY'),
    ]
    id = Column(Integer,primary_key=True)
    auth_type = Column(ChoiceType(AuthTypes),comment="枚举类型")
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username

class UserProfile(Base):
    '''
    用户名，密码，权限，多对多关系
    '''
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128),unique=True)
    bind_hosts = relationship("BindHost",secondary=user_mtm_bindhost,backref='user_profiles')
    host_groups=relationship("HostGroup",secondary=user_mtm_hostgroup,backref='user_profiles')
    def __repr__(self):
        return self.username

class BindHost(Base):
    '''
    192.168.1.111    web   bj_group
     192.168.1.111    mysql  sh_group
    '''
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('host_id','group_id','remoteuser_id',name='_host_user_remoteuser_uc'))
    id = Column(Integer,primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    group_id = Column(Integer,ForeignKey('group.id'))
    remoteuser_id = Column(Integer,ForeignKey('remoteuser.id'))

    host = relationship('Host',backref='bind_hosts')
    # group = relationship('HostGroup',backref='bind_hosts')
    remote_user = relationship('RemoteUser',backref='bind_hosts')

    def __repr__(self):
        return "<%s --- %s --- %s>"% (self.host.ip,self.remote_user.username,self.group.name)
