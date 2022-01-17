import pytest


@pytest.fixture()
def test1():
    a = 'zs'
    b = '123123'
    print("test1")
    return (a, b)


def test03(test1):
    user = test1[0]
    psw = test1[1]
    assert user == 'zs'
    assert psw == '123123'


if __name__ == '__main__':
    pytest.main(["-s", "test_multi_fixture01.py"])