# -*- coding: utf-8 -*-
from setuptools import setup
from src.sidrapy import VERSION

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sidrapy",
    version=VERSION,
    install_requires=[
        'requests',
        'requests[security]',
        'pandas',
    ]
)
