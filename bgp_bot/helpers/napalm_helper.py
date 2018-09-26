"""NAPALM helper."""

import sys

import napalm

import misc

CONNECTION_KEYS = ['hostname', 'username', 'password']


def open_session(host, config):
    driver = napalm.get_network_driver(config[host].pop('driver'))
    transport = config[host].pop('transport', None)
    port = config[host].pop('port', None)
    device_config = {k: v for k, v in config[host].items() if k in CONNECTION_KEYS}
    if transport or port:
        optional_args = {'port': port, 'transport': transport}
        device_config['optional_args'] = optional_args
    device = driver(**device_config)
    device.open()
    return device


def execute(config, host, napalm_func):
    if host in config:
        device = open_session(host, config)
    else:
        print("No host found in config: ", host)
        sys.exit(-1)
    return getattr(device, napalm_func)()


def commit_config(config, host, config_file):
    device = open_session(host, config)
    device.load_merge_candidate(config_file)
    return device.commit_config()
