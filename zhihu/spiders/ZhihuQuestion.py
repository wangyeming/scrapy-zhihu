# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from zhihu.items import ZhihuQuestionItem
from zhihu.items import ZhihuAnswerItem


class ZhihuQuestionSpider(CrawlSpider):
    name = 'ZhihuQuestion'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'question/\d+'), callback='parse_question_item', follow=True),
    )

    def parse_question_item(self, response):
        questions = []
        question = ZhihuQuestionItem()
        question = ZhihuQuestionItem()
        question['_id'] = response.url.split('/')[-1]
        question['url'] = response.url.encode('utf-8')
        question['title'] = response.xpath('//div[@id="zh-question-title"]/h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        question['question_summary'] = response.xpath('//div[@id="zh-question-detail"]/div[@class="zm-editable-content"]/text()').extract()
        question['question_description'] = response.xpath('//div[@id="zh-question-detail"]/textarea[@class="content hidden"]/text()').extract()
        if question['title']:
            print "title", question['title'][0].encode('utf8')
        if question['question_summary']:
            print "question_summary", question['question_summary'][0].encode('utf8')
        if question['question_description']:
            print "question_description", question['question_description'][0].encode('utf8')
        # question['answer_num'] = response.xpath('//h3[@id="zh-question-answer-num"]/text()').extract()
        answer_list = response.xpath('//div[@id="zh-question-answer-wrap"]/div[@class="zm-item-answer "]')
        question['answer_num'] = len(answer_list)
        if answer_list:
            print "答案总数", str(question['answer_num'])
            # answer循环
            for sel in answer_list:
                self.parse_answer_item(response, question, sel)
        else:
            print "没有回答！"
        questions.append(question)
        # yield question
        return questions

    def parse_answer_item(self, response, question, sel):
        answers = []
        answer = ZhihuAnswerItem()
        answer['question_id'] = question['_id']
        # answer['answer_id'] =
        answer['answerer_name'] = sel.xpath('div[@class="answer-head"]/div/h3/a[2]/text()').extract()
        '''
        if len(answer['answerer_name']) == 0:
            answer['answerer_name'] = sel.xpath(
                'div[@class="answer-head"]/div[@class="zm-item-answer-author-info"]/h3[@class="zm-item-answer-author-wrap"]/text()').extract()
        '''
        answer['answerer_tag'] = sel.xpath('div[@class="answer-head"]/div/h3/strong/text()').extract()
        answer['answer_approve_num'] = sel.xpath('div[@class="zm-votebar goog-scrollfloater"]/button/span[@class="count"]/text()').extract()
        answer['answer_content'] = sel.xpath('div[@class="zm-item-rich-text"]/div/text()').extract()
        answer['answer_edittime'] = sel.xpath(
                'div[@class="zm-item-meta zm-item-comment-el answer-actions clearfix"]/div[@class="zm-meta-panel"]/span/a/text()').extract()
        answer['answer_comment_num'] = sel.xpath(
            'div[@class="zm-item-meta zm-item-comment-el answer-actions clearfix"]/div[@class="zm-meta-panel"]/a/i/text()').extract()
        if answer['answerer_name']:
            print "answerer_name", len(answer['answerer_name'])
            for answerer_name in answer['answerer_name']:
                print answerer_name.encode('utf8')
        if answer['answerer_tag']:
            print "answerer_tag", len(answer['answerer_tag'])
            for answerer_tag in answer['answerer_tag']:
                print answerer_tag.encode('utf8')
        if answer['answer_approve_num']:
            print "answer_approve_num", len(answer['answer_approve_num'])
            for answer_approve_num in answer['answer_approve_num']:
                print answer_approve_num.encode('utf8')
        if answer['answer_content']:
            print "answer_content", len(answer['answer_content'])
            for answer_content in answer['answer_content']:
                print answer_content.encode('utf8')
        if answer['answer_comment_num']:
            print "answer_comment_num", len(answer['answer_comment_num'])
            for answer_comment_num in answer['answer_comment_num']:
                print answer_comment_num.encode('utf8')
        answers.append(answer)
        # yield answer
        return answers
