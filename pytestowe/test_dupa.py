from python_ex import pytest


def test_example(setup_teardown):
    print("Wykonuję test!")



def test_elements(get_elements):
    assert [1,2,3,4] == get_elements

@pytest.mark.parametrize("multiply_by_two, expected", [(1, 2), (3, 6)], indirect=["multiply_by_two"])
def test_multiplying(multiply_by_two, expected):
    assert multiply_by_two == expected


from unittest.mock import patch, Mock
from datetime import datetime, time
import random

def daj_godzine():
    return datetime.now().time()

def losuj_liczbe():
    return random.randint(1,100)

def test_losuj_liczbe(mocker):
    fixed_value = mocker.patch('test_dupa.random.randint')
    fixed_value.return_value = 42
    assert losuj_liczbe()==42

def test_daj_godzine_patch():
    # Tworzymy mock dla zwracanej instancji
    fake_now = Mock()
    fake_now.time.return_value = time(15, 15)

    with patch("test_dupa.datetime") as mock_datetime:
        mock_datetime.now.return_value = fake_now
        assert daj_godzine() == time(15, 15)