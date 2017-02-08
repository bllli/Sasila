#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 导入:
from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class Process(Base):
    # 表的名字:
    __tablename__ = 'process_tbl'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    collect_token = Column(String(20))
    process_code = Column(Integer)
    process_cookie = Column(String(200))
    start_time = Column(DateTime)
    expire_time = Column(DateTime)
    company_account = Column(String(20))
    name = Column(String(20))
    identity_card_number = Column(String(20))
    cell_phone_number = Column(String(20))


class JdDatabase(object):
    def __init__(self):
        # 初始化数据库连接:
        self.engine = create_engine('mysql+mysqlconnector://root:root@192.168.3.210:3306/jd_manager')
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=self.engine)
        self._create_all()

    def _create_all(self):
        '''
        创建从Base派生的所有表,如果数据表存在则忽视
        :return:
        '''
        Base.metadata.create_all(self.engine)

    def _drop_all(self):
        '''
        删除DB中所有的表
        :return:
        '''
        Base.metadata.drop_all(self.engine)

    def create_session(self):
        return self.DBSession()
