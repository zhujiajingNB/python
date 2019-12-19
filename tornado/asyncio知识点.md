asyncio中有三类可等待对象（awaitble对象）

1. coroutine: 即协程函数

2. tasks : 任务，对协程函数的进一步封装

3. future: 它是一个“更底层”的概念，他代表一个一步操作的最终结果，因为一步操作一般用于耗时操作，结果不会立即得到，会在“将来”得到异步运行的结果，故而命名为Future。

   三者的关系：coroutine可以自动封装成task，而task是future的子类。

   ### task:

   ​	用来做并发调度的，即对协程的进一步封装，为什么需要对协程进行进一步封装？因为单独的协程只是一个函数，而task任务，包含各种状态，异步编程需要的是对异步操作状态的把控。

   1. 创建方法：

      - task = asyncio.create_task(coro())
      - task = asyncio.ensure_future(coro())
      - loop.create_future()
      - loop.create_task(coro)

   2. 获取任务：

      - task = asyncio.current_task(loop=None)

      - asyncio = asyncio.all_tasks(loop=None)

        

   #####    多个协程函数，一起执行：

   ​		task = asyncio.wait((coro(),coro(),))  返回的是一个可等待对象

   ​		task = asyncio.gather(*args) ,返回的是一个可等待对象 (该方法也会直接将协程添加至事件循环中)

   ​		调用方式：

   ​			1. loop.run_until_complete(task) 

   ​			2. await task 

   ​			3. asyncio.create_task(task)

   ​			4. syncio.ensure_future(task)

   ​			其中1，3，4都是直接添加到当前线程中的事件循环中，2需要将其调用它的协程添加至事件循环		中