import thriftpy2
import asyncio
from thriftpy2.rpc import make_aio_server
import json
import pickle
import datetime
import requests
import time
pingpong_thrift = thriftpy2.load(
    "pingpong.thrift",
    module_name="pingpong_thrift")


class Dispatcher(object):
    async def ping(self):
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(date)
        await asyncio.sleep(1)
        # res = requests.get(url="http://www.baidu.com")
        # print(res.status_code)
        dic = {
            "time": date
        }
        return pickle.dumps(dic)


if __name__ == '__main__':
    server = make_aio_server(
        pingpong_thrift.PingPong,
        Dispatcher(),
        '127.0.0.1',
        8000)
    server.serve()
