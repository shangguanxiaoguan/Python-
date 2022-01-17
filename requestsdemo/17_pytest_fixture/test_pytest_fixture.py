import pytest


@pytest.fixture
def first_fix():
    return ["a"]


def test_case01(first_fix):
    first_fix.append("b")
    assert first_fix == ["a", "b"]
    print(first_fix)


if __name__ == '__main__':

    pytest.main(["-s"])   # 以这种方式运行，文件名必须以test_开头

