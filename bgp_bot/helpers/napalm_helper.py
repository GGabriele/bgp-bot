"""NAPALM helper."""

import sys

import napalm


CONNECTION_KEYS = ['hostname', 'username', 'password']


def open_session(host, config):
    """Open session using napalm."""
    driver = napalm.get_network_driver(config[host].get('driver'))
    transport = config[host].get('transport', None)
    port = config[host].get('port', None)
    device_config = {k: v for k, v in config[host].items() if k in CONNECTION_KEYS}
    if transport or port:
        optional_args = {'port': port, 'transport': transport}
        device_config['optional_args'] = optional_args
    device = driver(**device_config)
    device.open()
    return device


def execute(host, config, napalm_func):
    """Execute napalm API call."""
    if host in config:
        device = open_session(host, config)
    else:
        print("No host found in config: ", host)
        sys.exit(-1)
    return getattr(device, napalm_func)()


def commit_config(host, config, config_file):
    device = open_session(host, config)
    device.load_merge_candidate(config_file)
    return device.commit_config()
