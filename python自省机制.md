## python自省机制

- hasattr 判断对象是否含有某个属性

- isinstance 判断是否是某个对象的实例

- __dict__ 获取和设置对象和类的属性和函数

  ```
  class A:
  	name = "tom"
  	def __init__(self):
  		sel.sex = "men"
  A.__dict__ 
  A().__dict__ (参照实例变量)
  A().__dict__update(dic) 设置对象的属性和函数（设置函数的本质是将函数赋值与变量）
  
  def test(name):
  	reurn name
  	
  # 下面两个的本质是相同的	
  A().__dict__update({"test_method":test})
  def __init__(self):
  	self.test_method = test
  A.().test_method("tom") 实现test函数
  
  ```

  

  