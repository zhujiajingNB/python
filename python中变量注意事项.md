## python中变量注意事项

- 场景一 默认参数

  ```
  def test(li=[], num):
  	li.append(num)
  	return li 
  test(num = 1) >>> [1]
  test(num = 2) >>>> [2]
  原因：
  	默认参数的可变参数指向同一个内存地址
  ```

- 场景二 同步异步执行

  ```
  # 生产端产生两个数据异步发送给消费端
  dic  ={}
  #　伪代码
  dic["name"] = "tom"
  # 异步发送
  await send dic
  # 覆盖字典参数
  dic["name"] = "jane"
  # 异步发送
  await send dic
  
  
  #消费端
  # 接收第一个值中（pending）
  await first_dic
  # 接收到第二个值（success）
  get dic_2 >>> {"name": "jane"}
  # 第一值接收成功
  get dic_1 >>> {"name": "jane"}
  ###############
  为什么dic_1 不为{"naem": 'tom'}
  1.首先两个dic指向的是同一个内存地址
  2.dic的最终值受最后一次修改影响
  3.同步中按先后执行顺序，会依次获取第一次修改的数据和第二次修改的数据
  3.异步中执行顺序无法确定，每次获取当前的最新修改数据，当获取dic_1的时候，dic已经修改为dic_2的值。
  4.无论同步异步，当前时间获取值就会获取当前时间指向内存地址的值。
  
  
  ```

- 场景三 实例变量和类变量

  ```
  class A:
  	num = 10
  	def change_num(self):
  		return self.num = 11
  a = A()
  a.num >>> 10
  a.change_num()
  a.num >>> 11
  A.num >>> 10
  # 类变量和实例变量的概念就不多说了，需要注意的是当类变量为可变变量时
  class A:
  	num = []
  	def change_num(self):
  		return self.append(1)
  a = A()
  a.num >>> []
  a.change_num() 
  a.num >>> [1]
  A.num >>> [1]
  ################
  1.对可变类型的类变量进行实例变量操作，也会影响到类变量的改变。
  
  ```

- 深浅拷贝

  详情请看其他文档（dict(dic)诸如此类的为浅拷贝）