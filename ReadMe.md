
#### python 路由重置脚本

CentOS7 测试通过


##### 用途

避免远程修改路由时，由于路由设置错误而断网。

小心驶得万年船

##### 原理

定时ping一个ip，发现不通则重置路由，路由配置错误引起。


重置路由后，还是ping不通，直接重置网络。


##### 定时执行

```
*/5 * * * * /usr/bin/python /home/py_check.py >> /home/check.log
```