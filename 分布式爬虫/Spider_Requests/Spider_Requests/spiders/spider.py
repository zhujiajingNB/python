# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'wuGuNY'
    base_url = "http://policy.wugu.com.cn/1_"
    #起始页面
    def start_requests(self):
        store_cahe={"information_categories":"政策法规","base_url":"http://policy.wugu.com.cn/1.html"}
        yield scrapy.Request(url="http://policy.wugu.com.cn/1.html",meta=store_cahe)
        #测试下载中间件捕获异常
        # yield scrapy.Request(url="http://policy.wuguasdfsdfg.coam.cn/1.html", meta=store_cahe)
    #提前页数信息
    def parse(self, response):
        #当前页
        current_page = response.xpath("//span[@class='page_num']//a[@class='current']/text()").extract_first()
        #下一页
        next_page = response.xpath("//span[@class='page_num']//a[@class='next_page']").extract_first()
        #测试爬虫中间件
        # raise Exception("抛出异常")
        #跳转下一页条件
        if next_page:
            next_page=str(int(current_page)+1)
            url = self.base_url+next_page+".htm"
            yield scrapy.Request(url,callback=self.parse,meta=response.meta)
    #解析内容页面函数，函数名与Spider_Rseponse对应
    def detail_info(self):
        pass