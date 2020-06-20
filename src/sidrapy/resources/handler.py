import requests

ENDPOINT_BASE = "https://apisidra.ibge.gov.br"


def get_url(table_code: str, territorial_level: str, ibge_territorial_code: str, variable: str = None,
            classification: str = None, categories: str = None, period: str = None, header: str = None):
    query_url = ENDPOINT_BASE + "/values"

    query_url += "/t/{}".format(table_code)
    query_url += "/n{}".format(territorial_level)
    query_url += "/{}".format(ibge_territorial_code)

    if header:
        query_url += "/h/{}".format(header)

    if period:
        query_url += "/p/{}".format(period)

    if variable:
        query_url += "/v/{}".format(variable)

    if classification:
        query_url += "/c{}".format(classification)

    if categories:
        query_url += "/{}".format(categories)

    return query_url


def get(table_code: str, territorial_level: str, ibge_territorial_code: str, variable: str = None,
        classification: str = None, categories: str = None, period: str = None, header: str = None):
    url = get_url(table_code, territorial_level, ibge_territorial_code, variable, classification, categories, period,
                  header)

    response = requests.get(url)

    if not response.ok:
        raise ValueError(response.text)

    return response.json()
