import os


import jinja2
from jinja2 import Environment, FileSystemLoader, StrictUndefined

BASE_PATH = os.path.dirname(__file__)


def render(template, **kwargs):
    templates_dir = os.path.join(BASE_PATH, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir),
                      undefined=StrictUndefined,
                      trim_blocks=True,
                      lstrip_blocks=True,
                      )
    template = env.get_template(template)
    return template.render(**kwargs)
