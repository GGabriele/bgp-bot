"""Tasks related to show deployments."""
import click

import os
import sys

from helpers import napalm_helper, misc


@click.command()
@click.argument('host', type=click.STRING)
@click.pass_context
def deploy(ctx, host):
    if host not in ctx.obj['config']:
        print("No host found in config: ", host)
        sys.exit(-1)
    config_file = os.path.join("/tmp/", "bgp_config.cfg")
    with open(config_file, "w") as f:
        f.write(misc.render("bgp_config.cfg.j2", data=ctx.obj['config'][host]['bgp']))
    napalm_helper.commit_config(ctx.obj['config'], host, config_file)
