### 生成器、协程、异步IO

------

- #### 生成器

  python在2.2时期，第一次提出了生成器的概念。生成器是指带有yield关键字的函数，每次调用yield时会暂停，可以使用next()和send()函数恢复生成器。

  ```
  # 生成器的实现方：式列表式
  	gen = (for i in range(10))
  	
  # 生成器的实现方式
  	def fun():
  		for i in range(10):
  			yield i
  #生成器语法糖
  	for i in fun():
  		yield i
  		
      相当于 
      
      yield from fun()
  ```

- #### 协程

  协程通常又称为微线程，它是相互协作的一组子程序。所谓相互协助是指在执行函数A时，可以随时中断去处理函数B，然后又中断去处理函数A。这一过程并不是函数调用（不存在函数调用语句），整个过程看似多线程，然而协程只是一个单线程执行。协程通过yield关键字和send()操作转移执行权，协程之间不是调用者和被调用者的关系。

  协程的优势：

  1. 执行效率高，是子程序（函数）之间的切换不是线程切换，由程序自身控制，没有线程切换的开销。
  2. 单线程，不存在资源竞争问题，执行效率更高。

  ```
  from functools import wraps
  # 装饰器，预激协程
  def coroutine(fn):
      @wraps(fn)
      def wrapper(*args, **kwargs):
          gen = fn(*args, **kwargs)
          next(gen)
          return gen
      return wrapper
  
  # 生成器 - 数据生产者
  def countdown_gen(n, consumer):
      while n > 0:
          consumer.send(n)
          n -= 1
      consumer.send(None)
  
  # 协程 - 数据消费者
  @coroutine
  def countdown_con():
      while True:
          n = yield
          if n:
              print(f'Countdown {n}')
              sleep(1)
          else:
              print('Countdown Over!')
  
  
  def main():
      countdown_gen(5, countdown_con())
  ```

  ###### 历史回顾

  1. Python 2.2：第一次提出了生成器（最初称之为迭代器）的概念（PEP 255）。
  2. Python 2.5：引入了将对象发送回暂停了的生成器这一特性即生成器的`send()`方法（PEP 342）。
  3. Python 3.3：添加了`yield from`特性，允许从迭代器中返回任何值（注意生成器本身也是迭代器），这样我们就可以串联生成器并且重构出更好的生成器。
  4. Python 3.4：引入`asyncio.coroutine`装饰器用来标记作为协程的函数，协程函数和`asyncio`及其事件循环一起使用，来实现异步I/O操作。
  5. Python 3.5：引入了`async`和`await`，可以使用`async def`来定义一个协程函数，这个函数中不能包含任何形式的`yield`语句，但是可以使用`return`或`await`从协程中返回值。	

- ##### 异步IO

  异步IO,避免多余的IO响应等待，以及切换线程的CPU耗费。通过协程和asyncio及其事件循环一起使用，来实现异步IO操作。

  ```
  
  ```

  ```
  
  ```

  

