import pytest


@pytest.fixture()
def first_entry():
    return "a"


@pytest.fixture()
def order(first_entry):
    return [first_entry]


def test_string(order):
    order.append("b")
    assert order == ["a", "b"]


if __name__ == '__main__':
    pytest.main(["-s", "fixture调用fixture.py"])
