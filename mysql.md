##### mysql事务

------

- 原子性

- 一致性

- 隔离性

- 持久性


###### 事务并发控制出现的问题

- 幻读

  事务里查询数据时未出现，插入数据时，发现数据已经存在

- 非重复读

  事务里第二次查询到上一次未查询到的数据

- 脏读

  事务里查询到其他事务未提交的修改

- 修改丢失

  不同事务覆盖了其他事务的修改

###### mysql事务隔离级别

- 读未提交

- 读已提交

- 可重复读（mysql默认的级别RR）

  事务中进行重复读的操作时，会读取第一次（即使第二次读操作前，另一个事务修改了数据）的读数据快照。但进行写操作时，如update，会读取最新的数据。所以，该隔离级别同样会出现幻读操作（只是出现在写操作中）。

- 串行化

乐观锁

​	认为修改数据时，不会有其他事务进行修改，当发现被修改后进行回滚。 利用版本或时间戳

悲观锁

​	对数据修改前，对数据库加锁，不让其他事务对数据进行修改。  select for update

参考文章：https://juejin.im/post/5c9040e95188252d92095a9e

##### innodb 和myisam引擎

------



| INNODB           | MYISAM   |
| ---------------- | -------- |
| 支持事务         |          |
| 支持行级锁、表锁 | 表锁     |
| 外键             |          |
| 索引             | 全文索引 |

##### mysql索引

------

- 普通索引
- 唯一索引
- 主键索引
- 全文索引
- 组合索引

##### 索引的实现

- B+树
- 哈希

#### 索引失效

- 以%号开头的like语句，模糊匹配
- or语句前后没有同时使用索引
- 数据类型出现隐始转换（如 varchar 不加单引号的话可能会自动转换为 int 型）
- 对于多列索引，没有满足最左匹配原则

#### 慢查询

- 配置慢查询日志
  1. slow_query_log  是否开启慢查询日志
  2. slow_query_log_file 日志存放路径
  3. long_query_time 慢查询阈值，超过记录下来
  4. log-queries-not-using-indexes 该配置记录未使用索引的sql语句
- explain排查索引使用情况

