from src import sidrapy
from src.sidrapy.resources.http_client import HttpClient


def test_connection():
    url = sidrapy.resources.handler.ENDPOINT_BASE
    with HttpClient.get_legacy_session() as session:
        r = session.get(url, timeout=10)
    assert r.status_code == 200


def test_sample_request():
    url = sidrapy.resources.handler.ENDPOINT_BASE
    # api docs here: http://api.sidra.ibge.gov.br/home/ajuda
    url += "/values/t/1612/p/2018/v/allxp/n1/1/d/m/h/y"
    with HttpClient.get_legacy_session() as session:
        r = session.get(url, timeout=10)
    assert r.status_code == 200
    sample_response = [
        {
            "NC": "Nível Territorial (Código)",
            "NN": "Nível Territorial",
            "MC": "Unidade de Medida (Código)",
            "MN": "Unidade de Medida",
            "V": "Valor",
            "D1C": "Ano (Código)",
            "D1N": "Ano",
            "D2C": "Variável (Código)",
            "D2N": "Variável",
            "D3C": "Brasil (Código)",
            "D3N": "Brasil",
            "D4C": "Produto das lavouras temporárias (Código)",
            "D4N": "Produto das lavouras temporárias",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1006",
            "MN": "Hectares",
            "V": "73274337",
            "D1C": "2018",
            "D1N": "2018",
            "D2C": "109",
            "D2N": "Área plantada",
            "D3C": "1",
            "D3N": "Brasil",
            "D4C": "0",
            "D4N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1006",
            "MN": "Hectares",
            "V": "72610755",
            "D1C": "2018",
            "D1N": "2018",
            "D2C": "216",
            "D2N": "Área colhida",
            "D3C": "1",
            "D3N": "Brasil",
            "D4C": "0",
            "D4N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1017",
            "MN": "Toneladas",
            "V": "..",
            "D1C": "2018",
            "D1N": "2018",
            "D2C": "214",
            "D2N": "Quantidade produzida",
            "D3C": "1",
            "D3N": "Brasil",
            "D4C": "0",
            "D4N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "33",
            "MN": "Quilogramas por Hectare",
            "V": "..",
            "D1C": "2018",
            "D1N": "2018",
            "D2C": "112",
            "D2N": "Rendimento médio da produção",
            "D3C": "1",
            "D3N": "Brasil",
            "D4C": "0",
            "D4N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "40",
            "MN": "Mil Reais",
            "V": "282953793",
            "D1C": "2018",
            "D1N": "2018",
            "D2C": "215",
            "D2N": "Valor da produção",
            "D3C": "1",
            "D3N": "Brasil",
            "D4C": "0",
            "D4N": "Total",
        },
    ]
    assert r.json() == sample_response


def test_single_classification():
    data = sidrapy.get_table(
        table_code="5459",
        territorial_level="1",
        ibge_territorial_code="all",
        classification="11278",
        categories="39324",
        period="202002",
        format="list",
    )

    expected_response = [
        {
            "NC": "Nível Territorial (Código)",
            "NN": "Nível Territorial",
            "MC": "Unidade de Medida (Código)",
            "MN": "Unidade de Medida",
            "V": "Valor",
            "D1C": "Brasil (Código)",
            "D1N": "Brasil",
            "D2C": "Semestre (Código)",
            "D2N": "Semestre",
            "D3C": "Grupos de capacidade útil (Código)",
            "D3N": "Grupos de capacidade útil",
            "D4C": "Variável (Código)",
            "D4N": "Variável",
            "D5C": "Tipo de unidade armazenadora (Código)",
            "D5N": "Tipo de unidade armazenadora",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1020",
            "MN": "Unidades",
            "V": "6731",
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "39324",
            "D3N": "Total",
            "D4C": "152",
            "D4N": "Número de estabelecimentos",
            "D5C": "114630",
            "D5N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1017",
            "MN": "Toneladas",
            "V": "153406525",
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "39324",
            "D3N": "Total",
            "D4C": "153",
            "D4N": "Capacidade útil",
            "D5C": "114630",
            "D5N": "Total",
        },
    ]

    assert data == expected_response


def test_single_classification():
    data = sidrapy.get_table(
        table_code="5459",
        territorial_level="1",
        ibge_territorial_code="all",
        classification="11278",
        categories="39324",
        period="202002",
        format="list",
    )

    expected_response = [
        {
            "NC": "Nível Territorial (Código)",
            "NN": "Nível Territorial",
            "MC": "Unidade de Medida (Código)",
            "MN": "Unidade de Medida",
            "V": "Valor",
            "D1C": "Brasil (Código)",
            "D1N": "Brasil",
            "D2C": "Semestre (Código)",
            "D2N": "Semestre",
            "D3C": "Grupos de capacidade útil (Código)",
            "D3N": "Grupos de capacidade útil",
            "D4C": "Variável (Código)",
            "D4N": "Variável",
            "D5C": "Tipo de unidade armazenadora (Código)",
            "D5N": "Tipo de unidade armazenadora",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1020",
            "MN": "Unidades",
            "V": "6731",
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "39324",
            "D3N": "Total",
            "D4C": "152",
            "D4N": "Número de estabelecimentos",
            "D5C": "114630",
            "D5N": "Total",
        },
        {
            "NC": "1",
            "NN": "Brasil",
            "MC": "1017",
            "MN": "Toneladas",
            "V": "153406525",
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "39324",
            "D3N": "Total",
            "D4C": "153",
            "D4N": "Capacidade útil",
            "D5C": "114630",
            "D5N": "Total",
        },
    ]

    assert data == expected_response


def test_multiple_classification():
    data = sidrapy.get_table(
        table_code="5459",
        territorial_level="1",
        ibge_territorial_code="all",
        classifications={"11278": "33460", "166": "3067,3327"},
        period="202002",
        format="list",
    )

    print(data)

    expected_response = [
        {
            "D1C": "Brasil (Código)",
            "D1N": "Brasil",
            "D2C": "Semestre (Código)",
            "D2N": "Semestre",
            "D3C": "Grupos de capacidade útil (Código)",
            "D3N": "Grupos de capacidade útil",
            "D4C": "Tipo de unidade armazenadora (Código)",
            "D4N": "Tipo de unidade armazenadora",
            "D5C": "Variável (Código)",
            "D5N": "Variável",
            "MC": "Unidade de Medida (Código)",
            "MN": "Unidade de Medida",
            "NC": "Nível Territorial (Código)",
            "NN": "Nível Territorial",
            "V": "Valor",
        },
        {
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "33460",
            "D3N": "menos de 1.200 toneladas",
            "D4C": "3067",
            "D4N": "Armazéns graneleiros e granelizados",
            "D5C": "152",
            "D5N": "Número de estabelecimentos",
            "MC": "1020",
            "MN": "Unidades",
            "NC": "1",
            "NN": "Brasil",
            "V": "185",
        },
        {
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "33460",
            "D3N": "menos de 1.200 toneladas",
            "D4C": "3067",
            "D4N": "Armazéns graneleiros e granelizados",
            "D5C": "153",
            "D5N": "Capacidade útil",
            "MC": "1017",
            "MN": "Toneladas",
            "NC": "1",
            "NN": "Brasil",
            "V": "100870",
        },
        {
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "33460",
            "D3N": "menos de 1.200 toneladas",
            "D4C": "3327",
            "D4N": "Silos",
            "D5C": "152",
            "D5N": "Número de estabelecimentos",
            "MC": "1020",
            "MN": "Unidades",
            "NC": "1",
            "NN": "Brasil",
            "V": "245",
        },
        {
            "D1C": "1",
            "D1N": "Brasil",
            "D2C": "202002",
            "D2N": "2º semestre 2020",
            "D3C": "33460",
            "D3N": "menos de 1.200 toneladas",
            "D4C": "3327",
            "D4N": "Silos",
            "D5C": "153",
            "D5N": "Capacidade útil",
            "MC": "1017",
            "MN": "Toneladas",
            "NC": "1",
            "NN": "Brasil",
            "V": "141615",
        },
    ]

    assert data == expected_response
