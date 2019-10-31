### Write Idiom Python

- python支持链式结构

  ```
  #bad
  a = 5
  if a > 2 and a < 7:
  	pass
  #good
  if 2 < a < 7:
  	pass
  ```

- python变量交换

  ```
  #bad
  a = 2
  b = 3
  temp = a
  b = temp
  b = a
  #good
  a = 2
  b = 3
  a, b = b, a
  ```

- python中三代目运算符?:

  ```
  #bad
  a = 3 
  b = 5
  if a > b:
  	c = a
  else:
  	c = b
  #good
  c = a if a > b else b
  ```

- 格式化字符串

  ```
  #bad
  str1 = "the apple price is "+price
  str = "the apple price is %s" % (price)
  #good
  str3 = "the apple price is {} ".format(price)
  ```

- 条件判断

  ```
  #bad
  name == None
  #good
  name is None
  ```

- 列表与字典

  ```
  #bad
  nums = range(1,11)
  list = []
  for i in nums:
  	if i % 2 == 0:
  		list.append(i)
  #good
  list = [i for i in range(1, 11) if i % 2 == 0]
  
  #bad
  user_list = [{'name': 'lucy', 'email': 'lucy@g.com'}, {'name': 'lily', 'email': 'lily@g.com'}]
  user_email = {}
  for user in user_list:
      if 'email' in user:
          user_email[user['name']] = user['email']
  #good
  {user['name']: user['email'] for user in user_list if 'email' in user}
  
  ```

- 遍历索引

  ```
  #bad
  list = range(5)
  index = 0
  for i in list:
  	print("{}, {}".format(index, i))
  	index += 1
  #good
  for index,i in enumerate(list):
  	print(index,i)
  ```

- 使用生成器返回消耗内存的对象

  ```
  #bad
  def a():
  	#...
  	return list
  #good
  def a():
  	#...
  	for i in list:
  		yield i 
  	
  ```

  