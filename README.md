# Sidrapy

[![Version](https://img.shields.io/pypi/v/sidrapy.svg?style=flat)](https://pypi.python.org/pypi/sidrapy)
[![Python Version](https://img.shields.io/pypi/pyversions/sidrapy?style=flat)](https://pypi.python.org/pypi/sidrapy)
[![License](https://img.shields.io/github/license/AlanTaranti/Sidrapy)](LICENSE)

## What is this project?

It is a library that provides a python interface for the IBGE SIDRA API.


## Requirements

- Python 3.5+
- Linux, Windows, Mac OSX or BSD

## How to install and use this project? 

### Installation
    
    pip install sidrapy
    
### Quick Start

Here is an example of how to use this library.
Let's assume that we want the IPCA from Brazil from last 12 months.


    import sidrapy
    
    data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")


### Where is the SIDRA API Documentation?
Here: http://api.sidra.ibge.gov.br/home/ajuda

## How I get in touch?
* Email: [alan.taranti@gmail.com](mailto:alan.taranti@gmail.com)
* Website: <a href="http://alantaranti.github.io" target="_blank">alantaranti.github.io</a>
