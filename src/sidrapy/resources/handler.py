from typing import Dict

from .http_client import HttpClient

ENDPOINT_BASE = "https://apisidra.ibge.gov.br"


def get_url(
    table_code: str,
    territorial_level: str,
    ibge_territorial_code: str,
    variable: str = None,
    classification: str = None,
    categories: str = None,
    classifications: Dict[str, str] = None,
    period: str = None,
    header: str = None,
):
    query_url = ENDPOINT_BASE + "/values"

    query_url += f"/t/{table_code}"
    query_url += f"/n{territorial_level}"
    query_url += f"/{ibge_territorial_code}"

    if header:
        query_url += f"/h/{header}"

    if period:
        query_url += f"/p/{period}"

    if variable:
        query_url += f"/v/{variable}"

    if classifications is not None and classifications != "":
        for key, value in classifications.items():
            query_url += f"/c{key}"
            query_url += f"/{value}"

    else:
        if classification:
            query_url += f"/c{classification}"

            if categories:
                query_url += f"/{categories}"

    return query_url


def get(
    table_code: str,
    territorial_level: str,
    ibge_territorial_code: str,
    variable: str = None,
    classification: str = None,
    categories: str = None,
    classifications: Dict[str, str] = None,
    period: str = None,
    header: str = None,
):
    url = get_url(
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

    with HttpClient.get_legacy_session() as session:
        response = session.get(url)

    if not response.ok:
        raise ValueError(response.text)

    return response.json()
