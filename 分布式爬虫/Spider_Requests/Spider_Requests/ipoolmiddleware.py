
import logging
import requests
import random
import scrapy.downloadermiddlewares.retry
class ProxyMiddleware(object):
    def __init__(self, proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url
    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False
    def process_request(self, request, spider):
        #retry_time有值时使用ip代理池
        if request.meta.get('retry_time'):
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + proxy)
                request.meta['proxy'] = uri
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )
class ProcessRefuseMiddleware(object):
    def __init__(self,response_status,max_retry_time):
        self.response_status=response_status
        self.max_retry_time=max_retry_time
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            response_status=settings.get('RESPONSE_STATUS'),
            max_retry_time =settings.get('MAX_RETRY_TIME')
        )
    def process_response(self, request, response, spider):
        # 捕获RESPONSE_STATUS的响应，进行更换ip重新请求
        if response.status in self.response_status:
            logging.warning("该网站有封ip的危险！！！")
            #拷贝请求
            retryreq = request.copy()
            #初始化请求次数
            retry_time = retryreq.meta.get("retry_time", 0) + 1
            retryreq.meta["retry_time"] = retry_time
            #不过滤该请求
            retryreq.dont_filter = True
            #当请求次数大于最大次数，不再请求
            if retry_time > self.max_retry_time:
                logging.warning("%s:该请求更换ip后仍旧失败"%(response.url))
                return response
            return retryreq
        # 其他状态码不处理
        return response