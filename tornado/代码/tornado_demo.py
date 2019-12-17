from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

# 非阻塞对列
q = Queue(maxsize=10)

# 消费者
async def consumer():
    # 无限循环遍历对列，不停止
    async for item in q:
        # 当前协程终止条件
        if item is None:
            return
        try:
            print("doing work on %s"%item)
            await gen.sleep(1)
        except:
            pass
        finally:
            print("计数减{}".format(item))
            # 每取出一个，对列计数减一
            q.task_done()

# 生产者
async def producer():
    for item in range(10):
        # 往对列放入数据
        await q.put(item)
        # await gen.sleep(2)
        print("put item{}".format(item))

async def main():
    # 将协程放入事件循环中运行，返回该task对象，可监控协程运行情况
    works = gen.multi([consumer() for _ in range(3)])
    print("start producer")
    # 启动生产者
    await producer()
    # 等待对列计数为0
    await q.join()

    print("Done")

    # 协程终止条件
    for i in range(10):
        await q.put(None)
        print("put None{}".format(i))

    # 监控协程运行到结束
    await works

if __name__ == '__main__':
    IOLoop.current().run_sync(main)