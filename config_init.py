import json


def config_to_haproxy(file):
    with open('haproxy/haproxy_base.cfg', 'r') as rf:
        base = rf.read()
    with open(file, 'r') as rf:
        configs = json.load(rf)
    with open('haproxy/haproxy.cfg', 'w') as f:
        for conf in configs:
            base += '    server ss-{local_port} ss:{local_port} weight 10 check inter 30000\n'.format(
                local_port=conf['local_port'])
        f.write(base)


if __name__ == '__main__':
    config_to_haproxy('client/config.json')

