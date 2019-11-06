### mongod备份和恢复

#### 1.备份：

第一步，需要将当前路径移动至mongd bin目录下，也可以将mongod配置至环境变量中。

```
mongodump -h 192.168.0.11:27017 -d industry -o /run/media/jskj/DP/mongodb_backup
```

#### 2.定时任务：

```
crontab -e #编辑定时任务
crontab -l #查看定时任务
sudo service  crond start 启动定时任务
0 1 * * 3,5,7 每周三、五、日凌晨1点 备份mogodb数据库
```

#### 3.恢复

```xml
mongorestore -h 192.168.0.11:27017 -d industry /run/media/jskj/DP/mongodb_backup/industry
.... --drop 该参数代表恢复数据前删除原数据
```

#注意：备份后的数据进行修改后，再次进行备份时会覆盖原有的数据。备份无法恢复修改后的文件（document）,推断为根据objectID确定数据是否需要恢复。