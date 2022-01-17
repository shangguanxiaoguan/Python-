"""
pytest常用插件
   pytest-HTML插件 生成测试报告
   安装方式：pip install pytest-html
   使用方法：pytest -s -v --html=用户路径/report.html

"""


import pytest


def test_case01():
    print("=======> 15_pytest_report.py")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()
