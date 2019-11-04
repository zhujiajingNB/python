import time
import requests
import gevent
from gevent import monkey
#注意通过猴子路径修改
monkey.patch_all()


def get(url):
    r = requests.session()
    res = r.get(url)
def sychrous(url):
    start = time.time()
    for i in range(100):
        get(url)
    end = time.time()
    print("同步执行时间为", end - start)


def test_gevent(url):
    start = time.time()
    gevent.joinall([gevent.spawn(get, url) for i in range(100)])
    end = time.time()
    print("异步执行时间为", end - start)


test_gevent("http://www.baidu.com")
sychrous("http://www.baidu.com")