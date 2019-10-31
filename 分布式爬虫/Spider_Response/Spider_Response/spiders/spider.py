# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from Spider_Response.items import SpiderResponseItem
import logging
class SpiderSpider(RedisSpider):
    name = 'wuGuNY'
    item = SpiderResponseItem()
    # 详情页解析
    def detail_info(self, response):
        self.item["id"] = response.meta["id"]
        self.item["title"] = response.meta["title"]
        self.item["issue_time"] = response.meta["issue_time"]
        self.item["information_categories"] = response.meta["information_categories"]
        self.item["content_url"] = response.meta["content_url"]
        self.item["source"] = response.xpath("//span[@class='words_author']/text()").extract_first()
        self.item["content"] = "".join(response.xpath("//div[@class='wd']").extract())
        self.item["tags"] = ",".join(response.xpath("//div[@class='mark']/a/text()").extract())
        self.item["images"] = ",".join(response.xpath("//div[@class='wd']//img/@data-url").extract())
        self.item["attachments"] = ",".join(response.xpath("//div[@class='wd']//a/@href").extract())
        #测试爬虫中间件
        # self.item["sdfs"]="dsfsdf"
        self.unchange_itme()
        yield self.item
    # 不变的值
    def unchange_itme(self):
        self.item["industry_categories"] = "农、林、牧、渔业"
        self.item["industry_Lcategories"] = "农业"
        self.item["information_source"] = "吾谷网"
        self.item["industry_Mcategories"] = None
        self.item["industry_Scategories"] = None
        self.item["area"] = None
        self.item["address"] = None
        self.item["author"] = None