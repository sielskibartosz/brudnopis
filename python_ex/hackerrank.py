from unittest.mock import patch, Mock

import requests

def get_users_above_age(min_age: int) -> list:
    """
    Fetches users from a remote API and returns users whose age is greater than min_age.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    users = response.json()  # Let's assume each user has an 'age' key
    return [user for user in users if user.get("age", 0) > min_age]

@patch('requests.get')
def test_get_true(mock_get):
    response = Mock()
    response.status_code= 200
    response.json.return_value = {'age':20}
    mock_get.return_value = response
    assert get_users_above_age(18)[0]

@patch('requests.get')
def test_get_false(mock_get):
    response = Mock()
    response.status_code= 200
    response.json.return_value = {'age':10}
    mock_get.return_value = response
    assert not get_users_above_age(18)[0]

@patch('requests.get')
def test_get_empty(mock_get):
    response = Mock()
    response.status_code= 200
    response.json.return_value = {}
    mock_get.return_value = response
    assert get_users_above_age(18)==[]