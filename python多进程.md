## python多进程

python中因为CIL的存在，同一时间内，只允许一个线程在单个cpu上运行，要想充分利用多核cpu的资源，则需要使用多进程。

- python多进程模块

  multiprocessing.Process

```
from multiprocessing import Process

class A(Process):

	def _init_(self, name):
		super()._init()
		self.name = name
	
	def run(self):
		print("process name is {}".format(self.name))
if __name__ == '__main__':
	process = A("a")
	process2 = A("b")
	process.start()
	process2.start()
	process.join()
	process2.join()
```

- 