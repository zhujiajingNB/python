#### self , cls, classmethod, staticmethod区别

- 在类中定义一个函数时，需要一个默认参数，通常用self表示，可通过self访问该类中全局变量和函数。

  这样的方法需要通过类的实例去访问。

- 在函数前面添加@classmethod,该函数则必须传递一个参数，通常用cls表示class,可以通过其调用属性和方法.这样的方法可以通过类或实例访问

  ```
  class A():
  	name = "demo"
  	@classmethod
  	def test(cls):
  		cls().name
  A.test()
  A().test()
  ```

- 在函数前添加@staticmethod，则表示该函数为静态函数，该函数可以不带参数。这样的方法可以通过类或类的实例去访问。

  ```
  class A():
  	name = "demo"
  	@staticmethod
  	def test():
  		A.name
  A.test()
  A().test()
  ```

  