from unittest.mock import patch, Mock
from datetime import timedelta
import requests

def fetch_status():
    response = requests.get("https://example.com/api/status")
    print(response.ok)

@patch('requests.get')
def test_tescik(mock_requests_get):
    mock = Mock()
    mock.ok = "Dupa"
    mock_requests_get.return_value = mock
    fetch_status()

@patch("requests.get")
def test_dwa(mock_dupa):
    pass