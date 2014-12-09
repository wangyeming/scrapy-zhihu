from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from zhihu.items import ZhihuItem

class ZhihuSpider(CrawlSpider):
    name = "zhihu_spider"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/"
    ]
    rules = [Rule(LinkExtractor(allow=['/question/\d+']), 'parse_torrent')]

    def parse(self, response):
        item = ZhihuItem()
        item['url'] = response.url
        item['question_title'] = response.xpath("//title/text()").extract()
        item['question_describtion'] = response.xpath("//div[@class='zm-editable-content']").extract()
        return item
