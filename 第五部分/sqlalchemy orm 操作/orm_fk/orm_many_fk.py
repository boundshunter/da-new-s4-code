#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship # relationship 在内存中构建关联关系
from sqlalchemy import Column,Integer,Index,String,DATE,PrimaryKeyConstraint,UniqueConstraint,ForeignKey,create_engine

# charset=utf8 加入此设置才能支持中文，encoding=utf-8 不管用
engin = sqlalchemy.create_engine("mysql+pymysql://root:gxw#mP8t@10.0.1.110/stumanage?charset=utf8",encoding='utf-8',echo=True)
Base = declarative_base()


# 一对多个外键
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    billing_address_id = Column(Integer,ForeignKey("address.id"))
    shipping_address_id = Column(Integer,ForeignKey("address.id"))
    #这样sqlachemy就能分清哪个外键是对应哪个字段了foreign_keys=[billing_address_id]
    bill_address = relationship("Address",foreign_keys=[billing_address_id]) # 此关联关系建立在内存中
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

Base.metadata.create_all(engin)
# Base.metadata.drop_all(engin)
