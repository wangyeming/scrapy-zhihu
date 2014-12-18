# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from zhihuModel import Question, db_connect, create_question_table

class ZhihuPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_question_table(engine)
        self.Session = sessionmaker(bind=engine)
        # self.file = open('ZhihuSpider.json', 'w')

    def process_item(self, item, spider):
        print 'spider:', spider.name
        session = self.Session()
        if spider.name == 'ZhihuQuestion':
            question = Question(**item)
            session.add(question)
            session.commit()
        '''
        if spider.name == 'ZhihuQuestion':
            answer = Answer(**item)
            session.add(answer)
            session.commit()
        '''
        return item

    # def close_spider(spider):
        # file.close()
