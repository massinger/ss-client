#!/usr/bin/python
from gevent import monkey

monkey.patch_all()
import gevent
import json
import sys

from shadowsocks.local import main as local_main


def start_local(config):
    try:
        sys.argv = ('sslocal -c {} start'.format(config)).split()
        local_main()
    except SystemExit:
        pass


def split_config():
    with open('./config.json', 'r') as rf:
        client_datas = json.load(rf)

    for index, client_data in enumerate(client_datas):
        file_name = '/tmp/config{}.json'.format(index)
        print(file_name)
        with open(file_name, 'w') as wf:
            json.dump(client_data, wf)
        yield file_name


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(start_local, file_name) for file_name in split_config()
    ])


