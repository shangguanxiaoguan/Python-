"""
安装： pip install pytest-rerunfailures

运行模式：


"""


import pytest
import time


def test_a_01():
    print("----------------->>> test_a_01")
    # time.sleep(1)
    assert 1


def test_a_02():
    print("----------------->>> test_a_02")
    # time.sleep(1)
    assert 1 == 2


def test_a_03():
    print("----------------->>> test_a_03")
    # time.sleep(1)
    assert 1 == 2


def test_a_04():
    print("----------------->>> test_a_04")
    # time.sleep(1)
    assert 1


if __name__ == '__main__':
    # 使用--reruns命令，指定运行测试的最大次数
    # pytest.main(["--reruns", "3", "12_pytest失败重跑.py"])
    # 要在两次重试之间增加延迟时间， 使用--reruns-delay，指定在下一次测试重新开始之前等待的秒数
    pytest.main(["--reruns", "2", "--reruns-delay", "1", "12_pytest失败重跑.py"])