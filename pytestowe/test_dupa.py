import pytest

def test_example(setup_teardown):
    print("Wykonuję test!")



def test_elements(get_elements):
    assert [1,2,3,4] == get_elements

@pytest.mark.parametrize("multiply_by_two, expected", [(1,2),(3,6)], indirect=["multiply_by_two"])
def test_multiplying(multiply_by_two, expected):
    assert multiply_by_two == expected


from unittest.mock import patch, Mock
from datetime import datetime, date, timedelta, time

def daj_godzine():
    return datetime.now().time()

def test_daj_godzine():
    with patch("test_dupa.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2000, 1, 1, 15, 15, 15)
        print(daj_godzine())
