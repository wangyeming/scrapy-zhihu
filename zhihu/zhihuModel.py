# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_question_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Question(DeclarativeBase):
    __tablename__ = "zhihu_questions"

    id = Column(Integer, primary_key=True)
    _id = Column("_id", Integer)
    url = Column("url", String)
    title = Column("title", String)
    '''
    question_summary = Column("question_summary", String)
    question_description = Column("question_description", String)
    answer_num = Column("answer_num", String)
    '''

'''
class Answer(DeclarativeBase):
    __tablename__ = "zhihu_answers"

    id = Column(Integer, primary_key=True)
    question_id = Column("question_id", String)
    # answer_id = Column(Integer)
    url = Column("url", String)
    answerer_name = Column("answerer_name", String)
    answerer_tag = Column("answerer_tag", String)
    answer_approve_num = Column("answer_approve_num", String)
    answer_content = Column("answer_content", String)
    answer_edittime = Column("answer_edittime", String)
    answer_comment_num = Column("answer_comment_num", String)
'''
