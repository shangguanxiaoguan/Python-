"""
pytest实现多进程运行测试用例：
    安装 pytest-xdist
        pip install pytest-xdist

运行模式：
    pytest -n NUMCPUS(进程数量)

"""

"""
运行时报错：ModuleNotFoundError: No module named '_pytest.resultlog'

解决办法：对pytest-rerunfailures进行了升级：pip install --upgrade pytest-rerunfailures

"""


import pytest


def test_case01():
    print("test01")
    assert 1 == 1


def test_case02():
    print("test02")
    assert 1 == 1


def test_case03():
    print("test03")
    assert 1 == 1


def test_case04():
    print("test04")
    assert 1 == 1


def test_case05():
    print("test05")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-n", "6", "10_pytest多进程运行用例.py"])
    # 使用与计算机具有的CPU内核一样多的进程
    pytest.main(["-n", "auto", "10_pytest多进程运行用例.py"])
    # pytest.main(["-s", "10_pytest多进程运行用例.py"])