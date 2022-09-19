"""
.. module:: Table
   :synopsis: Interage com as tabelas do SIDRA.
"""

from typing import Dict

import pandas as pd

from .resources import get


def get_table(
    table_code: str,
    territorial_level: str,
    ibge_territorial_code: str,
    variable: str = None,
    classification: str = None,
    categories: str = None,
    classifications: Dict[str, str] = None,
    period: str = None,
    header: str = None,
    format: str = "pandas",
    **kwargs  # noqa
):
    """Realiza a busca da tabela no SIDRA

    Parameters
    ----------
    table_code : str
        Código da tabela de onde se deseja extrair os dados
    territorial_level : str
        Nível territorial do IBGE.

        As opções de níveis territoriais dependem da tabela selecionada.
    ibge_territorial_code : str
        Unidades territoriais do IBGE. É possível especificar múltiplos elementos utilizando vírgulas.

        As opções de unidades territoriais dependem da tabela selecionada.
    variable : str, optional (padrão=None)
        Variáveis desejadas. Caso não seja espeficiado, é retornado todas as variáveis da tabela, exceto as variáveis de percentual geradas automaticamente pelo Sidra.

        As opções de variáveis dependem da tabela selecionada.
    classifications : Dict[str, str], optional  (padrão=None)
        Classificações da tabela e suas categorias desejadas. A chave do dicionário é a classificação, e o valor são as categorias.
        É possível especificar múltiplos categorias utilizando vírgulas.

        As opções de classificação e categorias dependem da tabela selecionada.
    period : str, optional (padrão=None)
        Períodos (meses, anos etc.) desejados. Caso não seja especificado, traz apenas os períodos mais recentes.

        As opções de período dependem da tabela selecionada.
    header : str, optional (padrão=None)
        Especifica se o resultado será precedido por um registro de cabeçalho. Caso não seja espefificado, traz o cabeçalho.

        Opções:
            - 'y' - Traz o cabeçalho
            - 'n' - Não traz o cabeçalho
    format : str, optional (padrão='pandas')
        Especifica o formato retorano pela API.

        Opções:
            - 'pandas' - Retorna uma pandas Dataframe
            - 'list' - Retorna uma lista

    Returns
    -------
     - list
        Retorna os dados no formato de lista
     - pd.DataFrame
        Retorna os dados no formato de dataframe do pandas

    Examples
    --------
    >>> import sidrapy
    >>> from pprint import pprint
    >>> data = sidrapy.get_table(
        table_code="5459",
        territorial_level="1",
        ibge_territorial_code="all",
        classifications={"11278": "33460", "166": "3067,3327"},
        period="202002",
        header='n',
        format='list'
    )
    >>> pprint(data[:2])  # doctest: +NORMALIZE_WHITESPACE
    [
        {
            'D1C': '1',
            'D1N': 'Brasil',
            'D2C': '202002',
            'D2N': '2º semestre 2020',
            'D3C': '33460',
            'D3N': 'menos de 1.200 toneladas',
            'D4C': '3067',
            'D4N': 'Armazéns graneleiros e granelizados',
            'D5C': '152',
            'D5N': 'Número de estabelecimentos',
            'MC': '1020',
            'MN': 'Unidades',
            'NC': '1',
            'NN': 'Brasil',
            'V': '185'
        },
        {
            'D1C': '1',
            'D1N': 'Brasil',
            'D2C': '202002',
            'D2N': '2º semestre 2020',
            'D3C': '33460',
            'D3N': 'menos de 1.200 toneladas',
            'D4C': '3067',
            'D4N': 'Armazéns graneleiros e granelizados',
            'D5C': '153',
            'D5N': 'Capacidade útil',
            'MC': '1017',
            'MN': 'Toneladas',
            'NC': '1',
            'NN': 'Brasil',
            'V': '100870'
        }
    ]
    """
    data = get(
        table_code,
        territorial_level,
        ibge_territorial_code,
        variable,
        classification,
        categories,
        classifications,
        period,
        header,
    )

    if format == "pandas":
        return pd.DataFrame(data)
    elif format == "list":
        return data
