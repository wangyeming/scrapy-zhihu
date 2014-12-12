# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from zhihu.items import ZhihuQuestionItem


class ZhihuquestionSpider(CrawlSpider):
    name = 'ZhihuQuestion'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/']


    rules = (
        Rule(LinkExtractor(allow=r'question/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        questions = []
        question = ZhihuQuestionItem()
        question['_id'] = response.url.split('/')[-1]
        question['url'] = response.url.encode('utf-8')
        question['title'] = response.xpath('//div[@id="zh-question-title"]/h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        question['question_summary'] = response.xpath('//div[@id="zh-question-detail"]/div[@class="zh-summary summary clearfix"]').extract()
        question['question_description'] = response.xpath('//div[@id="zh-question-detail"]/textarea[@class="content hidden"]/text()').extract()
        # question['answer_num'] = response.xpath('//h3[@id="zh-question-answer-num"]/text()').extract()
        answer_list = response.xpath('//div[@id="zh-question-answer-wrap"]/div[@class="zm-item-answer "]')
        question['answer_num'] = len(answer_list)
        # answer循环
        for sel in answer_list:
            question['answerer_name'] = ''.join(response.xpath('//div[@class="answer-head"]/div/h3/a2/text()').extract())
            question['answerer_tag'] = ''.join(response.xpath('//div[@class="answer-head"]/div/h3/strong/text()').extract())
            question['answer_approve_num'] = ''.join(
                response.xpath('//div[@class="zm-votebar goog-scrollfloater"]/button/span[@class="count"]/text()').extract())
            question['answer_content'] = ''.join(response.xpath('//div[@class="zm-item-rich-text"]/div/text()').extract())
            question['answer_edittime'] = ''.join(
                response.xpath(
                    '//div[@class="zm-item-meta zm-item-comment-el answer-actions clearfix"]/div[@class="zm-meta-panel"]/span/a/text()').extract())
            question['answer_comment_num'] = ''.join(
                response.xpath('//div[@class="zm-item-meta zm-item-comment-el answer-actions clearfix"]/div[@class="zm-meta-panel"]/a/i/text()').extract())
        questions.append(question)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return questions

    '''
    def answer_num(response)
        answer_num = response.xpath('//h3[@id="zh-question-answer-num"]/text()').extract()
        if(answer_num.):
    '''
