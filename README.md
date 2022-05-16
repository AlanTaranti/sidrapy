# sidrapy

[![Version](https://img.shields.io/pypi/v/sidrapy.svg?style=flat)](https://pypi.python.org/pypi/sidrapy)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sidrapy)](https://pypi.python.org/pypi/sidrapy)
[![Python Version](https://img.shields.io/pypi/pyversions/sidrapy?style=flat)](https://pypi.python.org/pypi/sidrapy)
[![License](https://img.shields.io/github/license/AlanTaranti/Sidrapy)](https://github.com/AlanTaranti/sidrapy/blob/master/LICENSE)
![Maintenance](https://img.shields.io/maintenance/yes/2022)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/AlanTaranti/sidrapy/blob/master/CODE_OF_CONDUCT.md)

## O que é esse projeto? / _What is this project?_

É uma biblioteca que oferece uma interface em python para a [API SIDRA](http://api.sidra.ibge.gov.br/) do Instituto Brasileiro de Geografia e Estatística (IBGE)

O sidrapy permite acessar facilmente em Python dados sobre habitação, inflação, industrias e muito mais.

_It is a library that provides a python interface for the Brazilian Institute of Geography and Statistics (IBGE) [SIDRA API](http://api.sidra.ibge.gov.br/)._

_Sidrapy allows you to access data about housing, inflation, industries and many more in Brazil; easily in Python._


## Versões Python Suportadas / _Supported Python Versions_

Todas as versões do Python 3 oficialmente suportadas. Atualmente:
- Python 3.7+

_All officially supported Python 3 versions. Currently:_
- _Python 3.7+_

## Como instalar e utilizar esse projeto? / _How to install and use this project?_

### Instalação / _Installation_
Instale e atualize utilizando o [pip](https://pip.pypa.io/en/stable/quickstart/) (inglês):
```shell script
pip install -U sidrapy
```

_Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):_
```shell script
pip install -U sidrapy
```

### Início Rápido / _Quick Start_

Aqui um exemplo de como utilizar essa biblioteca.
Digamos que desejamos os dados do IPCA dos ultimos 12 meses.

_Here is an example of how to use this library._
_Let's assume that we want the IPCA from Brazil from last 12 months._

```python
import sidrapy

data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")
```

### Onde está a documentação da API do SIDRA? / _Where is the SIDRA API documentation?_
Aqui: http://api.sidra.ibge.gov.br/home/ajuda

_Here: http://api.sidra.ibge.gov.br/home/ajuda (brazilian portuguese)_

### E onde está a documentação do sidrapy? / _How about the sidrapy documentation?_
Aqui: https://sidrapy.readthedocs.io

_Here: https://sidrapy.readthedocs.io (brazilian portuguese)_

### Contribuindo / _Contributing_
Para obter orientações sobre como configurar o ambiente de desenvolvimento e como fazer uma contribuição para o sidrapy, consulte o [guia de contribuição](https://github.com/AlanTaranti/sidrapy/blob/master/CONTRIBUTING.md).

_For guidance on setting up a development environment and how to make a contribution to sidrapy, see the [contributing guidelines](https://github.com/AlanTaranti/sidrapy/blob/master/CONTRIBUTING_EN.md)._

## Como entrar em contato? / _How do I get in touch?_
Suporte / _Support:_
* [Grupo Telegram](https://t.me/joinchat/AmdQix1KKeZ5KGpsKVFsKw)

Mantenedor / _Maintainer_:
* Email: [contato@alantaranti.me](mailto:contato@alantaranti.me)
* Website: <a href="https://alantaranti.me" target="_blank">alantaranti.me</a>
