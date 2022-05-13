import random
from unittest.mock import Mock
from unittest.mock import patch
from uuid import uuid4

import pytest
from src import sidrapy


def random_args():
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
        if random.random() < 0.5:
            del kwargs[arg]
    return kwargs


def test_get_url():
    for _ in range(5_000):
        kwargs = random_args()
        url = sidrapy.resources.handler.get_url(**kwargs)
        assert isinstance(url, str)
        assert url.startswith("https://apisidra.ibge.gov.br/values/")
        for value in kwargs.values():
            assert value in url


def test_get_ok():
    mock_response = Mock()
    mock_response.ok = True
    with patch("src.sidrapy.resources.handler.requests") as mock_request:
        kwargs = random_args()
        mock_request.get.return_value = mock_response
        response = sidrapy.resources.handler.get(**kwargs)
        assert response is mock_response.json()


def test_get_not_ok():
    mock_response = Mock()
    mock_response.ok = False
    with patch("src.sidrapy.resources.handler.requests") as mock_request:
        kwargs = random_args()
        mock_request.get.return_value = mock_response
        with pytest.raises(ValueError):
            sidrapy.resources.handler.get(**kwargs)
