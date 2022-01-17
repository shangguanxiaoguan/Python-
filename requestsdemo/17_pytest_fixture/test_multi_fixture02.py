import pytest


@pytest.fixture()
def test1():
    a = 'zs'
    # b = '123123'
    print("test1")
    return a


@pytest.fixture()
def test2():
    b = '123123'
    print("test2")
    return b


def test03(test1, test2):
    user = test1
    psw = test2
    assert user == 'zs'
    assert psw == '1231123'
    print("传入多个fixture参数正确")


if __name__ == '__main__':
    pytest.main(["-s", "test_multi_fixture02.py"])