# redis

- 数据类型
  1. string
  2. has
  3. list
  4. set
  5. zset
  
- 持久化策略
  1. RDB
  2. AOF

- redis主从

- redis哨兵

- redis集群

- 缓存
  1. （缓存穿透、缓存雪崩、缓存击穿）
  2. 双写一致
  
- 线程模型

  内部采用文件事件处理器，该处理器是单线程的。

  - 多个socket
  - io多路复用
  - 文件事件分派器
  - 事件处理器

- 效率高的原因

  - io多路复用
  - 内存操作
  - 单线程避免多线程的上下文切换问题，预防多线程竞争问题

  

参考：https://www.jianshu.com/p/fa29d4ef9cc7