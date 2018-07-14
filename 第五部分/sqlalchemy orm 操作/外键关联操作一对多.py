#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship # relationship 在内存中构建关联关系
from sqlalchemy import Column,Integer,Index,String,DATE,PrimaryKeyConstraint,UniqueConstraint,ForeignKey,create_engine

engin = sqlalchemy.create_engine("mysql+pymysql://root:gxw#mP8t@10.0.1.110/stumanage",encoding='utf-8',echo=True)
Base = declarative_base()

# '''
# 一对多关系

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False) # 不允许为空
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>"% (self.id,self.name)

class StudyRecode(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True,autoincrement=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))

    # #这个nb，允许你在student表里通过backref字段反向查出所有它在study_record表里的关联项
    student = relationship("Student",backref="my_stu_record")


def init_db():
    Base.metadata.create_all(engin)

def drop_db():
    Base.metadata.drop_all(engin)
# drop_db()
init_db()
# # '''
#
stu_1 = Student(name='alex',register_date='2017-05-28')
stu_2 = Student(name='alfx',register_date='2017-06-28')
stu_3 = Student(name='algx',register_date='2017-07-28')
stu_4 = Student(name='alhx',register_date='2017-08-28')
stu_5 = Student(name='alix',register_date='2017-09-28')

stu_rd_1 = StudyRecode(day='1',status="Yes",stu_id='1')
stu_rd_2 = StudyRecode(day='2',status="No",stu_id='1')
stu_rd_3 = StudyRecode(day='3',status="Yes",stu_id='1')
stu_rd_4 = StudyRecode(day='4',status="Yes",stu_id='1')
stu_rd_5 = StudyRecode(day='1',status="Yes",stu_id='2')

SessionClass = sessionmaker(bind=engin)
session = SessionClass()

session.add_all([stu_1,stu_2,stu_3,stu_4,stu_5,stu_rd_1,stu_rd_2,stu_rd_3,stu_rd_4,stu_rd_5])

session.commit()