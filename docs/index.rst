.. _topics-index:

================================
sidrapy |release| - Documentação
================================

O sidrapy é uma biblioteca que oferece uma interface em python para a [API SIDRA](http://api.sidra.ibge.gov.br/) do Instituto Brasileiro de Geografia e Estatística (IBGE).

Essa ferramenta permite acessar facilmente em Python dados sobre habitação, inflação, industrias e muito mais.

Instalação
==========

O sidrapy roda em Python 3.7 ou superior.

Para instalar o sidrapy com o pip::

   pip install -U sidrapy

Início Rápido
=============

Aqui um exemplo de como utilizar essa biblioteca.
Digamos que desejamos os dados do IPCA dos ultimos 12 meses.

   import sidrapy

   data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")


Contribua
=========

Quera ajudar a melhorar o sidrapy? Contribua com o código e/ou reporte algum problema que encontrar.

- `Rastreador de Problemas`_
- `Código Fonte`_

.. _Rastreador de Problemas: https://github.com/AlanTaranti/sidrapy/issues
.. _Código Fonte: https://github.com/AlanTaranti/sidrapy

Como entrar em contato?
=======================

- `Grupo Telegram`_

.. _Grupo Telegram: https://t.me/joinchat/AmdQix1KKeZ5KGpsKVFsKw
