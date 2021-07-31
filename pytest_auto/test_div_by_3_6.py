import pytest

@pytest.fixture
def input_value():
    num = 39
    return num

def test_div_by_3(input_value):
    assert input_value % 3 == 0

def test_div_by_6(input_value):
    assert input_value % 6 == 0
