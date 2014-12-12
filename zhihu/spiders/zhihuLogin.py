#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request,FormRequest
from scrapy import log

from zhihu.items import ZhihuUserItem
from zhihu.settings import *
from zhihu.secrets import GlobalVar

from datetime import datetime


import sys


reload(sys)
sys.setdefaultencoding('utf-8')

host='http://www.zhihu.com'

class ZhihuLoginSpider(CrawlSpider):
    name = "zhihu_user"
    # allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com"
    ]

    # rules = [Rule(LinkExtractor(allow=['/question/\d+']), 'parse_torrent')]
    # 使用rule时候，不要定义parse方法
    rules = (
        Rule(SgmlLinkExtractor(allow=("/lookup/class/[^/]+/?$", )), follow=True,callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=("/lookup/class/$", )), follow=True,callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=("/lookup/people", )),  callback='parse_item'),
    )

    def __init__(self,  *a,  **kwargs):
        super(ZhihuLoginSpider, self).__init__(*a, **kwargs)
        self.user_names = []

    # 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request
    def start_requests(self):
        return [FormRequest(
            "http://www.zhihu.com/login",
            formdata = {'email': GlobalVar.email,
                        'password': GlobalVar.email_password,
                        '_xsrf': GlobalVar.xsrf
            },
            callback = self.after_login
        )]

    # 登录后操作
    def after_login(self, response):
        for url in self.start_urls:
            print url
            yield self.make_requests_from_url(url)

    # 解析推荐人列表
    def parse_item(self, response):
        selector = Selector(response)
        print 'response.url ' + response.url
        for link in selector.xpath('//div[@id="suggest-list-wrap"]/ul/li/div/a/@href').extract():
            #link  ===> /people/javachen
            print "link " + link
            yield Request(host+link+"/about", callback=self.parse_user)

    # 获取推荐人信息
    def parse_user(self, response):
        selector = Selector(response)
        users = []
        user = ZhihuUserItem()
        user['_id']=user['username']=response.url.split('/')[-2]
        user['url']= response.url.encode('utf-8')
        user['nickname'] = ''.join(selector.xpath("//div[@class='title-section ellipsis']/a[@class='name']/text()").extract())
        user['location'] = ''.join(selector.xpath("//span[@class='location item']/@title").extract())
        user['industry'] = ''.join(selector.xpath("//span[@class='business item']/@title").extract())
        user['sex'] = ''.join(selector.xpath('//div[@class="item editable-group"]/span/span[@class="item"]/i/@class').extract()).replace("zg-icon gender ","")
        user['description'] = ''.join(selector.xpath("//span[@class='description unfold-item']/span/text()").extract()).strip().replace("\n",'')
        user['view_num'] = ''.join(selector.xpath("//span[@class='zg-gray-normal']/strong/text()").extract())
        user['update_time'] = str(datetime.now())
        #抓取用户信息，此处省略代码

        users.append(user)
        return users
