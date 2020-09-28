#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "ansible_helpers",
    author = "jsammut",
    version = "2.0.0",
    install_requires = [
        "boto3",
        "botocore",
        "ansible==2.9.13"
    ],
    packages = find_packages(),
    description = "Helpers for developing ansible plugins/modules/etc",
    url = "http://github.vena.vpn/Infra/ansible_helpers",
)
