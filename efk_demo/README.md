##### 搭建一个本地的 docker network

docker network list

docker network create mynetwork

##### 起 ES， 然后 docker logs es 把启动页的 secrets 全记下来

```sh
docker run -dit \
  --rm \
  --name es \
  --network mynetwork \
  -p 9200:9200 \
  -e "network.host=0.0.0.0" \
  -e "discovery.type=single-node" \
  elasticsearch:8.17.0
```





fluentd 内部没有默认装 es 的插件

想要把 fluentd 收集到的日志 push 到 es 里， 还需要打镜像装插件

##### 打镜像

Dockerfile

```sh
FROM fluent/fluentd:v1.17-debian-arm64-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.4.3"]
USER fluent
```

```
docker build -t cf:1.17 .
```

##### 跑 fluentd 容器

```sh
docker run -d \
  --name fff \
  --net mynetwork \
  -p 24224:24224 \
  -v $(pwd):/fluentd/etc \
  -v $(pwd)/myapp.log:/var/log/myapp.log \
  -v $(pwd)/myapp.pos:/var/log/myapp.pos \
  cf:1.17 \
  -c /fluentd/etc/fluent.conf

```



##### kibana

```sh
docker run -d \
  --rm \
  --name kb \
  --network mynetwork \
  -p 5601:5601 \
  kibana:8.17.0

```



docker logs 去 kibana 启动页拿到验证码， 输入 es 启动页的 secrets 即可使用

```
http://127.0.0.1:5601/
```



进入 kibana 页面

先给 log 文件（此处为 app.log）加一行日志

之后应该可以在 Management => Stack Management => Data => Index Management => Indices 里看到新生成的索引

然后在 Management => Stack Management => Kibana Data Views 里 create data view， 匹配已有日志的格式即可

之后即可在 Analytics => Discover 里找到新建的 data view， 查找日志



碰到的问题

- fluentd 连不上 es
  - 版本原因？
  - fluentd 配置 ssl_verify false
  - fluentd 里设置的 host 不对
    - 去 docker inspect mynetwork 看一下容器对应的 ipv4 地址多少

