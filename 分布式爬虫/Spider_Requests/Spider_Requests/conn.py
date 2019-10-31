from redis import StrictRedis
class Redis(object):
    def __init__(self,redis_host,port):
        self.redis_host=redis_host
        self.port=port
    def get_con(self):
        return StrictRedis(host=self.redis_host, port=self.port)

