import requests

import sidrapy


def test_connection():
    url = sidrapy.resources.handler.ENDPOINT_BASE
    r = requests.get(url, timeout=10)
    assert r.status_code == 200


def test_sample_request():
    url = sidrapy.resources.handler.ENDPOINT_BASE
    # api docs here: http://api.sidra.ibge.gov.br/home/ajuda
    url += "/values/t/1612/p/2018/v/allxp/n1/1/d/m/h/y"
    r = requests.get(url, timeout=10)
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
