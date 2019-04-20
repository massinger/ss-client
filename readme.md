# ss-client load balancing

## install docker and docker-compose 

- [docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

## git clone 

```angular2
git clone https://github.com/sazima/ss-client.git
```

## Change configuration file

- config.json

```angular2
[
  {
    "server": "your server ip",
    "local_address": "0.0.0.0",
    "local_port": "1085",  
    "server_port": "2400",
    "password": "your password",
    "method": "aes-256-cfb",
    "protocol": "origin",
    "obfs": "plain"
  },
  #...
  ]
```

- haproxy.cfg

```angular2
# ...
    server ss-1081 ss:1081 weight 10 check
    server ss-1082 ss:1082 weight 10 check
    server ss-1083 ss:1083 weight 10 check
    server ss-1084 ss:1084 weight 10 check
    server ss-1085 ss:1085 weight 10 check
    server bad-1 ss:1080 weight 10 check
```

## build and run

```angular2
cd ss-client
docker build -t haproxy:v1 haproxy/
docker build -t sslocal:v1 client/
docker-compose up
```
and then configure your application or browser to use proxies `socks5://127.0.0.1:25502`

