python中__iter__函数的使用

迭代器和可迭代对象的区别：	

```
Iterable: 有迭代能力的对象，一个类，实现了`__iter__`，那么就认为它有迭代能力，通常此函数必须返回一个实现了`__next__`的对象，如果自己实现了，你可以返回`self`，当然这个返回值不是必须的；
Iterator: 迭代器(当然也是`Iterable`)，同时实现了`__iter__`和`__next__`的对象，缺少任何一个都不算是Iterator。
```

```
class A():
	def __iter__(self):
		return self
	def __next__(self):
		a = 1
		a += 1
		if a > 100: #循环停止条件
			raise StopIteration 
		return a
for i in A():
	print(i)
```

当类中使用iter函数时需要返回一个可迭代的对象（凡是可以用for循环的都是可迭代对象），如果返回本身的话，则需要实现next函数.凡是可以next()的可迭代对象，就是迭代器。

```
class B():
	def __iter__(self):
		for i in range(10):
			yield i
for i in B():
	print(i)
```

参考：https://www.jianshu.com/p/1b0686bc166d