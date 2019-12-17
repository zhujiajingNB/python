from tornado import web
import tornado
import time
import asyncio
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
class MainHandler(web.RequestHandler):
    executor = ThreadPoolExecutor(4)
    #当客户端发起不同在http请求时，只需重载handler中不同的请求方法
    async def get(self, *args, **kwargs):
        # time.sleep(5)
        # time.sleep(10)
        await self.background_task()
        self.write("hello world")
    # 多线程执行阻塞io操作
    @run_on_executor
    def background_task(self):
        time.sleep(10)

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()