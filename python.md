##### python引用地址

python强类型语言，动态语言

对象三要素：ID ，type,data

is 和 ==：

is判断对象id是否相同，指向同一内存地址

==判断data是否相同

python中数字对象和字符串对象，在全局解释器范围会放入缓存中供重复使用，所以指向的ID不变

##### python中继承

子类不实现构造函数，默认先实现父类构造函数。子类实现构造函数则不会调用父类构造函数

###### 调用父类构造函数

```
父类._init_(self,参数)
super()._init_(参数) #不能带self参数
```

##### django中登陆

cookie 设置的过期时间，时间一到浏览器删除cookie

session 设置过期时间，时间一到删除cookie和存储的session值