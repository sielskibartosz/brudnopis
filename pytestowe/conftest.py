import pytest


@pytest.fixture
def setup_teardown():
    print(f"Witam przed testem!")
    yield
    print("Zegnaj po teście!")

@pytest.fixture
def get_elements():
    return [1,2,3,4]


@pytest.fixture()
def multiply_by_two(request):
    return request.param * 2
