import pytest

@pytest.fixture
def my_fixture():
    print("start of fixture")
    yield "fixture_value"
    print("end of fixture")

def test_with_fixture(my_fixture):
    print("Using fixture value:", my_fixture)
    assert my_fixture == "fixture_value"

