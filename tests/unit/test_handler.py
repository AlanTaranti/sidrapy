
import uuid
import random
from unittest.mock import patch, Mock

import pytest

import sidrapy


def test_dumb():
    return


def random_args():
    args = [
        'table_code',
        'territorial_level',
        'ibge_territorial_code',
        'variable',
        'classification',
        'categories',
        'period',
        'header',
    ]
    kwargs = {k: str(uuid.uuid4()) for k in args}
    for arg in args[3:]:
        if random.random() < 0.5:
            del kwargs[arg]
    return kwargs


def test_get_url():
    for i in range(5_000):
        kwargs = random_args()
        aux = sidrapy.resources.handler.get_url(**kwargs)
        assert isinstance(aux, str)
        assert aux.startswith('https://apisidra.ibge.gov.br/values/')
        for k, v in kwargs.items():
            assert v in aux


def test_get_ok():
    mock_response = Mock()
    mock_response.ok = True
    with patch('sidrapy.resources.handler.requests') as mock_request:
        kwargs = random_args()
        mock_request.get.return_value = mock_response
        aux = sidrapy.resources.handler.get(**kwargs)
        assert aux is mock_response.json()


def test_get_not_ok():
    mock_response = Mock()
    mock_response.ok = False
    with patch('sidrapy.resources.handler.requests') as mock_request:
        kwargs = random_args()
        mock_request.get.return_value = mock_response
        with pytest.raises(ValueError):
            _ = sidrapy.resources.handler.get(**kwargs)
