# -*- coding: utf-8 -*-
import logging
import time
from scrapy import signals


class RedisSpiderClosedExensions(object):

    def __init__(self, idle_number, crawler):
        self.crawler = crawler
        self.idle_number = idle_number
        self.idle_list = []
        self.idle_count = 0

    @classmethod
    def from_crawler(cls, crawler):
        # IDLE_NUMBER目前被被设定为等待时间，IDLE一个时间片5秒，所以setting.py中设置的时间除以5就是时间片的数量
        idle_number = crawler.settings.getint('IDLE_TIME', 600) // 5
        ext = cls(idle_number, crawler)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.spider_idle, signal=signals.spider_idle)

        return ext

    def spider_opened(self, spider):
        logging.info("opened spider %s redis spider Idle, Continuous idle limit： %d", spider.name, self.idle_number)

    def spider_closed(self, spider):
        logging.info("closed spider %s, idle count %d , Continuous idle count %d",
                    spider.name, self.idle_count, len(self.idle_list))

    def spider_idle(self, spider):
        self.idle_count += 1
        self.idle_list.append(time.time())
        idle_list_len = len(self.idle_list)

        if idle_list_len > 2 and self.idle_list[-1] - self.idle_list[-2] > 6:
            self.idle_list = [self.idle_list[-1]]

        elif idle_list_len > self.idle_number:
            logging.info('\n continued idle number exceed {} Times'
                        '\n meet the idle shutdown conditions, will close the reptile operation'
                        '\n idle start time: {},  close spider time: {}'.format(self.idle_number,
                                                                              self.idle_list[0], self.idle_list[0]))
            self.crawler.engine.close_spider(spider, 'closespider_pagecount')