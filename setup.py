import os
from distutils.core import setup
from setuptools import find_packages


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as ff:
        return ff.read()

setup(
    name='openpilot',
    version='0.1',
    author='',
    author_email='',
    url='https://github.com/commaai/openpilot',
    description='openpilot by commaai',
    long_description=(read('README.md')),
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="MIT",
    keywords="commaai openpilot",
    packages=['cereal',
              'openpilot',
              'selfdrive'],
    include_package_data=True,
    install_requires=[
        'pyzmq',
        'pycapnp',
        'raven',
        'setproctitle',
        'libusb1',
    ]
)
