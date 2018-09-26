# Dump CLI tool to control basic BGP

### Install

`pip install -e .`

### Sample config

```
---

eos1:
  driver: eos
  hostname: 0.0.0.0
  port: 44331
  transport: https
  username: test
  password: test
  bgp:
    local-as: 65001
    neighbors:
      192.168.1.2:
        remote-as: 65002
    networks:
      - 100.100.100.0/24
eos2:
  driver: eos
  hostname: 0.0.0.0
  port: 44332
  transport: https
  username: test
  password: test
  bgp:
    local-as: 65002
    neighbors:
      192.168.1.1:
        remote-as: 65001
    networks:
      - 200.200.200.0/24

```

### Docker env
Spun-up 2 EOS docker containers.

```
cd tests/helpers
make up
```

Connect to `eos1` or `eos2`

`docker exec -it helpers_ceos1_1 Cli`

### Sample usage

```
$ bgp-bot deploy eos1
$ bgp-bot deploy eos2
$ bgp-bot show eos1 --bgp-config
{
    "_": {
        "neighbors": {
            "192.168.1.2": {
                "export_policy": "",
                "remote_as": 65002,
                "import_policy": "",
                "prefix_limit": {},
                "local_as": 65001,
                "nhs": false,
                "route_reflector_client": false,
                "local_address": "",
                "authentication_key": "",
                "description": ""
            }
        },
        "export_policy": "",
        "remote_as": 0,
        "import_policy": "",
        "prefix_limit": {},
        "local_as": 65001,
        "multihop_ttl": 0,
        "apply_groups": [],
        "local_address": "",
        "remove_private_as": false,
        "multipath": false,
        "type": "",
        "description": ""
    }
}

$ bgp-bot show eos1 --neighbors
{
    "global": {
        "router_id": "192.168.1.1",
        "peers": {
            "192.168.1.2": {
                "is_enabled": true,
                "uptime": 562,
                "remote_as": 65002,
                "description": "",
                "remote_id": "192.168.1.2",
                "local_as": 65001,
                "is_up": true,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 1,
                        "accepted_prefixes": -1,
                        "received_prefixes": 1
                    },
                    "ipv6": {
                        "sent_prefixes": 0,
                        "accepted_prefixes": -1,
                        "received_prefixes": 0
                    }
                }
            }
        }
    }
}
```
