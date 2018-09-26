import click

import yaml

from . import show, deploy


@click.group()
@click.option('--config', default="sample.yml",
              help="Configuration fail to use")
@click.pass_context
def run(ctx, config):
    """Main entry point."""
    if not ctx.obj:
        ctx.obj = {}
    with open(config, 'r') as f:
        ctx.obj['config'] = yaml.load(f.read())


run.add_command(show.show)
run.add_command(deploy.deploy)


if __name__ == "__main__":
    run()
