from setuptools import setup

with open("__version__") as version_file:
    VERSION = version_file.read().strip()

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(name="sidrapy", version=VERSION, install_requires=["requests", "pandas"])
