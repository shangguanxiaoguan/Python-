import pytest

"""
控制测试用例执行：
在第N个用例失败后，结束测试执行
pytest --maxfail=N 

"""


def test_fail01():
    print("第一次失败")
    assert 1 == 2


def test_fail02():
    print("第二次失败")
    assert 1 == 2


def test_fail03():
    print("第三次成功")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-s", "--maxfail=2", "09_pytest控制用例执行.py"])
