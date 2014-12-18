# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

#禁止cookies,防止被ban
# COOKIES_ENABLED = False

LOG_LEVEL = 'WARNING'

ITEM_PIPELINES = {'zhihu.pipelines.ZhihuPipeline': 100}

DATABASE = {'drivername': 'sqlite',
            'database': 'zhihu.sqlite3'}
