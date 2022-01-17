"""
通过标记表达式执行用例：
    pytest -m slow 会执行被装饰器@pytest.mark.slow装饰的所有测试用例

"""

import pytest
import time


def test_a_01():
    print("----------------->>> test_a_01")
    time.sleep(1)
    assert 1


@pytest.mark.slow
def test_a_02():
    print("----------------->>> test_a_02")
    time.sleep(1)
    assert 1


def test_a_03():
    print("----------------->>> test_a_03")
    time.sleep(1)
    assert 1


@pytest.mark.slow
def test_a_04():
    print("----------------->>> test_a_04")
    time.sleep(1)
    assert 1


if __name__ == '__main__':
    pytest.main(["-s", "-m", "slow", "11_pytest通过标记表达式执行用例.py"])