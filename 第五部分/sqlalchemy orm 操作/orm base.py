#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
# engin = create_engine("mysql+pymysql://root:gxw#mP8t@10.0.1.110/test",encoding='utf-8',echo=True) # echo=True(打印执行过程的debug日志）
engin = create_engine("mysql+pymysql://root:gxw#mP8t@10.0.1.110/test",encoding='utf-8') # echo=True(打印执行过程的debug日志）

Base = declarative_base() # 生成 ORM 基类

# 继承
class User(Base):
    __tablename__ = 'user' # 表名
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False)
    password = Column(String(64),nullable=False)

    def __repr__(self):
        return "<id:%s name:%s password:%s>"%(self.id,self.name,self.password)

Base.metadata.create_all(engin) # 创建表结构，调用Base类的create_all方法，使用engin引擎连接
SessionClass = sessionmaker(bind=engin) # 创建于数据库的会话 sessionclass（此时还是一个类）
session_obj = SessionClass() # 这里才生成 类的对象

'''
# 插入数据过程

# 生成要创建的数据对象
user_obj = User(name='alex',password='alex3714')
user_obj1 = User(name='susie',password='abc123')
session_obj.add(user_obj) # 把要创建的数据对象添加到这个session对象里，一会儿统一创建
session_obj.add(user_obj1)
print(user_obj.name,user_obj.password,user_obj.id)

# 多条增加
session_obj.addall([
    User(name='alex',password='alex3714'),
    User(name='albx',password='alex3715'),
])

session_obj.commit() # 此处统一提交，创建数据

# 查询数据过程
# data = session_obj.query(User).filter_by().all() # 默认返回的是数据对象，需要返回值，是通过21-22行的内置函数返回
# data = session_obj.query(User).filter_by().first() # 默认返回的是数据对象，需要返回值，是通过21-22行的内置函数返回
                                                   # first() 取第一条数据
                                                   # 等于的条件，用filter_by，大于小于类的条件，用filter
# data_filter = session_obj.query(User).filter_by(id=1).all()
data_filter_by = session_obj.query(User).filter_by(id=1).all() # 显示所有的时候两种方式相同
# data_filter = session_obj.query(User).filter(User.id>1).all() # 条件大于，小于情况需要跟表名，否则报错
# data_filter = session_obj.query(User).filter(User.id==2).all() # filter 判断等于用双等号，而且要使用[表名.字段名]+条件的格式
# print(data)
# 多条件查询
data_filter = session_obj.query(User).filter(User.id>1).filter(User.id<3).all() # 多条件 filter
data_filter_like = session_obj.query(User).filter(User.name.like("%su%")).all() #模糊匹配查询 like

print(data_filter_by)
print(data_filter)
print(data_filter_like)

# 数据修改
# 单条数据修改
data_sel = session_obj.query(User).filter().first() #查询第一条数据（对象）
print(data_sel)

#对象修改
data_sel.name = "Jack Wang"
data_sel.password = "wangJ!@#"
# 修改提交
session_obj.commit()
# 再次查询，确认修改
data_sel = session_obj.query(User).filter().first()
print(data_sel)

# 回滚
my_user = session_obj.query(User).filter().first() # 修改第一条
my_user.name = 'abc'

fake_user = User(name='hanboger',password='abc123') # 增加一条数据
session_obj.add(fake_user)

data=session_obj.query(User).filter(User.name.in_(['abc','hanboger'])).all()
print(data) # 打印修改和增加的数据

session_obj.rollback() # 回滚数据
data=session_obj.query(User).filter(User.name.in_(['abc','hanboger'])).all() # 再次获取修改和增加的数据
print(data) # 打印结果，发现已经回滚
'''
# 统计和分组
from sqlalchemy import func
print(session_obj.query(User.name,func.count(User.name)).group_by(User.name).all())# 按照name分组排序，后面是出现的次数

# delete

print(session_obj.query(User).filter(User.id==1).all()) # 删除前查看数据
print(session_obj.query(User).filter(User.id==1).delete()) # 删除
print(session_obj.query(User).filter(User.id==1).all()) # 删除后查看数据

# update
session_obj.query(User).filter(User.id > 2).update({"name" : "099"})
session_obj.query(User).filter(User.id > 2).update({User.name: User.name + "099"}, synchronize_session_obj=False)
session_obj.query(User).filter(User.id > 2).update({"num": User.num + 1}, synchronize_session_obj="evaluate")
session_obj.commit()
# select
ret = session_obj.query(User).all()
ret = session_obj.query(User.name, User.extra).all()
ret = session_obj.query(User).filter_by(name='alex').all()
ret = session_obj.query(User).filter_by(name='alex').first()

ret = session_obj.query(User).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(User.id).all()

ret = session_obj.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()


# 通配符
ret = session.query(Users).filter(Users.name.like('e%')).all()
ret = session.query(Users).filter(~Users.name.like('e%')).all()

# 限制
ret = session.query(Users)[1:2]

# 排序
ret = session.query(Users).order_by(Users.name.desc()).all()
ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

# 分组
from sqlalchemy.sql import func

ret = session.query(Users).group_by(Users.extra).all()
ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).all()

ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all()

# 连表

ret = session_obj.query(User, Favor).filter(User.id == Favor.nid).all()

ret = session_obj.query(Person).join(Favor).all()

ret = session_obj.query(Person).join(Favor, isouter=True).all()


# 组合
q1 = session_obj.query(User.name).filter(User.id > 2)
q2 = session_obj.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union(q2).all()

q1 = session_obj.query(User.name).filter(User.id > 2)
q2 = session_obj.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union_all(q2).all()