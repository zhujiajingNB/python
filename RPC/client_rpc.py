import thriftpy2
import asyncio
import pickle
import time
import datetime
from thriftpy2.rpc import make_aio_client
pingpong_thrift = thriftpy2.load(
    "pingpong.thrift",
    module_name="pingpong_thrift")


async def request():
    client = await make_aio_client(pingpong_thrift.PingPong, '127.0.0.1', 8000)
    data = await client.ping()
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(pickle.loads(data), date)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([request(), request()]))
