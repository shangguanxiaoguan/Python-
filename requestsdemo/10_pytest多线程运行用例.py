"""
pytest实现多线程运行测试用：
    安装  pip install pytest-parallel

运行模式：
    pytest test.py --workers 3 ：3个进程运行
    pytest test.py --tests-per-worker 4 ：4个线程运行
    pytest test.py --workers 2 --tests-per-worker 4 ：2个进程并行，且每个进程最多4个线程运行，即总共最多8个线程运行。


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
    # pytest.main(["-s", "10_pytest多进程运行用例.py", "10_pytest多线程运行用例.py"])
    pytest.main(["-s", "10_pytest多线程运行用例.py", "--workers=2", "--tests-per-worker=4"])
