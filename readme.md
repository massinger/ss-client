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
    {
    "server": "your server ip",
    "local_address": "0.0.0.0",
    "local_port": "1086",  
    "server_port": "2400",
    "password": "your password",
    "method": "aes-256-cfb",
    "protocol": "origin",
    "obfs": "plain"
  }
  ]
```

- haproxy.cfg

```angular2
# ...

backend ss-out
    balance roundrobin
    option external-check
    external-check path /app/
    external-check command curl_get.sh
    server ss-1085 ss:1085 weight 10 check 
    server ss-1086 ss:1086 weight 10 check 
    
```

## build and run

```angular2
cd ss-client
docker-compose up
```
and then configure your application or browser to use proxies `socks5://127.0.0.1:25502`

