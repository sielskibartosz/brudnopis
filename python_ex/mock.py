from unittest.mock import patch, Mock
from datetime import timedelta
import requests

def fetch_status():
    response = requests.get("https://example.com/api/status")
    # if not response.ok:
    #     raise ValueError(f"Bad response status: {response.status_code}")
    print(response.ok)
    #return response.json()["status"]

@patch("requests.get")
def test_fetch_status_extended(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.ok = True
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.elapsed = timedelta(milliseconds=150)
    mock_response.json.return_value = {"status": "ok"}

    mock_get.return_value = mock_response

    result = fetch_status()

    # Sprawdzenia
    assert result == "ok"
    mock_get.assert_called_once_with("https://example.com/api/status")
    assert mock_response.headers["Content-Type"] == "application/json"
    assert mock_response.elapsed.total_seconds() == 0.15
    assert mock_response.ok is True

@patch('requests.get')
def test_tescik(mock_requests_get):
    mock = Mock()
    mock.ok = "Dupa"
    mock_requests_get.return_value = mock
    fetch_status()


@patch("requests.get")
def test_fetch_status_bad_response_extended(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.ok = False
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.elapsed = timedelta(seconds=1)
    mock_response.json.return_value = {"status": "error"}

    mock_get.return_value = mock_response

    from python import pytest
    with pytest.raises(ValueError) as excinfo:
        fetch_status()
    assert "Bad response status" in str(excinfo.value)
