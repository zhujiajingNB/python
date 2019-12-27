
asyncio中有三类可等待对象（awaitble对象）

1. coroutine: 即协程函数

2. tasks : 任务，对协程函数的进一步封装

3. future: 它是一个“更底层”的概念，他代表一个一步操作的最终结果，因为一步操作一般用于耗时操作，结果不会立即得到，会在“将来”得到异步运行的结果，故而命名为Future。

   三者的关系：coroutine可以自动封装成task，而task是future的子类。

   ### task:

   ​	用来做并发调度的，即对协程的进一步封装，为什么需要对协程进行进一步封装？因为单独的协程只是一个函数，而task任务，包含各种状态，异步编程需要的是对异步操作状态的把控。(注意：当创建task时，就会将task任务放入当前线程的事件循环中执行)

   1. 创建方法：

      - task = asyncio.create_task(coro())
      - task = asyncio.ensure_future(coro())
      - loop.create_future()
      - loop.create_task(coro)

   2. 获取任务：

      - task = asyncio.current_task(loop=None)
      - asyncio = asyncio.all_tasks(loop=None)

   3. 取消任务:

      - ​	task.cancel()

   4. 完成时添加回调函数

      - task.add_done_callback(callback)

   5. done()

      - 任务完成，返回True

   6. result()

      - 当task任务完成时，返回结构
      - 当任务被取消时，会触发异常

      ```。
      import asyncio
      async def time_set():
          await asyncio.sleep(2)
       
      async def main():
      	# 直接添加至事件循环中
          task =asyncio.create_task(time_set())
          print(task.done())
          # task.cancel()
          # 如果不阻塞等待task,则会出现task还在执行中，main就先执行完，也可以使用await asyncio.sleep(2)，如果使用time.sleep()则会造成线程阻塞，无法切换其他协程运行
          await task
          
          print(task.done())
      
      if __name__ == '__main__':
          loop = asyncio.get_event_loop()
          loop.run_until_complete(main())
      #结论就是协程的本质是，当进行到await关键字，其后接的是可等待对象，当前协程阻塞（但是线程不会阻塞住），并切换到事件循环中的其他协程运行。
      ```

      

   #####    多个协程函数，一起执行：

   ​		task = asyncio.wait([coro(),coro(),])  返回的是一个可等待对象

   ​		task = asyncio.gather(*args) ,返回的是一个可等待对象 (*直接将任务添加至协程中)

   ​		调用方式：

   ​			1. loop.run_until_complete(task) 

   ​			2. await task 

   ​			3. asyncio.create_task(task)

   ​			4. syncio.ensure_future(task)       

   ```
   其中1，3，4都是直接添加到当前线程中的事件循环中，2需要将其调用它的协程添加至事件循环中
   ```
```

asyncio.get_event_loop()  若当前线程的事件循环还没有创建（即set_event_loop未调用），则创建一个事件       循环为当前线程的，若已经创建则返回当前线程的事件循环。

asyncio.new_event_loop(loop) 设置为当前线程的事件循环

asyncio.set_event_loop() 创建一个新事件循环



添加协程：

loop.create_task(c)

asyncio.ensure_future(c)

执行阻塞io

```
### asyncio

loop = asyncio.get_event_loop()
	executor = ThreadPoolExecutor(4)
	task =loop.run_in_executor(executor,函数，参数)  #

#### tornado中

executor = ThreadPoolExecutor(4)
		@run_on_server 修饰一个阻塞函数，为协程

tornado.ioloop.IOloop.current().run_in_executor(executor,函数，参数) 

```

多线程协程

一个创建一个线程执行事件循环

主线程中用asyncion.run_coroutine_threadsafe(函数()，loop)

注意：

​	按顺序执行的协程，仍旧是阻塞的，因为只有一个协程挂起时，并无其他协程可以切换执行。所以要使协程达到异步，需要有多个协程加入事件循环中。

```

### 知识点小记

1. 开启事件循环时，事件循环默认会维护一个线程池
2. 多线程协程，可以通过loop.call_soon_threadsafe(loop.stop)来关闭该线程的事件循环
3. run_in_excuter（None,fun） 第一个参数为None时默认调用线程池，也可以传递一个线程池或进程池