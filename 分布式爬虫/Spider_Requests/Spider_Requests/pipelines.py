# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from Spider_Requests.items import ErrorRequest
class SpiderRequestsPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ErrorRequest):
            return item
        # return item