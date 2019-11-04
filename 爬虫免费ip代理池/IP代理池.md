### IP代理池

地址：http://127.0.0.1:5010

#### api接口说明

| api         | method | Description      | arg           |
| ----------- | ------ | ---------------- | ------------- |
| /           | Get    | 接口介绍         | None          |
| /get        | Get    | 随机获取一个代理 | None          |
| /get_all    | Get    | 获取所有代理     | None          |
| /get_status | Get    | 查看代理数量     | None          |
| /delete     | Get    | 删除代理         | proxy=host:ip |

#### 代码示例

```
import requests

#获取ip
def get_proxy():
    return requests.get("http://192.168.0.11:5010/get/").json().get("proxy")
    
#访问百度
proxy = get_proxy()
res = requests.get(url="http://www.baidu.com",proxies={"http":"http://{}".format(proxy)})

#删除ip
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

```

### docker 

```
docker pull jhao104/proxy_pool

docker run --env db_type=REDIS --env db_host=127.0.0.1 --env db_port=6379 --env db_password=pwd_str -p 5010:5010 jhao104/proxy_pool
```

