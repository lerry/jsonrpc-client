#! /usr/bin/env python
# -*- coding: utf-8 -*-
import jsonclient
from setuptools import setup, find_packages

setup(
    name='jsonrpc-client',
    version=jsonclient.__version__,
    description="Another python json-rpc client",
    author="Lerry",
    license='MIT',
    author_email="lvdachao@gmail.com",
    packages=['jsonclient'],
    platforms = 'any',
    install_requires = [
       'requests>=2.0',
    ],
    url = "https://github.com/lerry/jsonrpc-client",
)