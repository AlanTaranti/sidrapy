from typing import Dict
from random import randint, random
from unittest.mock import Mock, MagicMock
from unittest.mock import patch
from uuid import uuid4

import pytest
from src import sidrapy


def random_args_classification():
    args = [
        "table_code",
        "territorial_level",
        "ibge_territorial_code",
        "variable",
        "classification",
        "categories",
        "period",
        "header",
    ]
    kwargs = {k: str(uuid4()) for k in args}
    for arg in args[3:]:
        if random() < 0.5:
            del kwargs[arg]

    if "classification" not in kwargs and "categories" in kwargs:
        del kwargs["categories"]

    return kwargs


def get_random_classifications() -> Dict[str, str]:
    classifications = {}
    for _ in range(randint(0, 10)):
        categories = [str(uuid4()) for __ in range(randint(0, 10))]
        classifications[str(uuid4())] = ",".join(categories)

    return classifications


def random_args():
    args = [
        "table_code",
        "territorial_level",
        "ibge_territorial_code",
        "variable",
        "classifications",
        "period",
        "header",
    ]
    kwargs = {k: str(uuid4()) for k in args}
    kwargs["classifications"] = get_random_classifications()

    for arg in args[3:]:
        if random() < 0.5:
            del kwargs[arg]

    return kwargs


def test_get_url_classification():
    for _ in range(5_000):
        kwargs = random_args_classification()
        url = sidrapy.resources.handler.get_url(**kwargs)
        assert isinstance(url, str)
        assert url.startswith("https://apisidra.ibge.gov.br/values/")
        for value in kwargs.values():
            assert value in url


def test_get_url():
    for _ in range(5_000):
        kwargs = random_args()
        url = sidrapy.resources.handler.get_url(**kwargs)
        assert isinstance(url, str)
        assert url.startswith("https://apisidra.ibge.gov.br/values/")
        for value in kwargs.values():
            if type(value) == "str":
                assert value in url
            elif type(value) == "dict":
                for k, v in value.items():
                    assert k in url
                    assert v in url
