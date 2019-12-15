asyncio.get_event_loop()  若当前线程的事件循环还没有创建（即set_event_loop未调用），则创建一个事件循环为当前线程的，若已经创建则返回当前线程的事件循环。

asyncio.new_event_loop(loop) 设置为当前线程的事件循环

asyncio.set_event_loop() 创建一个新事件循环



添加协程：

loop.create_task(c)

asyncio.ensure_future(c)

执行阻塞io

```
loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(4)
task =loop.run_in_executor(executor,函数，参数)

tornado中
executor = ThreadPoolExecutor(4)
@run_on_server 修饰一个阻塞函数，为协程

```

多线程协程

一个创建一个线程执行事件循环

主线程中用asyncion.run_coroutine_threadsafe(函数()，loop)