import os
from setuptools import setup

VERSION = "0.0.1"

REQUIREMENTS = open('requirements.txt', 'r').readlines()

setup(
    name="elearnix-api",
    version=VERSION,
    url="https://github.com/qprichard/elearnix-api",
    author="qprichard hugofloter",
    install_require=REQUIREMENTS,
    tests_require=['mock', 'pytest']
)
