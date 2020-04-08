import pandas as pd
from sidrapy.resources import get


def get_table(table_code: str, territorial_level: str, ibge_territorial_code: str, variable: str = None,
              classification: str = None, categories: str = None, period: str = None, header: str = None,
              format: str = "pandas"):
    data = get(table_code, territorial_level, ibge_territorial_code, variable, classification, categories, period,
               header)

    if format == "pandas":
        return pd.DataFrame(data)
    elif format == "list":
        return data
