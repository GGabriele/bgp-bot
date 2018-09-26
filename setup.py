"""setup.py file."""
from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

__author__ = '???'
__license__ = '???'

setup(name='bgp_bot',
      description="Dumb BGP bot",
      author=__author__,
      url='https://github.com/GGabriele/bgp_bot',
      include_package_data=True,
      install_requires=reqs,
      packages=find_packages(exclude=("test*", )),
      entry_points={
          'console_scripts': {
              "bgp-bot = bgp_bot.main:run",
          }
      },
      license=__license__,
      test_suite='tests',
      platforms='any',
      classifiers=[
          'Programming Language :: Python :: 2.7'
        ]
      )
