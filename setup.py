from setuptools import setup

VERSION = "0.1.1"

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(name="sidrapy", version=VERSION, install_requires=["requests", "pandas"])
