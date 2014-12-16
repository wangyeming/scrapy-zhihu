# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ZhihuUserItem(Item):
    _id=Field()
    url=Field()
    img=Field()
    username = Field()
    nickname = Field()
    location = Field()
    industry = Field()
    sex = Field()
    jobs = Field()
    educations = Field()
    description = Field()
    sinaweibo = Field()
    tencentweibo = Field()

    followee_num = Field()
    follower_num = Field()

    ask_num = Field()
    answer_num = Field()
    post_num = Field()
    collection_num = Field()
    log_num = Field()

    agree_num = Field()
    thank_num = Field()
    fav_num = Field()
    share_num = Field()

    view_num = Field()
    update_time = Field()

class ZhihuQuestionItem(Item):
    _id = Field()
    url = Field()
    title = Field()
    question_summary = Field()
    question_description = Field()
    answer_num = Field()

class ZhihuAnswerItem(Item):
    question_id = Field()
    answer_id = Field()
    url = Field()
    answerer_name = Field()
    answerer_tag = Field()
    answer_approve_num = Field()
    answer_content = Field()
    answer_edittime = Field()
    answer_comment_num = Field()
