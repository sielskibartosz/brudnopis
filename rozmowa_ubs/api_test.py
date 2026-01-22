import unittest

import pytest
import requests
from unittest.mock import patch, Mock

@pytest.fixture
def value():
    return 2


@pytest.fixture
def pass_id(value):
    print("dupa")
    return value


@unittest.mock.patch('requests.get')
def test_get_data(mock_get,pass_id):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id':pass_id}

    mock_get.return_value = mock_response


    url = "http://example.com/api/data"
    req = requests.get(url)
    assert req.status_code == 200
    assert req.json()['id'] == 2


def test_get_data_2(pass_id):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id':pass_id}

        mock_get.return_value = mock_response