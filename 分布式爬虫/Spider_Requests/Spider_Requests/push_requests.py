import re
import pickle
import scrapy
from scrapy import utils
from redis import StrictRedis
from scrapy import signals
from scrapy.utils.reqser import request_to_dict, request_from_dict
from Spider_Requests.conn import Redis
from Spider_Requests import settings
from scrapy_redis.queue import LifoQueue
from urllib.parse import urljoin
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from twisted.internet import defer
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError
import logging
class SpiderPushUrl(object):
    serializer = pickle
    redis_host = settings.REDIS_HOST
    port = settings.REDIS_PORT
    reids = Redis(redis_host, port)
    key = settings.REDIS_KEY
    server = reids.get_con()
    def process_request(self, request, spider):
        return None
    #存储requests
    def push(self, request,spider):
        """Push a request"""
        self.server.lpush(self.key, self._encode_request(request,spider))
    #序列化requests
    def _encode_request(self, request,spider):
        """Encode a request object"""
        obj = request_to_dict(request,spider)
        return self.serializer.dumps(obj)
    def process_response(self, request, response, spider):
        store_cahe = {}
        base_url = "http://news.wugu.com.cn"
        node_list = response.xpath("//li[@class='list_item']")
        store_cahe["information_categories"] = request.meta.get("information_categories", None)
        for node in node_list:
            title = node.xpath("./a/@title").extract_first()
            issue_time = node.xpath("./span[@class='time']/text()").extract_first()
            content_url = node.xpath("./a/@href").extract_first()
            store_cahe["title"] = title
            if re.match("http.*", content_url):
                store_cahe["content_url"] = content_url
            else:
                store_cahe["content_url"] = base_url + content_url
            store_cahe["issue_time"] = issue_time
            req = scrapy.Request(store_cahe["content_url"], callback=spider.detail_info, meta=store_cahe)
            req.meta["id"] = utils.request.request_fingerprint(req)
            # 存储请求
            self.push(req, spider)
        return response
    #对个别响应异常的网站进行捕获和存储
    def process_exception(self, request, exception, spider):
        ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                          ConnectionRefusedError, ConnectionDone, ConnectError,
                          ConnectionLost, TCPTimedOutError, ResponseFailed,
                          IOError, TunnelError)
        # 经过内置中间件后仍旧异常时
        if isinstance(exception, ALL_EXCEPTIONS):
            logging.error("错误请求:%s" % (request))


