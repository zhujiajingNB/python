# 具体逻辑可参考 tornado_demo
import asyncio
from asyncio import Queue

q = Queue(maxsize=10)

async def consumer():
    while 1:
        item = await q.get()
        if item is None:
            return
        try:
            print("doing work on %s"%item)
            await asyncio.sleep(1)
        except:
            pass
        finally:
            print("计数减{}".format(item))
            q.task_done()

async def producer():
    for item in range(10):
        await q.put(item)
        print("put item{}".format(item))

async def main():
    print("start work")
    task = asyncio.ensure_future(asyncio.wait([consumer() for _ in range(3)]))
    print("start producer")
    await producer()
    await q.join()
    print("Done")
    for i in range(10):
        await q.put(None)
        print("put None{}".format(i))
    await task
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
