### pthon序列化

- pickle模块

  1. pickle.dumps()  将python对象序列化成bytes
  2. pickle.loads() 将字节对象转化成python对象

- json模块

  1. json.dumps() 将python对象转化成json格式
  2. json.loads() 将json对象转化成python对象

- json和python内置的数据类型对应：

  | json类型   | pthon类型  |
  | ---------- | ---------- |
  | {}         | dict       |
  | []         | list       |
  | "string"   | str        |
  | 123.56     | int或float |
  | true/false | True/False |
  | null       | None       |

  