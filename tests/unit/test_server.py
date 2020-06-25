

from unittest.mock import patch, Mock

import pytest
import requests

import sidrapy.server


def test_create_url():
    assert sidrapy.server.create_url('/') == 'http://api.sidra.ibge.gov.br/'
    assert sidrapy.server.create_url('') == 'http://api.sidra.ibge.gov.br'
    assert sidrapy.server.create_url('x') == 'http://api.sidra.ibge.gov.br/x'
    with pytest.raises(TypeError):
        assert sidrapy.server.create_url()


def test_ping_ok():
    mock_response = Mock()
    mock_response.status_code = 200
    with patch('sidrapy.server.requests') as mock_request:
        mock_request.get.return_value = mock_response
        aux = sidrapy.server.ping()
    mock_request.get.assert_called_once_with(
        'http://api.sidra.ibge.gov.br/',
        timeout=10
    )
    assert isinstance(aux, float)
    assert aux < 1


def test_ping_timeout():
    with patch('sidrapy.server.requests') as mock:
        mock.get.side_effect = requests.exceptions.Timeout
        with pytest.raises(requests.exceptions.Timeout):
            _ = sidrapy.server.ping()


def test_ping_status_not_200():
    mock_response = Mock()
    with patch('sidrapy.server.requests') as mock_request:
        mock_request.get.return_value = mock_response
        for status in [199, 201, 400, 404, 300, 301, 302, 500]:
            mock_response.status_code = status
            with pytest.raises(sidrapy.server.ConnectionError):
                _ = sidrapy.server.ping()
