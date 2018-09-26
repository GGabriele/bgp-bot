"""Tasks related to show deployments."""
import click

import sys
import json

from helpers import napalm_helper


@click.command()
@click.argument('host', type=click.STRING)
@click.option('--neighbors/--no-neighbors', default=False,
              help="Show neighbors")
@click.option('--bgp-config/--no-bgp-config', default=False,
              help="Show all configuration")
@click.option('--neighbors-detail/--no-neighbors-detailt', default=False,
              help="Show neighbors detail")
@click.pass_context
def show(ctx, host, neighbors, bgp_config, neighbors_detail):
    if not neighbors and not bgp_config and not neighbors_detail:
        print("At least one from 'neighbors', 'bgp_config' or 'neighbors_detail' should be used")
        sys.exit(-1)

    if (neighbors and (bgp_config or neighbors_detail) or
            bgp_config and (neighbors or neighbors_detail) or
            neighbors_detail and (bgp_config and neighbors)):
        print("At most one from 'neighbors', 'bgp_config' or 'neighbors_detail' should be used")
        sys.exit(-1)

    if neighbors:
        func = 'get_bgp_neighbors'
    elif neighbors_detail:
        func = 'get_bgp_neighbors_detail'
    else:
        func = 'get_bgp_config'
    print json.dumps(napalm_helper.execute(ctx.obj['config'], host, func), indent=4)
