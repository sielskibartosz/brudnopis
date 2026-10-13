import pytest



def c_to_f(temp):
    return temp * 9/5 +32

print(c_to_f(0))

@pytest.fixture
def my_fixture(n,x):
    print("dupa")
    yield n * c_to_f(x)
    print("papa")

@pytest.mark.parametrize("temperature, expected", [(0,32),(100,212)])
def test_c_to_f(temperature,expected):
    assert c_to_f(temperature) == expected
    assert c_to_f(temperature) == pytest.approx(expected, rel=1e-2)

def test_my_fixture(my_fixture):
    assert my_fixture(1,0) == 32.0


def to_hex(n:int)-> str:
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return hex(n)

def test_to_hex():
    assert to_hex(255) == '0xff'
    assert to_hex(16) == '0x10'
    with pytest.raises(ValueError):
        to_hex(-1)

"2026-10-12 14:03:22 [ERROR] sensor: timeout"
def parse_log(log_line):
    log_line
    return {"date":log_line[:10], "time":log_line[11:19],"level":log_line.startswith("[ERROR]"),"module":log_line[22:28],"message":log_line[29:]}
# @functools.wraps(func)
print(parse_log("2026-10-12 14:03:22 [ERROR] sensor: timeout"))

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                print("dupa")
        return None

    return wrapper


@retry
def error():
    raise Exception("lalal")
a = [i*2 for i in range(10) if 1%2 != 0]