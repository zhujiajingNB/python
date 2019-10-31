import logging
from Spider_Response.items import ErrorRequest
class StoreErrorRequets(object):
    def process_spider_exception(self,response, exception, spider):
        item = ErrorRequest()
        item["url"]=response.url
        item["exception"]=exception
        yield item
