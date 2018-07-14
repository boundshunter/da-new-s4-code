#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import sys,os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from orm_fk import orm_many_fk
from sqlalchemy.orm import sessionmaker

SessionClass = sessionmaker(bind=orm_many_fk.engin)
session = SessionClass()

addr1 = orm_many_fk.Address(street='NanKairoad',city="Tianjin",state="Hebei")
addr2 = orm_many_fk.Address(street='wudaokou',city="Beijng",state="Beijing")
addr3 = orm_many_fk.Address(street='Yanjiao',city="Langfang",state="Hebei")

c1 = orm_many_fk.Customer(name='Alex',billing_address=addr1,shipping_address=addr3)
c2 = orm_many_fk.Customer(name='Jack',billing_address=addr2,shipping_address=addr2)
session.add_all([addr1,addr2,addr3])
# session.commit()

session.add_all([c1,c2])
session.commit()
