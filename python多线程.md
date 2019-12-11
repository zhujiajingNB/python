### python多线程

python中GIL在单位时间内只运行一个线程进行字节码操作，但是python的原子操作时单字节码操作，(如a+=a为多字节码操作)所以仍然存在线程安全的问题。检测代码是否为单字节码，可以用dis模块。

- 多线程的实现

  ```
  class A(threading.Thread):
  	def _init_(self,id):
  		treading.Thread_init(self)
  		#supder()._init()
  		self.id = id
  	def run(self):
  		#...
  		
  thread1 = A(01)
  thread2 = A(02)
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
  ```

- 线程同步

  ```
  class A(threading.Thread):
  	def _init_(self,id):
  		treading.Thread_init(self)
  		self.id = id
  	def run(self):
  		lock.acquire()
  		#...
  		lock.release()
  		
  lock = threading.Lock()
  thread1 = A(01)
  thread2 = A(02)
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
  ```

- 线程通信

  ```
  class A(threading.Thread):
  	def _init_(self,id):
  		treading.Thread_init(self)
  		self.id = id
  	def run(self):
  		workqueue.get()
  		#...
  workqueu = queue.Queue()
  workqueu.put(#...)
  thread1 = A(01)
  thread2 = A(02)
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
  ```

- 线程池实现

  ```
  from concurrent.futures import ThreadPoolExecutor
  def a(self, url):
  	return requests.get(url)
  with ThreadPoolExecutor（max_workers = 10） as executor:
  	futures = executor.submit(a, url)
  
  ```

- join /setDaemon

  join:主线程在子线程完成后才退出

  setDaemon:主线程完成后，子线程也会退出。