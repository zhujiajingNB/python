# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderRequestsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
#错误的请求
class ErrorRequest(scrapy.Item):
    url=scrapy.Field()
    exception = scrapy.Field()