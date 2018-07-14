#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey,PrimaryKeyConstraint,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

# 创建连接池

engin = sqlalchemy.create_engine("mysql+pymysql://root:gxw#mP8t@10.0.1.110/stumanage",encoding='utf-8',echo=True)

Base = declarative_base() # 创建基类

# 继承基类创建表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
        UniqueConstraint('id','name',name='uix_id_name'),
        Index('ix_id_name',name,extra),
    )


# 一对多
class Favor(Base):
    __tablename__= 'favor'
    nid = Column(Integer,primary_key=True)
    caption = Column(String(50),default='red',unique=True)

class Persion(Base):
    __tablename__ = 'person'
    nid = Column(Integer,primary_key=True)
    name = Column(String(32),index=True,nullable=True)
    favor_id = Column(Integer,ForeignKey("favor.nid"))

# 多对多
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=True)
    port = Column(Integer,default=22)

class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(50),unique=True,nullable=False)

class ServerGroup(Base):
    __tablename__ = 'servergroup'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    server_id = Column(Integer,ForeignKey('server.id'))
    group_id = Column(Integer,ForeignKey('group.id'))

def init_db():
    Base.metadata.create_all(engin)

def drop_db():
    Base.metadata.drop_all(engin)

init_db() # 调用此处已经开始创建表
# drop_db() # drop stumanage库中所有的表

#等同于Base.metadata.create_all(engin) # 创建表结构，调用create_all()方法创建表 调用engin连接

# 下面定义的是关于操作表的过程中需要使用的
# SessionClass = sessionmaker(bind=engin) # 建立连接，使用engin的连接 此处是创建一个类SessionClass
# session = SessionClass() # 实例化sessionclass类

# 注：设置外检的另一种方式 ForeignKeyConstraint(['other_id'], ['othertable.other_id'])


